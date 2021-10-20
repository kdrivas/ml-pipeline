from fastapi import APIRouter, Form, status, Depends
from kafka import KafkaProducer
from joblib import load

from app.crud import create_record
from app.schemas import PredictionCreate
from .deps import get_session

import os
import json
import time

pipeline = load('pipeline.joblib')

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

@router.get('/')
def root():
  return {'message': 'Hello from score route'}

@router.post('/send_data_1', status_code=status.HTTP_201_CREATED)
async def send_data(credit_score_1: str = Form(...), 
                    credit_score_2: str = Form(...),
                    credit_score_3: str = Form(...),
                    credit_score_4: str = Form(...),
                    db = Depends(get_session)):

  pred = pipeline.predict([[credit_score_1, credit_score_2, credit_score_3, credit_score_4]])
  item = PredictionCreate(credit_score_1 = credit_score_1, 
                          credit_score_2 = credit_score_2, 
                          credit_score_3 = credit_score_3, 
                          credit_score_4 = credit_score_4, 
                          pred = pred)
  new_item = create_record(db, item)

  kafka_producer.send(KAFKA_TOPIC, {'credit_score_1': float(credit_score_1), 
                                    'credit_score_2': float(credit_score_2), 
                                    'credit_score_3': float(credit_score_3), 
                                    'credit_score_4': float(credit_score_4),
                                    'score': int(pred)})
  kafka_producer.flush()

  print(new_item)
  return {'S': 'clase'} 

@router.get('/get_dummy', status_code=status.HTTP_200_OK)
async def dummy(): 
  return {'S': 'clase'} 