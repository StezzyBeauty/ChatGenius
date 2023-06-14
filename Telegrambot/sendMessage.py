#!/usr/bin/python3
import requests

url1 = "https://api.telegram.org/bot"
url2 = ""
mainUrl = "{}{}/sendMessage".format(url1, url2)
#res = requests.get(mainUrl)
#resp = res.json()
#print(resp)
para = {
        "chat_id" : "-892311724",
        "text" : "Hello"
}
req = requests.get(mainUrl, data = para)
reqs = req.json()
print(reqs)
