FROM python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev python-dev build-essential

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

EXPOSE 8000

CMD ["alembic", "upgrade", "head &&", "uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]