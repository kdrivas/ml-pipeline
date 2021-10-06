from fastapi import APIRouter, Form, status
from kafka import KafkaProducer

import os
import json
import time

KAFKA_SERVER = os.getenv('KAFKA_SERVER')
KAFKA_PORT = os.getenv('KAFKA_PORT')
KAFKA_CONN = KAFKA_SERVER + ':' + KAFKA_PORT
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')

def get_kafka_producer():
  for _ in range(100):
    time.sleep(3)
    try:
      return KafkaProducer(bootstrap_servers=KAFKA_CONN,
                          value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                          retries=5)
    except:
      print('Error: Loading Kafka Producer')

kafka_producer = get_kafka_producer()

router = APIRouter(
  prefix="/scores",
  tags=["scores"],
)

@router.app('/')
def root():
  return {'message': 'Hello from score route'}

@router.post('/send_data_1', status_code=status.HTTP_201_CREATED)
async def send_data(sepal_length: str = Form(...), 
                    petal_length: str = Form(...),
                    sepal_width: str = Form(...),
                    petal_width: str = Form(...)):
  
  kafka_producer.send(KAFKA_TOPIC, {'credit_score_1': float(sepal_length), 
                                    'credit_score_2': float(sepal_width), 
                                    'credit_score_3': float(petal_length), 
                                    'credit_score_4': float(petal_width),
                                    'score': 1})
  kafka_producer.flush()

  return {'S': 'clase'} 

@router.get('/get_dummy', status_code=status.HTTP_200_OK)
async def dummy(): 
  return {'S': 'clase'} 