import faust
import os
import time
import requests

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def telegram_bot_sendtext(bot_message):
  send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + CHAT_ID + '&parse_mode=Markdown&text=' + bot_message
  print(send_text)
  response = requests.get(send_text)

  return response.json()

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
    telegram_bot_sendtext("We found..." + str(pred.credit_score_4))

time.sleep(40)
app.start()
