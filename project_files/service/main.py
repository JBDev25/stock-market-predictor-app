from typing import Union, Optional, List

from fastapi import FastAPI

from model import StockModel

import logging

app = FastAPI()



MODEL = StockModel('./saved_model/my_model','../data/all_stocks_5yr.csv')

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict/{stock_name}/{n_days}")
def predict(stock_name: str,n_days:Optional[int]=1):

    res = MODEL.predict(stock_name,n_days)

    return {"stock_name": stock_name,'prices':res}
