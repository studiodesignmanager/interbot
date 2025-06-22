import time
from datetime import datetime, timedelta
from bot import get_online_girl, post_to_telegram

def job():
    girl = get_online_girl()
    if girl:
        post_to_telegram(girl)
    else:
        print("Нет подходящих анкет онлайн.")

def main():
    # Ждём 5 минут для тестового поста после запуска
    time.sleep(300)
    print(f"{datetime.now()}: Запускаем тестовый пост")
    job()

    # Основной цикл: пост в 20:00 по Москве (UTC+3)
    while True:
        now = datetime.utcnow() + timedelta(hours=3)  # московское время
        if now.hour == 20 and now.minute == 0:
            print(f"{now}: Запускаем основной пост")
            job()
            time.sleep(60)  # чтобы не запустилось несколько раз за минуту
        time.sleep(20)

if __name__ == "__main__":
    main()
