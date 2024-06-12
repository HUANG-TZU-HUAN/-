from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    clinics = get_clinics(user_message)

    if clinics:
        reply = "\n".join([f"{clinic['name']}\n地址: {clinic['address']}\n电话: {clinic['phone']}\n地圖: https://your-deployed-map-link" for clinic in clinics])
    else:
        reply = "找不到符合条件的诊所。"

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

def get_clinics(query):
    clinic_data = [
        {"name": "宜蘭診所A", "address": "宜蘭市某街道1號", "phone": "123-456-789"},
        {"name": "宜蘭診所B", "address": "宜蘭市某街道2號", "phone": "123-456-789"}
    ]
    matching_clinics = [clinic for clinic in clinic_data if query in clinic['name']]
    return matching_clinics

if __name__ == "__main__":
    app.run(port=8000)
