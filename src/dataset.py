import os

import pandas as pd

from src.constants import Columns


def get_forecast_df(
    csv_root: str,
    train_csv_name: str = "train.csv",
    submit_csv_path: str = "submit.csv",
    ans_csv_path: str = "ans.csv",
):
    """予測対象のデータフレームを取得する
    Args:
        csv_root: csvデータのルートパス

    Returns:
        以下のcsvを読み込んだデータフレーム
        - train.csv
        - submit.csv
        - ans.csv
    """
    # train.csv読み込み
    train_df = pd.read_csv(os.path.join(csv_root, train_csv_name))
    train_df[Columns.date] = pd.to_datetime(train_df[Columns.date])
    # submit.csv読み込み
    submit_df = pd.read_csv(os.path.join(csv_root, submit_csv_path))
    submit_df[Columns.date] = pd.to_datetime(submit_df[Columns.date])
    # ans.csv読み込み
    # 1行目の[カテゴリ： ソフトウェア]を飛ばして読み込む
    ans_df = pd.read_csv(os.path.join(csv_root, ans_csv_path), skiprows=1)
    ans_df[Columns.date] = pd.to_datetime(ans_df[Columns.date])
    return (train_df, submit_df, ans_df)
