import schedule
import time

# existing code...

def schedule_email(time, email):
    schedule.every().day.at(time).do(send_email, email)

# existing code...

if __name__ == '__main__':
    # existing code...
    time = input('Enter the time to schedule emails (24 hour format): ')
    email = input('Enter the email to send: ')
    schedule_email(time, email)
    while True:
        schedule.run_pending()
        time.sleep(1)

    print('Emails have been scheduled successfully!')
    print('This is a new print statement to confirm the update.')