from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='request.log', level=logging.INFO)

@app.before_request
def log_request_info():
    app.logger.info('Headers: %s', request.headers)
    app.logger.info('Body: %s', request.get_data())

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)