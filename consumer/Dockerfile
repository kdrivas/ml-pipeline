FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev python-dev build-essential

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["faust", "-A", "main", "worker", "-l", "info"]