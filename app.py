

import numpy as np
import pandas as pd
import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
# Loading the pretrained model
model,expected_features=joblib.load('House_Price_prediction.joblib')
app=FastAPI()
class Housefeatures(BaseModel):
    OverallQual:float
    YearBuilt:float
    YearRemodAdd:int
    TotalBsmtSF:float
    FstFlrSF:float
    GrLivArea:float
    FullBath:int
    GarageCars:float
    GarageArea:float
    ExterQualencoded:int
    BsmtQualencoded:int
    KitchenQualencoded:int
    
@app.get("/")
def index():
    return {"message": "House price prediction API is running"}

@app.post("/predict")
def predict_houseprice(data:Housefeatures):
    input_data=data.dict()
    # Ensue feature names should match training order
    input_data["1stFlrSF"] = input_data.pop("FstFlrSF")
    input_df=pd.DataFrame([input_data])
    input_df = input_df[expected_features]
    prediction = model.predict(input_df)
    
    return {"predicted_price": float(prediction[0])}