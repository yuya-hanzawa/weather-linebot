import os
import requests

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

lat = os.environ["LAT"]
lon = os.environ["LON"]
sign_up_token = os.environ["SIGN_UP_TOKEN"]
channel_access_token = os.environ["CHANNEL_ACCESS_TOKEN"]
reply_token = os.environ["REPLY_TOKEN"]


def Create_messages(lat, lon, sign_up_token):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly"

    params = {"lat":"35.6", "lon":"139.61", "lang":"ja", "hours":"15"}


    headers = {
        'x-rapidapi-key': sign_up_token,
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
        }

    try:
        response = requests.request("GET", url, headers=headers, params=params)
    
    except Exception as e:
        raise(e)

    cnt = 0
    message = ''
    
    for data in response.json()["data"]:
        if int(data["timestamp_local"][11:13])%3==0:

            text = data["timestamp_local"][11:16] + "時の降水確率は" + str(data["pop"]) + "%です。"

            if int(data["pop"]) == 0:
                text += "晴天です。"
            elif 0 < int(data["pop"]) <= 30:
                text += "雨が降る可能性は非常に低いです。"
            elif 30 < int(data["pop"]) <= 60:
                text += "雨が降るかもしれません。念のため折り畳み傘を持ち歩きましょう。"
            else:
                text += "雨が降りそうです。傘を持ち歩きましょう。"

            cnt += 1
            message += text

            if cnt == 5:
                break

            message += "\n\n"

    return message
    
def Send_messages(channel_access_token, reply_token, message):
    line_bot_api = LineBotApi(channel_access_token)

    try:
        line_bot_api.push_message(reply_token, TextSendMessage(text=message))

    except LineBotApiError as e:
        raise(e)

def main():
    message = Create_messages(lat, lon, sign_up_token)
    Send_messages(channel_access_token, reply_token, message)


if __name__ == '__main__':
   main()
