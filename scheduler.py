import schedule
import time
import subprocess

def job():
    print("Запуск задачи поста в телеграм...")
    subprocess.run(["python3", "/root/interbot/bot.py"])

def main():
    job()  # запуск сразу при старте для проверки
    schedule.every().day.at("20:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()
