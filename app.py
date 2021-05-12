from flask import Flask, request, abort
from kiteconnect import KiteConnect
import pandas as pd
import json
import logging


app = Flask(__name__)


kite = KiteConnect(api_key="60sdy72jltn7a949")
print("***********************************************************************")

kite.set_access_token("1b9tm4jed5ITEDIeri3adFJb8RzuuvSS")
print("***********************************************************************")




@app.route('/')
def home():
    return "Hello Deployemnt Working"


@app.route('/hit')
def hit():
    return "Hello Tradingview Hit"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("*******************")
    if request.method == 'POST':
        print("*******************")
        data_recieved =json.loads(request.data)
        
        print(data_recieved['direction'])
        print(data_recieved['Name'])
        print(data_recieved['contracts'])
        
        dir = data_recieved['direction']
        if dir == "buy":
            direction_LS = kite.TRANSACTION_TYPE_BUY
        else:
            direction_LS = kite.TRANSACTION_TYPE_SELL
     

        order_id = kite.place_order(tradingsymbol=data_recieved['Name'],
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=direction_LS,
                                    quantity=data_recieved['contracts'],
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product='MIS',
                                    variety = "regular")
        
        return '', 200

if __name__ == '__main__':
    app.run()
