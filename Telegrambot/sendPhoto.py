#!/usr/bin/python3
import requests
import time

url1 = "https://api.telegram.org/bot"
url2 = "6169941166:AAEIEvAHAwYog2RbM17gxRayy-5EaxcgI0M"
mainUrl = "{}{}/sendPhoto".format(url1, url2)
photos = ["https://www.shutterstock.com/image-photo/smiling-woman-carrying-excited-son-600w-2224840803.jpg", "https://images.unsplash.com/photo-1682685797406-97f364419b4a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80"]
for photo in photos:
    time.sleep(10)
    para = {
        "chat_id" : "-892311724",
        "photo" : photo
    }   
    req = requests.get(mainUrl, data = para)
    reqs = req.json()
    print(reqs)
