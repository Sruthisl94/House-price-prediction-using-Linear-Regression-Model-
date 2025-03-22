# House-price-prediction-using-Linear-Regression-Model-
## Task:  Build and Deploy a Machine Learning Model for Predicting House Prices
This project predicted House price using a Linear Regression model. The trained model is deployed as a web API using FastAPI. The API allows users to send house features as input and receive a predicted price in response. The deployment was done using Render after pushing necessary files to GitHub.
## Building and Running the model
1. The model is trained ans saved it as .joblib file
2. The trained model (House_Price_prediction.joblib) is loaded in app.py to serve predictions.

## Running FastAPI API locally
1. Start the API Server
   python -m uvicorn app:app --reload
2. Open API Documentation (Swagger UI)
   Open http://127.0.0.1:8000/docs in the web browser
   Here you can test the /predict endpoint
## API Usage
POST/predict
This endpoint takes house features in JSON format and returns the predicted price.
Example request:
{
    "OverallQual": 7,
    "YearBuilt": 2005,
    "YearRemodAdd": 2010,
    "TotalBsmtSF": 1200.5,
    "FstFlrSF": 1500,
    "GrLivArea": 2500,
    "FullBath": 2,
    "GarageCars": 2,
    "GarageArea": 500,
    "ExterQualencoded": 3,
    "BsmtQualencoded": 2,
    "KitchenQualencoded": 3
}
Example Response
{
    "predicted_price": 250000.5
}

## Testing the API using Postman
The API can be tested using Postman
1. Open postman > Create New Request
2. Select POST method
3. Enter the URL http://127.0.0.1:8000/predict
4. Go to Body > Raw > JSON and enter the example request data
5. Click Send and check the response

## Deploying API using Render
1. Create a repository on Github initially inchecking the readme file. 
   eg: House_Price_Prediction.git
2. Push the required files to Github
   Since only three files are required for deployment, push only app.py, House_Price_prediction.joblib, requiremnts.txt
   The requiremnts.txt file is created manually which contain the intalling dependencies.
   
git init  git add app.py House_Price_prediction.joblib requirements.txt  git commit -m "Added API and model for deployment"  git branch -M main  git remote add origin https://github.com/yourusername/House_Price_Prediction.git  git push -u origin main

3. Deploy on Render
   * Go to Render and create a new Web Service
   * Connect your GitHub repository.
      * Build Command: pip install -r requirements.txt
      * Start Command: uvicorn app:app --host 0.0.0.0 --port 8000
   * Click Deploy Service and wait for the API to be hosted.
4. Get the Live API URL
   
     
   
