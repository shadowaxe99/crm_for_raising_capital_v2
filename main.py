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

const generateTextGPT35Turbo5Turbo = async (message) => {
  try {
    const response = await openai.createChatCompletion({
      model: 'gpt-3.5-turbo',
      messages: [this.context, message],
    });
    return response.data.choices[0].message.content;
  }
};


# Schedule email
schedule.every().day.at('09:00').do(send_email, 'example@example.com')

while True:
    schedule.run_pending()
    time.sleep(1)
