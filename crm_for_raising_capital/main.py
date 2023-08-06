import logging
from flask import Flask
from datetime import datetime

logging.basicConfig(filename='app.log', level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.info('Hello, World! route was accessed')
    return 'Hello, World!'

@app.route('/error')
def error_route():
    try:
        raise Exception('An error occurred!')
    except Exception as e:
        logging.error(str(e))
        return 'An error occurred, check the logs!'

@app.route('/time')
def server_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return 'Current server time is: ' + current_time

if __name__ == '__main__':
    app.run(debug=True, port=5001)