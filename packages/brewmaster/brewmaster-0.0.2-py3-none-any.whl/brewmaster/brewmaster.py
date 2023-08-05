import numpy as np
import pandas as pd

from tqdm.contrib.concurrent import thread_map, process_map
from pandas.core.accessor import CachedAccessor, _register_accessor


def register_groupby_accessor(name):
    from pandas.core.groupby import DataFrameGroupBy

    return _register_accessor(name, DataFrameGroupBy)


class BrewMaster:

    def __init__(self, pandas_obj, progress_bar=True):

        self._obj = pandas_obj
        self._progress_bar = progress_bar

        return

    def progress_bar(self, enable=True):

        self._progress_bar = enable

        return self

    def _map_series_iterable(self, *args):
        if args:
            return map(lambda x: (x, *args), self._obj)
        else:
            return self._obj

    def _map_dataframe_iterable(self, *args):
        if args:
            return map(lambda x: (x[1], *args), self._obj.iterrows())
        else:
            return map(lambda x: x[1], self._obj.iterrows())

    def _map_groupby_iterable(self, *args):
        if args:
            return map(lambda x: (x[1], *args), self._obj)
        else:
            return map(lambda x: x[1], self._obj)


@pd.api.extensions.register_series_accessor('brewmaster')
class SeriesAccessor(BrewMaster):

    def __init__(self, pandas_obj):

        super(SeriesAccessor, self).__init__(pandas_obj)

        return

    def thread_apply(self, func, *args, **tqdm_kwargs):

        res = pd.Series(
            thread_map(
                func,
                self._map_series_iterable(*args),
                disable=not self._progress_bar,
                total=len(self._obj),
                **tqdm_kwargs
            )
        )

        return res

    def process_apply(self, func, *args, **tqdm_kwargs):

        res = pd.Series(
            process_map(
                func,
                self._map_series_iterable(*args),
                disable=not self._progress_bar,
                total=len(self._obj),
                **tqdm_kwargs
            )
        )

        return res


@pd.api.extensions.register_dataframe_accessor('brewmaster')
class DataFrameAccessor(BrewMaster):

    def __init__(self, pandas_obj):

        super(DataFrameAccessor, self).__init__(pandas_obj)

        return

    def thread_apply(self, func, *args, **tqdm_kwargs):

        res = pd.DataFrame(
            thread_map(
                func,
                self._map_dataframe_iterable(*args),
                disable=not self._progress_bar,
                total=len(self._obj),
                **tqdm_kwargs
            )
        )

        return res

    def process_apply(self, func, *args, **tqdm_kwargs):

        res = pd.DataFrame(
            process_map(
                func,
                self._map_dataframe_iterable(*args),
                disable=not self._progress_bar,
                total=len(self._obj),
                **tqdm_kwargs
            )
        )

        return res


@register_groupby_accessor('brewmaster')
class DataFrameGroupByAccessor(BrewMaster):

    def __init__(self, pandas_obj):

        super(DataFrameGroupByAccessor, self).__init__(pandas_obj)

        return

    def thread_apply(self, func, *args, **tqdm_kwargs):

        res = pd.DataFrame(
            thread_map(
                func,
                self._map_groupby_iterable(*args),
                disable=not self._progress_bar,
                total=len(self._obj),
                **tqdm_kwargs
            ),
            index=np.array(
                [value for _, value in self._obj.groups.items()]
            ).reshape(-1)
        )

        return res

    def process_apply(self, func, *args, **tqdm_kwargs):

        res = pd.DataFrame(
            process_map(
                func,
                self._map_groupby_iterable(*args),
                disable=not self._progress_bar,
                total=len(self._obj),
                **tqdm_kwargs
            ),
            index=np.array(
                [value for _, value in self._obj.groups.items()]
            ).reshape(-1)
        )

        return res
