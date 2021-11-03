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

# パラメーターの引数

## JobとCronJob特有のパラメーター

```
- completions: 実行成功回数、設定した回数Jobが正常終了するまで続く(途中で変更不可)
- parallelism: 並列数、設定した数のJobを並列に同時実行する
- baskoffLimit: 実行失敗を許容する回数

restartPolicy: 異常終了した時にどのように再起動するかを決めるパラメーター
- OnFailure: 再度同一のPodを利用してJobを再開する
- Never: 新規Podが作成される
``` 

## CronJob特有のパラメーター

```
ConcurrencyPolicy: 同時実行に関するパラメータ 
- Allow: 同時実行を許容する
- Forbid: 実行中のJobがあった場合、新規Jobをスキップする
- Replace: 実行中のJobを停止し、新規Jobに置き換える

successfulJobsHistoryLimit: 成功したJobをPod内に保存する数
failedJobsHistoryLimit: 失敗したJobをPod内に保存する数
```

## Weather API
### API
https://api.rakuten.net/weatherbit/api/weather/endpoints

### Documents
https://www.weatherbit.io/api/weather-forecast-5-day

## Line API
### Documents
https://developers.line.biz/ja/reference/messaging-api/#send-push-message
