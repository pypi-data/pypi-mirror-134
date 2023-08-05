"""
This __init__.py file allows Python to read your package files
and compile them as a package. It is standard practice to leave 
this empty if your package's modules and subpackages do not share
any code.
(If your package is just a module, then you can put that code here.)
"""
import requests
import json
from bs4 import BeautifulSoup

def check(name):
  name = name.strip()
  if len(name) < 3:
    return "error"
  try:
    name = int(name)
    return "error"
  except:
    url = "https://www.tiktok.com/@" + name
    resp = requests.get(url).text
    soup = BeautifulSoup(resp, 'html.parser')
    res = soup.find('script', type = 'application/ld+json')
    try:
      json_object = json.loads(res.contents[0])
      user = json_object['itemListElement'][1]["item"]["name"]
      if not user.startswith("undefined"):
        return "taken"
    except:
      try:
        headers={
            "authority": "m.tiktok.com",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
            "method": "GET",
            "scheme": "https",
            "accept": "application/json, text/plain, */*",
            "accept-encoding": 'gzip, deflate, utf-8',
            "accept-language": "en-US,en;q=0.9",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1"
            }
        priv = requests.get("https://www.tiktok.com/api/user/detail/?aid=1988&uniqueId=" + name, headers=headers).json()
        check = priv["userInfo"]["user"]["privateAccount"]
        if check == True:
          return "taken"
        else:
          return "error"
      except:
        return "available"