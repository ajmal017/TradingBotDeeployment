from flask import Flask, request, abort
from kiteconnect import KiteConnect
import pandas as pd
import json


app = Flask(__name__)


kite = KiteConnect(api_key="60sdy72jltn7a949")

data = kite.generate_session("bK0GTX4f870tvVCgykCsZn2zbKVoeeVz", api_secret="cbjxfw3tek45p7thq3yywyy5gsvuc4t8")
kite.set_access_token(data["access_token"])

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
     

        order_id = kite.place_order(tradingsymbol="IDEA",
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type="BUY",
                                    quantity=5,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product='MIS',
                                    variety = "regular")
        
        return '', 200

if __name__ == '__main__':
    app.run()
