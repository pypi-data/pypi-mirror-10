from .base import ExperimenterBase
import time
import inspect
import numpy as np
import h5py


DATASET_COMPRESS_THRESHOLD = 512


def hdf5_attrs(**kwargs):
    def wrapper(obj):
        obj.hdf5_attrs = kwargs
        return obj
    return wrapper


class ExperimenterHDF5(ExperimenterBase):

    def init_results(self):
        time_start = time.time()

        self.h5group = self.h5file.create_group('experimenter_%s' % int(time_start))
        self.h5groups = []
        self.h5datasets = []

        self.h5group.attrs['_is_experiment'] = True
        self.h5group.attrs['name'] = self.name
        self.h5group.attrs['time_sec'] = time_start
        self.h5group.attrs['time_str'] = time.ctime(time_start)

        if hasattr(self, 'hdf5_attrs'):
            for k, v in self.hdf5_attrs.items():
                self.h5group.attrs[k] = v

        for step_ind, step in enumerate(self.steps):
            dtypes_all = [(name, dtype)
                          for step in self.steps[:step_ind + 1]
                          for name, dtype in step._args.as_dtypes_dict.items()] +\
                         [(name, dtype)
                          for name, dtype in step._results.items()]
            dtype = np.dtype([(name, dtype if dtype != np.ndarray else h5py.special_dtype(ref=h5py.Reference))
                              for name, dtype in dtypes_all])

            step_group = self.h5group.create_group('step_%d' % step_ind)

            step_group.attrs['ind'] = step_ind
            step_group.attrs['name'] = step.__name__
            step_group.attrs['args_names'] = step._args.names
            step_group.attrs['cum_args_names'] = [name
                                                  for step in self.steps[:step_ind + 1]
                                                  for name in step._args.names]
            step_group.attrs['results_names'] = step._results.keys()
            step_group.attrs['code'] = inspect.getsource(step)

            if hasattr(step, 'hdf5_attrs'):
                for k, v in step.hdf5_attrs.items():
                    step_group.attrs[k] = v

            length = np.prod([len(step._args_prod_values)
                              for step in self.steps[:step_ind + 1]])
            is_compress = length * dtype.itemsize > DATASET_COMPRESS_THRESHOLD
            step_ds = step_group.create_dataset('scalars',
                                                shape=(length,),
                                                dtype=dtype,
                                                compression='lzf' if is_compress else None,
                                                shuffle=True,
                                                fletcher32=True)
            step_ds.attrs['written_cnt'] = 0

            for name, dtype in dtypes_all:
                if dtype == np.ndarray:
                    step_group.create_group('%s_values' % name)

            self.h5groups.append(step_group)
            self.h5datasets.append(step_ds)

        self.h5file.flush()

    def add_result(self, step_ind, args, result):
        group = self.h5groups[step_ind]
        ds = self.h5datasets[step_ind]
        row_ind = ds.attrs['written_cnt']

        for k, v in args.items() + result.items():
            if not isinstance(v, np.ndarray):
                ds[row_ind, k] = v
            else:
                is_compress = v.nbytes > DATASET_COMPRESS_THRESHOLD
                new_ds = group.create_dataset('%s_values/%d' % (k, ds.attrs['written_cnt']),
                                              data=v,
                                              compression='lzf' if is_compress else None,
                                              shuffle=True,
                                              fletcher32=True)
                ds[row_ind, k] = np.array((new_ds.ref,), dtype=np.dtype([(k, h5py.special_dtype(ref=h5py.Reference))]))

        ds.attrs['written_cnt'] = row_ind + 1
        self.h5file.flush()
