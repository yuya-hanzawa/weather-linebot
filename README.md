# weather-linebot
DockerとKubernetesの練習&勉強  
LINEのAPIと経度・緯度から天気予報を取得するAPIを使用し、定期的に天気予報を通知するBotを作成する

</br>

# Botの作成方法
使用環境  
OS: macOS Big Sur 11.6  
チップ: Intel

Version  
docker: 20.10.8  
Kubernetes: v1.21.2

</br>

## 1. コードをクローン
```
$ git clone https://github.com/zawa1120/weather-linebot.git
```

## 2. コンテナをデプロイ
```
$ bash build.sh
```

</br>

# オプションコマンド

## CronJobの停止
```
$ kubectl patch cronjob weather-bot -p '{ "spec": { "suspend": true } }'
```

## CronJobの再起動
```
$ kubectl patch cronjob weather-bot -p '{ "spec": { "suspend": false } }'
```

## 手動でCronJobを起動
```
$ kubectl create job manually --from=cronjob/weather-bot
```

</br>

# パラメーターと引数
## JobとCronJob専用のパラメーター

| パラメーター | 引数 | 概要 | デフォルト値 |
| :--: | :--: | ---- | :--: |
| parallelism | - | 並列数、設定した数のJobを並列に同時実行 | 1 |
| completions | - | 実行成功回数、設定した回数Jobが正常終了するまで続く(途中で変更不可) | parallelismと同じ数 |
| baskoffLimit | - | 実行失敗を許容する回数 | 6 |
| restartPolicy | (2) | 異常終了した時にどのように再起動するかを決めるパラメーター | 選択必須 |
| L | OnFailure | 再度同一のPodを利用してJobを再開 | - |
| L | Never | 新規Podを作成 | - |

</br>

`PodとJobでそれぞれ別のrestartPolicyが存在する
同じ引数でも挙動が異なるので確認必須`

</br>

## CronJob専用のパラメーター

| パラメーター | 引数 | 概要 | デフォルト値 |
| :--: | :--: | ---- | :--: |
| concurrencyPolicy | (3) | 同時実行に関するパラメータ | Allow |
| L | Allow | 同時実行を許容 | - |
| L | Forbid | 実行中のJobがあった場合、新規Jobをスキップ| - |
| L | Replace | 実行中のJobを停止し、新規Jobに置換 | - |
| successfulJobsHistoryLimit| - | 成功したJobをPod内に保存する数 | 3 |
| failedJobsHistoryLimit | - | 失敗したJobをPod内に保存する数 | 3 |

</br>

# 参照
## Weather API
### API
https://api.rakuten.net/weatherbit/api/weather?endpoint=apiendpoint_5067b308-eb68-4d2d-b0ae-e135dbd646d8

### Documents
https://www.weatherbit.io/api/weather-forecast-120-hour

## Line API
### Documents
https://developers.line.biz/ja/reference/messaging-api/#send-push-message
