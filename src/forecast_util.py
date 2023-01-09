import random

import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_absolute_error, mean_squared_error

from src.constants import target_column_list


def calc_scores(y_true: np.ndarray, y_pred: np.ndarray):
    """以下の評価指標を返す
    - mean absolute error
    - mean squared error
    - mean absolute percentage error
    """
    mae_score = mean_absolute_error(y_true, y_pred)
    rmse_score = np.sqrt(mean_squared_error(y_true, y_pred))
    mape_score = mape(y_true, y_pred)
    return {"mae": mae_score, "rmse": rmse_score, "mape": mape_score}


def mape(y_true: np.ndarray, y_pred: np.ndarray):
    """平均絶対パーセント誤差を返す
    Args:
        y_true: 正解値
        y_pred: 予測値
    """
    return np.mean(np.abs((y_true - y_pred) / (y_true + 1e-9)))


def get_result_base_dict(framework_list=target_column_list):
    return [
        {"framework": target_column, "rmse": 0, "mape": 0, "mae": 0}
        for target_column in framework_list
    ]


class LogConverter:
    def to_log(self, target):
        return 0 if target == 0 else np.log10(target)

    def to_base(self, target):
        return 0 if target == 0 else 10**target


def reset_random_seeds(seed=0):
    tf.random.set_seed(seed)
    np.random.seed(seed)
    random.seed(seed)
