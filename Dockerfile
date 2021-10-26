FROM python:3.8-alpine

COPY /app /app

WORKDIR /app 

RUN chmod +x hello-world.py

ENTRYPOINT [“python”, “hello-world.py”]
