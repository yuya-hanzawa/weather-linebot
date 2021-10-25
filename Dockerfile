FROM python:3.8-alpine

COPY hello-world.py hello-world.py

RUN chmod +x /hello-world.py

ENTRYPOINT [“python”, “hello-world.py”]
