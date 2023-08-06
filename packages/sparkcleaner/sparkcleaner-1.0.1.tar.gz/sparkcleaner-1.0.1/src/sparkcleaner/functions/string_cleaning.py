from typing import List
import pyspark.sql.functions as F
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql.types import DataType
import src.sparkcleaner.helpers.verify as verify


def remove_leading_zeros(df: SparkDataFrame,
                         col_name: str,
                         maintain_type: bool = True):
    """Remove leading zeros from column using regex.

    Parameters
    ----------
    (required) df: pyspark.sql.DataFrame
        Pyspark DataFrame containing column to be processed
    (required) col_name: str
        name of column to remove leading zeros from
    (optional) maintain_type: bool
        If false, returns col as str.
        If true, returns col as type before function call

    Returns
    ----------
    pyspark.sql.DataFrame
        processed column in place

    See Also
    ----------
    pyspark.sql.functions.regexp_replace()
    pyspark.sql.Column.cast()

    Example
    ----------
    my_df = remove_leading_zeros(my_df, "MY_COL", False)
    """
    input_vals: List[type] = [SparkDataFrame, str, bool]
    expected_vals: List[type] = [type(df),
                                 type(col_name),
                                 type(maintain_type)]

    verify.verify_func_input(input_vals, expected_vals)

    original_type: DataType = df.schema[col_name].dataType
    df = df.withColumn(col_name, F.regexp_replace(F.col(col_name),
                                                  r'^[0]*', ""))
    if maintain_type:
        df = df.withColumn(col_name,
                           F.col(col_name)
                            .cast(original_type)
                            .alias(col_name))
    return df
