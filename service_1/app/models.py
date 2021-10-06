from enum import Flag
from sqlalchemy import Column, Integer, Float, Integer

from .database import Base

class Prediction(Base):
  __table_name__ = "predictions"

  id = Column(Integer, primary_key=True, index=True)
  credit_score_1 = Column(Float)
  credit_score_2 = Column(Float)
  credit_score_3 = Column(Float)
  credit_score_4 = Column(Float)
  pred = Column(Integer)
