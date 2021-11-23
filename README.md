# weather-linebot
Create a bot that periodically notifies you of weather forecasts using the LINE API and an API that obtains weather forecasts from longitude and latitude information.

</br>

# Usage
## 1. Clone Codes
```
$ git clone https://github.com/zawa1120/weather-linebot.git
```

## 2. Create a Configuration File
Create a Configuration file based on k8s-config.yml.samle.

## 3. Deploy Containers
```
$ bash build.sh
```

</br>

# Requirements
- macOS Big Sur 11.6 Intel

</br>

- docker 20.10.8  
- Kubernetes v1.21.2

</br>

# Optional commands

## Disable CronJob
```
$ kubectl patch cronjob weather-bot -p '{ "spec": { "suspend": true } }'
```

## Restart CronJob
```
$ kubectl patch cronjob weather-bot -p '{ "spec": { "suspend": false } }'
```

## Run CronJob Manually
```
$ kubectl create job manually --from=cronjob/weather-bot
```

</br>

# References

## Weather API

### API
https://api.rakuten.net/weatherbit/api/weather?endpoint=apiendpoint_5067b308-eb68-4d2d-b0ae-e135dbd646d8

### Documents
https://www.weatherbit.io/api/weather-forecast-120-hour

## Line API
### Documents
https://developers.line.biz/ja/reference/messaging-api/#send-push-message
