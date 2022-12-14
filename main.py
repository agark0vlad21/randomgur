#! /usr/bin/python3

from random import sample
from string import digits, ascii_letters
from requests import get, post
from time import sleep as wait

TOKEN = "" # token of your bot
CHAT_ID = "" # chat id for send photos, like @telegram, or -1825122896521
METHOD = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

if TOKEN.strip() == "" or CHAT_ID.strip() == "":
    print(" 'TOKEN' and 'CHAT_ID' variables must be not empty")
    exit(1)
else:
    print("trying to check posting, please wait")
    if not post(METHOD, data={ "chat_id": CHAT_ID,
                              "photo": "http://http.cat/200",
                              "caption": "test photo"  }).ok:
        print("looks like you configure randomgur incorrect, please check 'CHAT_ID' and 'TOKEN' variables\nNOTE: you need to issue the rights of the administrator of the bot if the posts go to the channel")
        exit(2)
def try_send_with(length):
    try:
        image_id = ''.join(sample(ascii_letters + digits, length))
        if get(f"https://i.imgur.com/{image_id}.jpg", allow_redirects=False).status_code != 200:
            print("\u001b[31murl is not valid\u001b[0m")
        else:
            print(f"\u001b[32mgot valid url, sending image\u001b[0m ({image_id})")
            post(METHOD, data={ "chat_id": CHAT_ID, "photo": f"https://i.imgur.com/{image_id}.jpg" })
            wait(1)
    except (EOFError, KeyboardInterrupt):
            print ("\u001b[2D\u001b[36mBye!\u001b[0m")
            exit(0)
    except Exception:
            print ("\u001b[31;1merror has been occured when downloading or checking image\u001b[0m")
            wait(1)
while True:
    try_send_with(5)
