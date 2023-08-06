import schedule
import time
import os
from transformers import pipeline
import dotenv
from openai import Configuration, OpenAIApi

dotenv.load_dotenv()

# Creating an instance of OpenAIApi with API key from the environment variables
openai = OpenAIApi(
  Configuration(api_key=os.getenv('OPENAI_KEY'))
)


# Schedule email
schedule.every().day.at('09:00').do(send_email, 'example@example.com')

while True:
    schedule.run_pending()
    time.sleep(1)
