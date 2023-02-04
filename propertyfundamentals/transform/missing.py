
import pandas as pd


@static_method
def replace_with_static(df: pd.DataFrame, value: object) -> pd.DataFrame:
    return df.fillna(value)


@static_method
def replace_with_mean(df: pd.DataFrame) -> pd.DataFrame:
    return df.fillna(df.mean())


@static_method
def replace_with_neighbour(df: pd.DataFrame) -> pd.DataFrame:
    # TODO
    return df
