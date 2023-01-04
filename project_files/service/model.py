import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class StockModel:
    def __init__(self,model_path,data_path):
        self.__model = tf.keras.models.load_model('saved_model/my_model')
        self.__stocks = pd.read_csv(data_path)
        
    def predict(self,stock_name,n_days):
        return self.predict_next_n_days(self.extract_stock(stock_name),n_days)

    def predict_next_n_days(self,series,n):
        close_prices = series['close']
        values = close_prices.values
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(values.reshape(-1,1))
        x = scaled_data[-60:,0]
        for i in range(n):
            x = np.append(x,self.__model.predict(np.array([x])))
            x = x[1:]
            
        return list(scaler.inverse_transform([x[-n:]])[0])
                    
    
    def extract_stock(self,stock_name):
        return self.__stocks[self.__stocks['Name']==stock_name].reset_index(drop=True)
    