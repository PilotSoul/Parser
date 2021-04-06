import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()

user = fake_useragent.UserAgent().random

link = "http://www.wrk.ru/forums/login.php?action=in"

header = {
    'user-agent': user
}

data = {
    "form_sent": "1",
    "req_username": "attempt",
    "req_password": "3ID6SfBP"
}

response = session.post(link, data=data, headers=header).text

profile_info = "http://www.wrk.ru/forums/profile.php"
profile_responce = session.get(profile_info).text

cookies_dict = [
    {"domain": key.domain, "name": key.name, "path": key.path, "value": key.value}
    for key in session.cookies
]

session2 = requests.Session()

for cookies in cookies_dict:
    session2.cookies.set(**cookies)

resp = session2.get(profile_info, headers=header)
print(resp.text)