from flask import Flask, request, abort
from kiteconnect import KiteConnect
import pandas as pd





app = Flask(__name__)


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
        data_recieved =request.data.decode('utf8').replace("'", '"')
        
        print(data_recieved)
        print(type(data_recieved))

        return '', 200

if __name__ == '__main__':
    app.run()
