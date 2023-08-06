from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def home():
    client_ip = request.remote_addr
    app.logger.info('Client IP: %s', client_ip)
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)