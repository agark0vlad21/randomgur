import random, string, requests, urllib
while True:
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
    generate_alphanum_random_string(5)
