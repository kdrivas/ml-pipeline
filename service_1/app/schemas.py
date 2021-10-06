from pydantic import BaseModel

class PredictionBase(BaseModel):
  credit_score_1: float
  credit_score_2: float
  credit_score_3: float
  credit_score_4: float

class Prediction(PredictionBase):
  id: int

  class Config:
    orm_mode = True