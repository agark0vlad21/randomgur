#!/bin/bash
# sends image as image
BotToken="" # enter bot token into " "
chatid="" # enter the id of the chat you want to send a message to

# sending image
curl -s -X POST "https://api.telegram.org/bot"$BotToken"/sendPhoto" -F chat_id="$chatid" -F photo="@$PWD/$1"

# removing image
rm $1

