from fastapi import FastAPI, status

app = FastAPI()

@app.get('/service_2', status_code=status.HTTP_201_CREATED)
def root():
  return {'Message': 'Hello world from service 2'}

@app.post('/model_2', status_code=status.HTTP_201_CREATED)
async def get_predictions_from_model():
  return {'Prediction': 'clase'} 