#!/usr/bin/python3
import requests

url1 = "https://api.telegram.org/bot"
url2 = ""
mainUrl = "{}{}/getUpdates".format(url1, url2)
#res = requests.get(mainUrl)
#resp = res.json()
#print(resp)
para = {
        "offset" : "61753786",
        "limit" : "1"
}
req = requests.get(mainUrl, data = para)
reqs = req.json()
print(reqs)
