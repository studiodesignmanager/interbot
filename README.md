# Interbot

Авто-постинг анкет девушек с сайта FindBride в Telegram-канал.

## Как использовать

1. Установи зависимости:

```
pip install -r requirements.txt
```

2. Заполни `config.py` (токен и канал).
3. Запусти:

```
python bot.py         # Тестовый пост
python scheduler.py   # Автопостинг каждый день в 20:00 МСК
```

> Бот должен быть админом в Telegram-канале.