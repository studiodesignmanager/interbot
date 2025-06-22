import requests
from telegram import Bot
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from config import TOKEN, CHANNEL, HEADERS

def get_online_girl():
    url = "https://findbride.com/members?age%5Bfrom%5D=25&age%5Bto%5D=40"
    resp = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')
    profiles = soup.select(".member-item")
    for profile in profiles:
        if 'online' not in profile.get('class', []):
            continue
        name = profile.select_one('.member-name')
        age = profile.select_one('.member-age')
        country = profile.select_one('.member-country')
        link_tag = profile.select_one("a")
        img_tag = profile.select_one("img")
        if name and age and country and link_tag and img_tag:
            return {
                "name": name.text.strip(),
                "age": age.text.strip(),
                "country": country.text.strip(),
                "link": "https://findbride.com" + link_tag['href'],
                "img": img_tag['src']
            }
    return None

def crop_logo(img_data):
    img = Image.open(BytesIO(img_data))
    width, height = img.size
    cropped = img.crop((0, 40, width, height))  # срез сверху 40 пикселей
    output = BytesIO()
    output.name = 'photo.jpg'
    cropped.save(output, format='JPEG')
    output.seek(0)
    return output

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
