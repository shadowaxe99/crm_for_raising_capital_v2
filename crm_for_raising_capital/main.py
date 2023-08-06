import logging

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

if __name__ == '__main__':
    app.run(debug=True, port=5001)