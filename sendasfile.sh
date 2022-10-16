#! /bin/bash
# sending image as file
BotToken = "" # enter bot token into " "
chatid = "" # enter the id of the chat you want to send a message to

# sending image
curl -F document=@"$PWD/$1" https://api.telegram.org/bot"$BotToken"/sendDocument?chat_id=$chatid

# removing image
rm $1
