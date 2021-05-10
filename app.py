from flask import Flask, request, abort



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
        data_recieved = request.get_json(force = True)
        print(type(data_recieved))
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
