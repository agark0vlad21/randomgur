token = "" # token of your bot
url = "https://api.telegram.org/bot"
channel_id = "" # username or id of channel
url += token
method = url + "/sendPhoto"


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    link = f"https://i.imgur.com/{rand_string}.jpg"
    #print(link)
    response = requests.get(link)
    if response.history:
        print("url is not valid")
    else:
        print("valid url, downloading image")
        requests.post(method, data={ "chat_id": channel_id, "photo": link })
        time.sleep(1)
while True:
    generate_alphanum_random_string(5)
