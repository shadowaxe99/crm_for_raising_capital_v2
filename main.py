import schedule
import time

# existing code...

def schedule_email(time, email):
    schedule.every().day.at(time).do(send_email, email)

# existing code...

if __name__ == '__main__':
    # existing code...
    schedule_email('09:00', 'investor@example.com')
    while True:
        schedule.run_pending()
        time.sleep(1)