# stock-market-predictor-app
Simple stock market predictor to predict the following n days close for the S&amp;P500.

Data was pulled from [link](https://www.kaggle.com/code/faressayah/stock-market-analysis-prediction-using-lstm/data?select=all_stocks_5yr.csv)

## EDA
Data was extracted and checked for various features including;
- Stationarity/Seasonality
- Autocorrelation
- Trend

## Model Trials
Three models were trialed:
1) ARIMA
2) Prophet (Facebooks Forecasting model)
3) LSTM forecasting 

All models used only previous close data as input and no other features.

## Model Selection
LSTM was selected as the model of choice as it perfomred the best in terms of mean squared error.

## Implmentation
A simple web API was constructed to call the pre-trained model to predict iteratively foreward n days.

## Conclusion 
The model is a good approximation of stock market price for the following day but errors compound quickly as the prediction window is extended.
