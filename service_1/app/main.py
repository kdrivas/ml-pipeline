from fastapi import FastAPI, status

app = FastAPI()

@app.get('/check_service', status_code=status.HTTP_201_CREATED)
def root():
  return {'Message': 'Hello world from service 1'}

