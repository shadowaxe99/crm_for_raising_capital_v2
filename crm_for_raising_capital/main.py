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

@app.route('/new')
def new_route():
    logging.info('New route was accessed')
    return 'This is a new route!'

@app.route('/trump')
def trump_route():
    logging.info('Trump route was accessed')
    return 'This is the best route, everybody says so!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)