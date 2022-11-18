import random
import string
from requests import get, post
from time import sleep as wait

TOKEN = "" # token of your bot
URL = "https://api.telegram.org/bot"
CHAT_ID = "" # username or id of chat
URL += TOKEN
METHOD = URL + "/sendPhoto"

def try_send(length):
    try:
        letters_and_digits = string.ascii_letters + string.digits
        rand_string = ''.join(random.sample(letters_and_digits, length))
        link = f"https://i.imgur.com/{rand_string}.jpg"
        response = get(link)
        if response.history:
            print("\u001b[31murl is not valid\u001b[0m")
        else:
            print("\u001b[32mgot valid url, sending image\u001b[0m")
            post(METHOD, data={ "chat_id": CHAT_ID, "photo": link })
            wait(1)
    except (EOFError, KeyboardInterrupt):
            print ("\n\u001b[36mBye!\u001b[0m")
            exit(0)
    except Exception:
            print ("\u001b[31;1merror has been occured when downloading or checking image\u001b[0m")
            wait(1)
while True:
    try_send(5)
