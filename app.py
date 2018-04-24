from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,\
                            ImageSendMessage, TemplateSendMessage, ButtonsTemplate,\
                            MessageTemplateAction)
import os

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('6ZldQ8v/2TGnZnzzPRLw6N/UIggRBS90jwXHmwuL+1rdV9fAotZ6SkJrCivb7v3v7hAxvFP/37qeFPomFDceKMzOGBk \
                           BbzrkcK0bO173AfqE/4b/3qWw2iF+hlMyWwIZjNLKcHPT6iADzZNLiGQQTAdB04t89/1O/w1cDnyilFU=')
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
    text = event.message.text.lower()

    if 'education' in text or 'study' in text or 'studies' in text:
        bachelor_content = 'I got the bachelor\'s degree of Information Management from National Taiwan University \
                            in June 2017.'
        mba_content = 'And I\'m now in the first year of the MBA degree of Information Management from National \
                       Taiwan University. My research focuses on the resource allocation problem of 5G network.'
        content = '{}\n{}'.format(bachelor_content, mba_content)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))

        return 0

    if 'contact' in text or 'communicat' in text:
        content = 'Contact me by:\nEmail: astrumstella048@gmail.com\nPhone: +886 975669869'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'research' in text or '5G' in text or 'network' in text:
        research_content = 'not done yet'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=research_content))
        return 0

    # if 'intern' in text:
    #     intern_content = 'I was an intern engineer in Gliacloud.'
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=intern_content))
    #
    #     glia_content = 'Gliacloud is a startup developing AI video creation platform. You could find more \
    #                     information on their website: https://www.gliacloud.com/'
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=glia_content))
    #
    #     glia_work = 'I developed and maintained UI for their video creation platform and the QC system. \
    #                  I also did test automation. Moreover, I sometimes provided sales related support \
    #                  such as business model analysis.'
    #
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=glia_work))

        # glia_buttons_template = TemplateSendMessage(
        #     alt_text='Do you want to see some pictures?',
        #     template=ButtonsTemplate(
        #         title='Do you want to see some pictures?',
        #         text='Choose Yes or No.',
        #         # thumbnail_image_url='https://i.imgur.com/kzi5kKy.jpg',
        #         actions=[
        #             MessageTemplateAction(
        #                 label='Yes',
        #                 text='Yes, show me some pictures.'
        #             ),
        #             MessageTemplateAction(
        #                 label='No',
        #                 text='No, thanks.'
        #             )
        #         ]
        #     )
        # )
        # line_bot_api.reply_message(event.reply_token, glia_buttons_template)

    #     return 0
    #
    # # if 'Yes, show me some pictures.' in text:
    #
    # if event.message.text == 'Wow! Show me your software development projects.':
    #     content = 'project'
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text=content))
    #     return 0
    #
    # if event.message.text == 'Did you join clubs or activities at school?':
    #     content = 'activities'
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text=content))
    #     return 0

    message = TemplateSendMessage(
        alt_text='Choose a movie to watch.',
        template=ButtonsTemplate(
            thumbnail_image_url='https://example.com/image.jpg',
            title='Choose a movie to watch.',
            text='Please select.',
            actions=[
                MessageTemplateAction(
                    label='The Study Diaries',
                    text='Let\'s see your educational background.'
                ),
                MessageTemplateAction(
                    label='The Intern',
                    text='Hey, talk more about your last internship.'
                ),
                MessageTemplateAction(
                    label='Project Hunting',
                    text='Wow! Show me projects you\'ve made.'
                ),
                MessageTemplateAction(
                    label='College Musical',
                    text='Did you join clubs or activities at school?'
                ),
                MessageTemplateAction(
                    label='Way of the Motto',
                    text='Share your motto with me.'
                ),
                MessageTemplateAction(
                    label='Contact',
                    text='How can I contact you?'
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
