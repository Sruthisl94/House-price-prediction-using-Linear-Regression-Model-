# House-price-prediction-using-Linear-Regression-Model-
## Task:  Build and Deploy a Machine Learning Model for Predicting House Prices
This project predicted House price using a Linear Regression model. The trained model is deployed as a web API using FastAPI. The API allows users to send house features as input and receive a predicted price in response. The deployment was done using Render after pushing necessary files to GitHub.
## Building and Running the model
1. The model is trained and saved it as .joblib file.
2. The trained model (House_Price_prediction.joblib) is loaded in app.py to serve predictions.

## Understanding app.py
app.py is the core FastAPI script that loads the trained model and serves predictions via an API endpoint.
### Key Components of app.py:<br>
Import necessary libraries: FastAPI, Joblib, Pandas, and Pydantic.<br>
Load the trained model: The House_Price_prediction.joblib is loaded using joblib.load().<br>
Define the API structure:<br>
Root (/) endpoint: Confirms the API is running.<br>
/predict endpoint: Accepts JSON input and returns the predicted house price.<br>
Run the FastAPI application using Uvicorn.

## Running FastAPI API locally
1. Start the API Server<br>
   python -m uvicorn app:app --reload
2. Open API Documentation (Swagger UI)<br>
   Open http://127.0.0.1:8000/docs in the web browser
   Here you can test the /predict endpoint
## API Usage
POST/predict
This endpoint takes house features in JSON format and returns the predicted price.
Example request:
 <p>{<br>
    <p>"OverallQual": 6.0, <br>
   <p> "YearBuilt": 1963.0, <br>
    <p>"YearRemodAdd": 2003, <br>
    <p>"TotalBsmtSF": 1059.0, <br>
   <p> "FstFlrSF": 1068.0, <br>
   <p> "GrLivArea": 1068.0, <br>
   <p> "FullBath": 1, <br>
    <p>"GarageCars": 1.0, <br>
   <p> "GarageArea": 264.0, <br>
   <p> "ExterQualencoded": 3, <br>
   <p> "BsmtQualencoded": 4, <br>
   <p> "KitchenQualencoded": 3 <br>
  <p>} <br>
Example Response<br>
 <p>{<br>
    <p> "predicted_price": 145526.5 <br>
} <br>

## Testing the API using Postman
The API can be tested using Postman
1. Open postman > Create New Request
2. Select POST method
3. Enter the URL http://127.0.0.1:8000/predict
4. Go to Body > Raw > JSON and enter the example request data
5. Click Send and check the response

## Deploying API using Render
1. Create a repository on Github initially unchecking the readme file. 
   eg: House_Price_Prediction.git
2. Push the required files to Github
   Since only three files are required for deployment, push only app.py, House_Price_prediction.joblib, requiremnts.txt
   The requiremnts.txt file is created manually which contain the intalling dependencies.
   <p>git init<br>  
   <p> git add app.py House_Price_prediction.joblib requirements.txt <br>
   <p>git commit -m "Added API and model for deployment"  <br>
   <p> git branch -M main  <br>
   <p> git remote add origin https://github.com/yourusername/House_Price_Prediction.git  <br>
   <p> git push -u origin main  <br>

3. Deploy on Render
   * Go to Render and create a new Web Service
   * Connect your GitHub repository.
      * Build Command: pip install -r requirements.txt
      * Start Command: uvicorn app:app --host 0.0.0.0 --port 8000
   * Click Deploy Service and wait for the API to be hosted.
4. Get the Live API URL <br>
   **https://house-price-api-sjhx.onrender.com**
5. Visit  **https://house-price-api-sjhx.onrender.com/docs** to test the API online.
6. API Usage
POST/predict
   This endpoint takes house features in JSON format and returns the predicted price.
   Example request:
 <p>{<br>
 <p>"OverallQual": 6.0, <br>
   <p> "YearBuilt": 1963.0, <br>
    <p>"YearRemodAdd": 2003, <br>
    <p>"TotalBsmtSF": 1059.0, <br>
   <p> "FstFlrSF": 1068.0, <br>
   <p> "GrLivArea": 1068.0, <br>
   <p> "FullBath": 1, <br>
    <p>"GarageCars": 1.0, <br>
   <p> "GarageArea": 264.0, <br>
   <p> "ExterQualencoded": 3, <br>
   <p> "BsmtQualencoded": 4, <br>
   <p> "KitchenQualencoded": 3 <br>
Example Response<br>
 <p>{<br>
    <p> "predicted_price": 250000.5 <br>
} <br>

## Author
Sruthi S L<br>
Email: sruthisl2012@gmail.com
   
   
     
   
