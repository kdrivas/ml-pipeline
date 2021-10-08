from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from app.api import scores

app = FastAPI()

app.include_router(scores.router)

@app.get('/check_service', status_code=status.HTTP_201_CREATED)
def root():
  return {'Message': 'Hello world from service 1'}

