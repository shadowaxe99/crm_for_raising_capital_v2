import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.info('Hello, World! route was accessed')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)