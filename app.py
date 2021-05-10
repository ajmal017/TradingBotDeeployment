from flask import Flask, request, abort
from kiteconnect import KiteConnect
import pandas as pd
import json


app = Flask(__name__)


kite = KiteConnect(api_key="60sdy72jltn7a949")

data = kite.generate_session("35AALoqX4qEH2VbOwZal3XKAV1ukL4H7", api_secret="cbjxfw3tek45p7thq3yywyy5gsvuc4t8")
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
        
        print(data_recieved)
        print(type(data_recieved))
        
        try:        
            order_id = kite.place_order(tradingsymbol=data_recieved['Name'],
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=data_recieved['direction'],
                                        quantity=data_recieved['contracts'],
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product='MIS',
                                        variety = "regular")
        
            print("Order placed.")
        except Exception as e:
            print(e.message)

        return '', 200

if __name__ == '__main__':
    app.run()
