import flask
from flask import request
import logging

app = flask.Flask(__name__)
logging.basicConfig(filename='request.log', level=logging.INFO)

@app.before_request
def log_request_info():
    logging.info('Headers: %s', request.headers)
    logging.info('Body: %s', request.get_data())

@app.route('/', methods=['GET'])
def home():
    ip = request.remote_addr
    logging.info(f'IP: {ip}')
    return {'message': 'Hello, World!'}

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return {'message': 'Missing username or password'}, 400
    if len(data['username']) < 5 or len(data['password']) < 8:
        return {'message': 'Username must be at least 8 characters'}, 400
    return {'message': 'Valid input'}

if __name__ == '__main__':
    app.run(debug=True)