from flask import Flask, request, abort,jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello Deployemnt Working"


@app.route('/hit')
def hit():
    return "Hello Tradingview Hit"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("*****************************************************")
        print(jsonify(request.data))
        print("*****************************************************")
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
