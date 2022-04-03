import requests

session = requests.session()
a = session.get("https://t.me/AHADx1337/3?embed=1").text
print(a)
