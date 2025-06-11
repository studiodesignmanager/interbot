import schedule
import time
import subprocess

def job():
    subprocess.run(["python3", "bot.py"])

schedule.every().day.at("20:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(30)