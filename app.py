from flask import Flask, request
import requests
import os

app = Flask(__name__)


VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    if message == "help" or message == "ajuda":
        message = "add SUA_MATRICULA --> Se cadastra no bot\n"
        message +="get SUA_MATRICULA --> \n"
        message += "alert NAO_SEI AINDA"
    else:
        message = "NUM TENDI OQUE FALO"
    reply(sender, message)

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
