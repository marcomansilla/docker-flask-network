import requests
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello from App2</h1>'


@app.route('/getdata')
def getdata():
    message = requests.get('http://app1:5000/senddata')
    return message.text


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001", debug=True)
