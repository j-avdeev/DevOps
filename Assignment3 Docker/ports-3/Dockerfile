FROM python:3.7

RUN mkdir /sync-folder

WORKDIR /sync-folder

ENTRYPOINT ["python3", "-m", "http.server", "--bind", "0.0.0.0", "8080"]