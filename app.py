from fastapi import FastAPI
from pydantic import BaseModel
from rules import predict_risk
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

class CustomerData(BaseModel):
    tickets_last_30: int
    monthly_increase: bool
    contract: str
    complaint_ticket: bool

@app.get("/")
def home():
    return {"message": "Churn Prediction API Running"}

@app.post("/predict-risk")
def predict(data: CustomerData):
    result = predict_risk(data.dict())
    
    logging.info(f"Prediction made: {result}")
    
    return {"risk": result}