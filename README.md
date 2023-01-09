## 前提

- docker, docker-compose がインストールされていること

## 環境構築

1. 本リポジトリを clone する

2. clone したリポジトリ配下で `docker-compose up`を実行(**cpu 環境の場合は、 `docker-compose -f docker-compose-cpu.yml up`を実行すること!**)

## 実行 notebook

- eda.ipynb: データの可視化などを実施

- forecast_with_arima_model.ipynb: ARIMA モデルを使用した予測

- forecast_with_prophet.ipynb: Prophet を使用した予測

- forecast_with_dl_model.ipynb: 深層学習モデルを使用した予測

- compare_result.ipynb: 各モデルの評価指標を可視化

## 使用モデル

- 過去 1 年間のトレンドをそのまま予測値とするモデル(ベースライン)

- ARIMA

- Prophet

- Prophet の予測結果 + lightGBM

- cnn(予測範囲データの最後の 3 ステップ分を使用)

- lstm

## 結果

トレンドに 0 が多いので、予測結果がバイアスを持っただけの値になることが多い(変動せずに一定の値を出力するだけのモデル)。

対策として、0 部分を近傍の非 0 の値の平均等で埋めるなどを実施するとよいかもしれない。
