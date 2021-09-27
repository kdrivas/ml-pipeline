from fastapi import FastAPI, status

app = FastAPI()

@app.get('/', status_code=status.HTTP_201_CREATED)
def root():
  return {'Message': 'Hello world'}

@app.post('/user_stats', status_code=status.HTTP_201_CREATED)
async def get_predictions_from_model():
  return {'Prediction': 'clase'} 