from fastapi import FastAPI, status

app = FastAPI()

@app.get('/service_1', status_code=status.HTTP_201_CREATED)
def root():
  return {'Message': 'Hello world from service 1'}

@app.post('/model_1', status_code=status.HTTP_201_CREATED)
async def get_predictions_from_model():
  return {'Prediction': 'clase'} 