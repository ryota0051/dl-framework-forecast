# 学習に使用するデータのカラム類
class Columns:
    date = "日"
    tensorflow = "TensorFlow: (日本)"
    pytorch = "PyTorch: (日本)"
    keras = "Keras: (日本)"
    caffe = "Caffe: (日本)"
    deeplearning4j = "Deeplearning4j: (日本)"


target_column_list = [
    Columns.tensorflow,
    Columns.pytorch,
    Columns.keras,
    Columns.caffe,
    Columns.deeplearning4j,
]


# Prophetに用いるカラム類
class ProphetTrainDfColumns:
    ds = "ds"
    y = "y"


class ProphetForecastColumns:
    ds = "ds"
    y = "yhat"


# 保存先ファイル名
scores_file_name = "scores.csv"
submission_file_name = "submission.csv"
