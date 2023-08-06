import os
import csv
import openai
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = os.path.join('uploads', file.filename)
            file.save(filename)
            return redirect(url_for('send_emails', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/send_emails')
def send_emails():
    filename = request.args.get('filename')
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            name, email = row
            message = f"Dear {name},\n\nI am writing to you to raise capital..."
            print(f"Sending email to {name} at {email}...")
            print(message)
    return 'Emails sent!'

if __name__ == '__main__':
    app.run(debug=True)