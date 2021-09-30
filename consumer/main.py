import faust
import os
import time

class data(faust.Record, serializer='json'):
  credit_score_1: float
  credit_score_2: float
  credit_score_3: float
  credit_score_4: float
  score: float

KAFKA_SERVER = os.getenv('KAFKA_SERVER')
KAFKA_PORT = os.getenv('KAFKA_PORT')
KAFKA_CONN = 'kafka://' +  KAFKA_SERVER + ':' + KAFKA_PORT
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')

app = faust.App('data_faust',
                broker=KAFKA_CONN,
                topic_partitions=4,
                )
app_topic = app.topic('data', value_type=data)

@app.agent(app_topic)
async def send_notifications(predictions):
  async for pred in predictions:
    print(pred)

time.sleep(40)
app.start()
