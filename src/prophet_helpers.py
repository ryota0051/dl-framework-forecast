import pandas as pd

from src.constants import Columns, ProphetTrainDfColumns


def get_trainable_df(
    df: pd.DataFrame, target_column: str, date_column: str = Columns.date
):
    return df[[date_column, target_column]].rename(
        columns={
            date_column: ProphetTrainDfColumns.ds,
            target_column: ProphetTrainDfColumns.y,
        }
    )
