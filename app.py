from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,\
                            ImageSendMessage, TemplateSendMessage, ButtonsTemplate,\
                            MessageTemplateAction)
import os

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('6ZldQ8v/2TGnZnzzPRLw6N/UIggRBS90jwXHmwuL+1rdV9fAotZ6SkJrCivb7v3v7hAxvFP/37qeFPomFDceKMzOGBkBbzrkcK0bO173AfqE/4b/3qWw2iF+hlMyWwIZjNLKcHPT6iADzZNLiGQQTAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b0428cbb30597d2668de5b08d62d68d7')
# User ID
user_id = 'U97cbe7589f49376ffa8a40727b4bf0e2'


# listen all post requests from /callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == 'Let\'s see your educational background.':
        content = 'education'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

    if event.message.text == 'Hey, talk more about your work experience.':
        content = 'gliacloud'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

    if event.message.text == 'Wow! Show me your software development projects.':
        content = 'project'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

    if event.message.text == 'Did you join clubs or activities at school?':
        content = 'activities'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

    buttons_template = TemplateSendMessage(
        alt_text='Are you ready?',
        template=ButtonsTemplate(
            title='Are you ready?',
            text='Choose Yes or No.',
            thumbnail_image_url='https://i.imgur.com/kzi5kKy.jpg',
            actions=[
                MessageTemplateAction(
                    label='Yes',
                    text='Yes'
                ),
                MessageTemplateAction(
                    label='No',
                    text='No'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
