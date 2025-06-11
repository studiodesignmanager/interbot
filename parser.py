import requests
from bs4 import BeautifulSoup
from config import HEADERS

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