docker build -t weather-bot:latest .
kubectl apply -f k8s-config.yml,k8s-cronjob.yml
