import fnmatch
import operator
import zipfile
from io import StringIO
from numbers import Number
from typing import Any, Callable, Dict, List, Literal, Sequence, Tuple, Union

import numpy as np
import pandas as pd
from loguru import logger

from .filename_utils import replace_extension
from .utils import now_timestamp

DataFrameFilenameTuple = Tuple[pd.DataFrame, str]


def faster_to_dict_records(df: pd.DataFrame) -> List[dict]:
    data: List[Any] = df.values.tolist()
    columns: List[str] = df.columns.tolist()
    return [dict(zip(columns, datum)) for datum in data]


def setup_pandas():

    pd.set_option("max_rows", None)
    pd.set_option("max_columns", None)
    pd.set_option('colheader_justify', 'left')
    pd.set_option('max_colwidth', 300)


def set_default_options():

    set_options(max_rows=None, max_columns=None, colheader_justify='left', max_colwidth=300)


def set_options(**kwargs):
    for k, v in kwargs.items():
        pd.set_option(k, v)


def _create_mask(df: pd.DataFrame, name: str, value: Any, sign: bool = True) -> np.ndarray:
    if isinstance(
        value,
        (
            list,
            set,
        ),
    ):
        m = df[name].isin(value)
    elif isinstance(value, tuple):
        m = df[name].between(*value)
    elif isinstance(value, (bool, Number, str)):
        m = df[name] == value
    else:
        m = df[name] == value
    if not sign:
        m = ~m
    return m


def create_mask2(df: pd.DataFrame, masks: Sequence[dict]) -> np.ndarray:

    v = np.repeat(True, len(df.index))
    for m in masks:
        v &= _create_mask(df, **m)
    return v


class CreateMaskError(Exception):
    def __init__(self):
        super().__init__(
            """
        Tuple length must be 2 or 3 and first element must be sign, second (optional) a binary op.
    """
        )


def create_mask(doc: pd.DataFrame, args: dict) -> np.ndarray:
    """Creates a mask based on key-values in `criterias`

    Each key-value in `criterias` specifies a filter. The filters are combined using boolean `and`.

    Args:
        doc (pd.DataFrame): Data frame to mask
        criterias (dict): Dict with masking criterias

    Raises:
        ValueError: [description]

    Returns:
        np.ndarray: [description]
    """
    mask = np.repeat(True, len(doc.index))

    if len(doc) == 0:
        return mask

    for attr_name, attr_value in args.items():

        attr_sign = True
        attr_binary_operator: Union[str, Callable] = None

        if attr_value is None:
            continue

        if attr_name not in doc.columns:
            continue

        if isinstance(attr_value, tuple):

            if len(attr_value) not in (2, 3):
                raise CreateMaskError()

            if len(attr_value) == 3:
                attr_sign, attr_binary_operator, attr_value = attr_value
            else:

                if isinstance(attr_value[0], bool):
                    attr_sign, attr_value = attr_value
                elif callable(attr_value[0]) or isinstance(attr_value[0], str):
                    attr_binary_operator, attr_value = attr_value
                else:
                    raise ValueError(f"expected bool, callable or operator name, found {attr_value[0]}")

            if isinstance(attr_binary_operator, str):
                if not hasattr(operator, attr_binary_operator):
                    raise ValueError(f"operator.{attr_binary_operator} not found")
                attr_binary_operator = getattr(operator, attr_binary_operator)

        value_serie: pd.Series = doc[attr_name]

        attr_mask = (
            attr_binary_operator(value_serie, attr_value)
            if attr_binary_operator is not None
            else value_serie.isin(attr_value)
            if isinstance(attr_value, (list, set))
            else value_serie == attr_value
        )

        if attr_sign:
            mask &= attr_mask
        else:
            mask &= ~attr_mask

    return mask


class PropertyValueMaskingOpts:
    """A simple key-value filter that returns a mask set to True for items that fulfills all criterias"""

    def __init__(self, **kwargs):
        super().__setattr__('data', kwargs or {})

    def __getitem__(self, key: int):
        return self.data[key]

    def __len__(self):
        return len(self.data)

    def __setattr__(self, k, v):
        self.data[k] = v

    def __getattr__(self, k):
        try:
            return self.data[k]
        except KeyError:
            return None

    @property
    def props(self) -> Dict:
        return self.data

    def mask(self, doc: pd.DataFrame) -> np.ndarray:

        return create_mask(doc, self.data)

    def apply(self, doc: pd.DataFrame) -> pd.DataFrame:
        if len(self.hot_attributes(doc)) == 0:
            return doc
        return doc[self.mask(doc)]

    def hot_attributes(self, doc: pd.DataFrame) -> List[str]:
        """Returns attributes that __might__ filter tagged frame"""
        return [
            (attr_name, attr_value)
            for attr_name, attr_value in self.data.items()
            if attr_name in doc.columns and attr_value is not None
        ]


def try_split_column(
    df: pd.DataFrame,
    source_name: str,
    sep: str,
    target_names: List[str],
    drop_source: bool = True,
    probe_size: int = 10,
) -> pd.DataFrame:

    if df is None or len(df) == 0 or source_name not in df.columns:
        return df

    if probe_size > 0 and not df.head(probe_size)[source_name].str.match(rf".+{sep}\w+").all():
        return df

    df[target_names] = df[source_name].str.split(sep, n=1, expand=True)

    if source_name not in target_names and drop_source:
        df.drop(columns=source_name, inplace=True)

    return df


def pandas_to_csv_zip(
    zip_filename: str, dfs: Union[DataFrameFilenameTuple, List[DataFrameFilenameTuple]], extension='csv', **to_csv_opts
):
    if not isinstance(dfs, (list, tuple)):
        raise ValueError("expected tuple or list of tuples")

    if isinstance(dfs, (tuple,)):
        dfs = [dfs]

    with zipfile.ZipFile(zip_filename, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for (df, filename) in dfs:
            if not isinstance(df, pd.core.frame.DataFrame) or not isinstance(filename, str):
                raise ValueError(
                    f"Expected Tuple[pd.DateFrame, filename: str], found Tuple[{type(df)}, {type(filename)}]"
                )
            filename = replace_extension(filename=filename, extension=extension)
            data_str = df.to_csv(**to_csv_opts)
            zf.writestr(filename, data=data_str)


def pandas_read_csv_zip(zip_filename: str, pattern='*.csv', **read_csv_opts) -> Dict:

    data = dict()
    with zipfile.ZipFile(zip_filename, mode='r') as zf:
        for filename in zf.namelist():
            if not fnmatch.fnmatch(filename, pattern):
                logger.info(f"skipping {filename} down't match {pattern} ")
                continue
            df = pd.read_csv(StringIO(zf.read(filename).decode(encoding='utf-8')), **read_csv_opts)
            data[filename] = df
    return data


def ts_store(data: pd.DataFrame, *, extension: Literal['csv', 'xlsx', 'clipboard'], basename: str):

    filename = f"{now_timestamp()}_{basename}.{extension}"
    if extension == 'xlsx':
        data.to_excel(filename)
    elif extension == 'csv':
        data.to_csv(filename, sep='\t')
    elif extension == 'clipboard':
        data.to_clipboard(sep='\t')
        filename = "clipboard"
    else:
        raise ValueError(f"unknown extension: {extension}")
    logger.info(f'Data stored in {filename}')


def rename_columns(df: pd.DataFrame, columns: List[str] = None) -> pd.DataFrame:
    df.columns = columns
    return df
