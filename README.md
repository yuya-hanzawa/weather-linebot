# weather-bot
DockerとKubernetesの練習&勉強 \
OS: macOS Big Sur 11.6

# Botの作成方法
```
Version
docker: 20.10.8
Kubernetes: v1.21.2
```

## 1. コードをクローン
```
git clone https://github.com/zawa1120/weather-bot.git
```

## 2. コンテナをデプロイ
```
bash build.sh
```

# オプションコマンド

## cronjobの停止
```
kubectl patch cronjob weather-bot -p '{ "spec": { "suspend": true } }'
```

## cronjobの再起動
```
kubectl patch cronjob weather-bot -p '{ "spec": { "suspend": false } }'
```

## 手動でcronjobを起動
```
kubectl create job manually --from=cronjob/weather-bot
```

# パラメーターと引数
カッコ内はデフォルトのパラメーター

## JobとCronJob特有のパラメーター

```
- completions: 実行成功回数、設定した回数Jobが正常終了するまで続く(途中で変更不可) (parallelismと同じ数)
- parallelism: 並列数、設定した数のJobを並列に同時実行する (1)
- baskoffLimit: 実行失敗を許容する回数 (6)

restartPolicy: 異常終了した時にどのように再起動するかを決めるパラメーター(必須)
- OnFailure: 再度同一のPodを利用してJobを再開する
- Never: 新規Podが作成される

PodとJobでそれぞれ別のrestartPolicyが存在する
同じ引数でも挙動が異なるので確認必須
``` 

## CronJob特有のパラメーター

```
concurrencyPolicy: 同時実行に関するパラメータ 
- Allow: 同時実行を許容する (デフォルト)
- Forbid: 実行中のJobがあった場合、新規Jobをスキップする
- Replace: 実行中のJobを停止し、新規Jobに置き換える

successfulJobsHistoryLimit: 成功したJobをPod内に保存する数 (３)
failedJobsHistoryLimit: 失敗したJobをPod内に保存する数 (３)
```

## Weather API
### API
https://api.rakuten.net/weatherbit/api/weather?endpoint=apiendpoint_5067b308-eb68-4d2d-b0ae-e135dbd646d8

### Documents
https://www.weatherbit.io/api/weather-forecast-120-hour

## Line API
### Documents
https://developers.line.biz/ja/reference/messaging-api/#send-push-message
