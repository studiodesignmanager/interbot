import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from telegram import Bot
from config import TOKEN, CHANNEL, HEADERS
from parser import get_online_girl
from image_utils import crop_logo

def post_to_telegram(profile):
    bot = Bot(token=TOKEN)
    response = requests.get(profile['img'])
    img = crop_logo(response.content)

    caption = (
        f"👩‍💼 {profile['name']}, {profile['age']}, {profile['country']}\n"
        f"🔗 [Смотреть анкету]({profile['link']})"
    )

    bot.send_photo(
        chat_id=CHANNEL,
        photo=img,
        caption=caption,
        parse_mode='Markdown'
    )

if __name__ == "__main__":
    girl = get_online_girl()
    if girl:
        post_to_telegram(girl)
    else:
        print("Нет подходящих анкет онлайн.")