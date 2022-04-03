import requests

_headers = {
  'accept-language': 'en-US,en;q=0.9',
  'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
  'x-requested-with': 'XMLHttpRequest'
}

main_url = "https://t.me/AHADx1337/3"
session = requests.session()
session.headers.update(_headers)
main_res = session.get(main_url).text
print(main_res)
