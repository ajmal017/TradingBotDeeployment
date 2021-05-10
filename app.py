from flask import Flask, request, abort
from kiteconnect import KiteConnect
import pandas as pd
from math import *




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
        data_recieved = request.data.decode('utf-8')
        
        print(data_recieved)
        print(type(data_recieved))
        final_dictionary = eval(data_recieved)
        
        print(final_dictionary)
        print(type(final_dictionary))
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug = True)
