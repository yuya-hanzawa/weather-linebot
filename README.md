# weather-bot
Practice Docker and Kubernetes \
OS: macOS Big Sur 11.6

## How to create Bot
```
Version
docker: 20.10.8
Kubernetes: v1.21.2
```

### 1. Clone Code
```
git clone https://github.com/zawa1120/weather-bot.git
```

### 2. Deploy Containers
```
bash build.sh
```

## Optional Command

### Suspend cronjob
```
kubectl patch cronjob weather-bot -p '{ "spec": { "suspend": true } }'
```

### Restart cronjob
```
kubectl patch cronjob weather-bot -p '{ "spec": { "suspend": false } }'
```

### Run cronjob manually
```
kubectl create job manually --from=cronjob/weather-bot
```

## Weather API
### API
https://api.rakuten.net/weatherbit/api/weather/endpoints

### Documents
https://www.weatherbit.io/api/weather-forecast-5-day

## Line API
### Documents
https://developers.line.biz/ja/reference/messaging-api/#send-push-message
