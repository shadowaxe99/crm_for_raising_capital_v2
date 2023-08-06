import logging
import datetime
import re
import openai
from flask import Flask, request, render_template

app = Flask(__name__)


def read_csv_to_json(file):
    # TODO: Implement this function
    pass


def format_prompt(data):
    # TODO: Implement this function
    pass


def safeguard(result):
    # TODO: Implement this function
    pass


def send_email(to, cc, bcc, subject, body, send_date=None):
    # TODO: Implement this function
    pass


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        investors = read_csv_to_json(file)
        return render_template('send_emails.html', investors=investors)
    return render_template('index.html')


@app.route('/send_emails', methods=['POST'])
def send_emails():
    investors = request.form.getlist('investors')
    for investor in investors:
        print(f"Running - {investor['Name']}")
        prompt = format_prompt({
            "name": investor["Name"],
            "company_name": investor["Company Name"],
        })
        messages = [{"role": "system", "content": f"""{prompt}"""}]

        try:
            # Add the following lines to make the temperature and tokens adjustable
            temperature = float(input("Enter the temperature: "))
            max_tokens = int(input("Enter the maximum number of tokens: "))
            result = openai.engine("whisper").generate(
                prompt=messages,
                engine="davinci-002",
                temperature=temperature,
                max_tokens=max_tokens,
                use_whisper=True
            )
        except RateLimitError as e:
            logging.error(f"WARNING: RateLimitError occurred: {str(e)}")
            continue
        except Exception as e:
            logging.error(f"WARNING: Unknown error occurred: {str(e)}")
            continue

        if not safeguard(result):
            logging.warning(f"WARNING: Not sending the email to - {investor['Name']}")
            failed.append({investor['Name']: result})
            continue

        # Personalize the email
        result = result.replace("[NAME]", investor["Name"])
        result = result.replace("[COMPANY NAME]", investor["Company Name"])

        # Track the open rates and click-through rates
        investor["Opens"] = 0
        investor["Clicks"] = 0

        # Send the email
        send_email([investor['Email']], cc_list, bcc_list, email_subject, result)

        # Schedule a follow up email to be sent in 5 days
        follow_up_subject = "Re: " + email_subject
        follow_up_body = "Hi [NAME],\n\nI hope this email finds you well.\n\nI'm just following up on the email I sent you earlier. I'm still very interested in your company and I'm wondering if you had a chance to review my proposal.\n\nIf you have any questions, please don't hesitate to contact me.\n\nThanks,\n[YOUR NAME]"

        # Send the follow up email if the investor hasn't responded in 5 days
        if not investor["Responded"] and datetime.date.today() > investor["Last Email"]:
            send_email([investor['Email']], cc_list, bcc_list, follow_up_subject, follow_up_body, datetime.date.today() + datetime.timedelta(days=5))

        # Update the last email date
        investor["Last Email"] = datetime.date.today()

    logging.info("Finished sending emails")
    return 'Emails sent successfully'


if __name__ == '__main__':
    app.run(debug=True)