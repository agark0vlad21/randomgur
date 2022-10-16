import random, string, requests, urllib, os

def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    variable = f"https://i.imgur.com/{rand_string}.jpg"
    #print(variable)
    response = requests.get(variable)
    if response.history:
        print("url is not valid")
    else:
        print("valid url, downloading image")
        urllib.request.urlretrieve(variable,rand_string)
        # if you want to send image as file, change sendasimage to sendasfile.sh
        os.system(f'sleep 1 && mv {rand_string} {rand_string}.jpg && bash sendasimage.sh {rand_string}.jpg > /dev/null')
while True:
    generate_alphanum_random_string(5)
