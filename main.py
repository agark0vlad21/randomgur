#! /usr/bin/python3

from random import sample
from string import digits, ascii_letters
from requests import get, post
from time import sleep as wait

TOKEN = "" # token of your bot
CHAT_ID = "" # chat id to send photos, like @telegram, or -1825122896521
METHOD = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

if TOKEN.strip() == "":
    print("'TOKEN' must be not empty, please fill this field")
    exit(2)
elif CHAT_ID.strip() == "":
    print("'CHAT_ID' must be not empty, please fill this field")
    exit(3)

def try_send_with(length):
    try:
        letters_and_digits = ascii_letters + digits
        image_id = ''.join(sample(letters_and_digits, length))
        if get(f"https://i.imgur.com/{image_id}.jpg").history:
            print("\u001b[31murl is not valid\u001b[0m")
        else:
            print("\u001b[32mgot valid url, sending image\u001b[0m")
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
