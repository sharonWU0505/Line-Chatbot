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
        bac_content = 'I got the bachelor\'s degree of Information Management from National Taiwan University \
                       in June 2017.'
        mba_content = 'And I\'m now in the first year of the MBA degree of Information Management from National \
                       Taiwan University.'
        res_content = 'My research focuses on the resource allocation problem of 5G network.'
        content = 'This is a film about my education.\nHere\'s the introduction:\n\n{}\n\n{}\n\n{}'.format(
            bac_content, mba_content, res_content)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'research' in text or '5G' in text or 'network' in text:
        res_content = '5G network is known for its centralized structure, which makes it more flexible to meet \
                       heterogeneous demand. However, the way to allocate resource remains a problem.'
        objectives = 'So I aim to design suitable allocation scheme for different scenarios.'
        link = 'Know more about 5G network: https://en.wikipedia.org/wiki/5G'
        content = '{}\n\n{}\n\n{}'.format(res_content, objectives, link)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'intern' in text or 'internship' in text:
        # buttons_template = TemplateSendMessage(
        #     alt_text='Internship in Gliacloud',
        #     template=ButtonsTemplate(
        #         thumbnail_image_url='https://i.imgur.com/tdG3kwI.png',
        #         title='Internship in Gliacloud',
        #         text='I was an intern enginner in Gliacloud.\nSelect topics to know more.',
        #         actions=[
        #             MessageTemplateAction(
        #                 label='Gliacloud',
        #                 text='Tell me more about Gliacloud.'
        #             ),
        #             MessageTemplateAction(
        #                 label='Achievements',
        #                 text='Tell me your achievements.'
        #             ),
        #             MessageTemplateAction(
        #                 label='Reflection',
        #                 text='Tell me your reflection.'
        #             )
        #         ]
        #     )
        # )
        # line_bot_api.reply_message(event.reply_token, buttons_template)
        # return 0
        buttons_template = TemplateSendMessage(
            alt_text='template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qKkE2bj.jpg',
                actions=[
                    MessageTemplateAction(
                        label='test1',
                        text='test1'
                    ),
                    MessageTemplateAction(
                        label='test2',
                        text='test2'
                    ),
                    MessageTemplateAction(
                        label='test3',
                        text='test3'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

    if 'gliacloud' in text:
        content = 'Gliacloud is a startup developing AI video creation platform. You could find more \
        information on their website:\nhttps://www.gliacloud.com/'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'achievement' in text:
        content = '1. Developed and maintained UI of the AI Video Creation Platform and the official website.\n\
        2. Supported and maintained quality control system based on user feedback.\n\
        3. Wrote and executed unit tests and system tests for core products.\n\
        4. Provided sales related support, including demo video production and business model analysis.'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'reflection' in text:
        content = 'I\'m very happy and also thankful for having the chance to apply what I learned to the real world.'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    # if 'project' in text:
    #     message = TemplateSendMessage(
    #         alt_text='My Works',
    #         template=ButtonsTemplate(
    #             thumbnail_image_url='https://i.imgur.com/tdG3kwI.png',
    #             title='My Works',
    #             text='Yes, I have joined two projects. Select the one you would like to know.',
    #             actions=[
    #                 MessageTemplateAction(
    #                     label='UP YOUNG Maintenance Staff System',
    #                     text='UP YOUNG Maintenance Staff System'
    #                 ),
    #                 MessageTemplateAction(
    #                     label='Trisoap Sales System',
    #                     text='Trisoap Sales System'
    #                 )
    #             ]
    #         )
    #     )
    #     line_bot_api.reply_message(event.reply_token, message)
    #     return 0

    if 'up young' in text:
        content = 'UP YOUNG is a washing machine dealer with many customers. What we do is to \
        digitize and optimize the workflow of their maintenance staff who have to check whether \
        each washing machine works well.\n\
        We developed optimized algorithm for scheduling and traveling route, in order to suggest \
        best schedule for maintenance staff members.'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'trisoap' in text:
        content = 'Trisoap is a brand dedicated to sale soap made by mentally retarded children.\n\
        We collected their system demand by face-to-face interview and designed an appropriate system.\n\
        Finally, we developed the online purchasing system, including connecting with \
        third-party payment service and build admin interface for managers.'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    # if 'this might be something interesting in your school life' in text:
    #     message = TemplateSendMessage(
    #         alt_text='Extracurricular Activities',
    #         template=ButtonsTemplate(
    #             thumbnail_image_url='https://i.imgur.com/oSKlcJi.jpg',
    #             title='Extracurricular Activities',
    #             text='Select the one you would like to know.',
    #             actions=[
    #                 MessageTemplateAction(
    #                     label='Art Exhibition',
    #                     text='Art Exhibition'
    #                 ),
    #                 MessageTemplateAction(
    #                     label='Volunteer Clubs',
    #                     text='Volunteer Clubs'
    #                 )
    #             ]
    #         )
    #     )
    #     line_bot_api.reply_message(event.reply_token, message)
    #     return 0

    if 'art exhibition' in text:
        artfest_content = '[Tech Art Exhibition of 23th NTUArtFest]\n\
        I was the curator of the Tech Art Exhibition. I led a team to plan a contemporary dance \
        display that demonstrated a world controlled by digits and people couldn\'t follow their minds.'
        funpark_content = '[10th Very Fun Park]\n\
        I was a guide and an exhibition assistant of Very Fun Park held by Fubonart and National \
        Taiwan University. I introduced art works to visitors and helped artists to arrange \
        exhibition and dismantled displayed items.'
        content = '{}\n\n{}'.format(artfest_content, funpark_content)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'volunteer club' in text:
        content = 'I joined the volunteer club for autism children and the volunteer club for children with cancer. \
        I worked with people from different backgrounds to plan events like summer camp for those children \
        and their family, which make them relax and connect more with each other.'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    # if 'know more about you' in text:
    #     message = TemplateSendMessage(
    #         alt_text='To know more?',
    #         template=ButtonsTemplate(
    #             thumbnail_image_url='https://i.imgur.com/oSKlcJi.jpg',
    #             title='To know more?',
    #             text='Please select.',
    #             actions=[
    #                 MessageTemplateAction(
    #                     label='Motto',
    #                     text='Motto'
    #                 ),
    #                 MessageTemplateAction(
    #                     label='Second Languages',
    #                     text='Second Languages'
    #                 )
    #             ]
    #         )
    #     )
    #     line_bot_api.reply_message(event.reply_token, message)
    #     return 0

    if 'motto' in text:
        content = 'To see the world, things dangerous to come to,\n\
        to see behind walls, draw closer, \n\
        to find each other and to feel. \n\
        That is the purpose of life.\n\n\
        This is my favorite sentence. And I believe technology should have the ability \
        to help people achieve this goal.'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'second language' in text:
        content = 'English: fluent\nKorean: basic'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'korean' in text:
        content = '안녕하세요. 저는 오아선 이에요\n Hello, I am Wu Ya-Syuan.'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    if 'contact' in text or 'communicat' in text or 'phone' in text or 'email' in text:
        content = 'Contact me by:\nEmail: astrumstella048@gmail.com\nPhone: +886 975669869'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=content))
        return 0

    message = TemplateSendMessage(
        alt_text='Choose a movie to watch.',
        template=ButtonsTemplate(
            thumbnail_image_url='https://example.com/image.jpg',
            title='Choose a movie to watch.',
            text='Please select.',
            actions=[
                MessageTemplateAction(
                    label='The Study Diaries',
                    text='What is "The Study Diaries" about?'
                ),
                MessageTemplateAction(
                    label='The Intern',
                    text='I want to watch "The Intern".'
                ),
                MessageTemplateAction(
                    label='Project Hunting',
                    text='Is this about the projects you\'ve made?'
                ),
                MessageTemplateAction(
                    label='School Musical',
                    text='This might be something interesting in your school life.'
                ),
                MessageTemplateAction(
                    label='Is Not Enough',
                    text='Can I know more about you from this film?'
                ),
                MessageTemplateAction(
                    label='Contact',
                    text='Watch "Contact" to know how to contact.'
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
