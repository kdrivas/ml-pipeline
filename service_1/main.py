from fastapi import FastAPI, status
from kafka import KafkaProducer

import os
import json

KAFKA_SERVER = os.getenv('KAFKA_SERVER')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
KAFKA_CONN = KAFKA_SERVER + ':' + KAFKA_TOPIC
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')

def get_kafka_conn():
  for _ in range(100):
    try:
      return KafkaProducer(bootstrap_servers=KAFKA_CONN,
                          retries=5)
    except:
      print('Error: Loading Kafka Producer')

kafka_producer = get_kafka_conn()
app = FastAPI()

@app.get('/service_1', status_code=status.HTTP_201_CREATED)
def root():
  return {'Message': 'Hello world from service 1'}

@app.post('/model_1', status_code=status.HTTP_201_CREATED)
async def get_predictions_from_model():
  kafka_producer.send(KAFKA_TOPIC, json.dumps())
  kafka_producer.flush()
  return {'Prediction': 'clase'} 

@app.post('/model_1', status_code=status.HTTP_201_CREATED)
async def get_predictions_from_model():
  kafka_producer.send(KAFKA_TOPIC, json.dumps())
  kafka_producer.flush()
  return {'Prediction': 'clase'} 