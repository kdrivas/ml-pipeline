FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev python-dev build-essential

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY app/ .

CMD ["alembic", "upgrade", "head", "&&", "uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]