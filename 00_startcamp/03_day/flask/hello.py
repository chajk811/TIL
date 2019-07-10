from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '111111111111'

@app.route('/ssafy')
def ssafy():
    return 'This is ssafy!'
