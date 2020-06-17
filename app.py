# This script all made by ARSYBAI [ http://arsybai.xyz ]
# Thats mean you can't modified or remove the copyright
# This just for learn
# So please respect me by not removing myname

"""BISSMILLAHIRRAHMANIRRAHIM"""
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json, pafy
import errno
import os
from flex import flexTemplate
import sys, random, requests
import tempfile
import urllib, urllib3, urllib.parse, codecs
from urllib.parse import quote
from bs4 import BeautifulSoup
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)
app = Flask(__name__)
line_bot_api = LineBotApi('HMmDaqVkgYZEsDLe+2+wtabB9WculAkpCWv7Ly9tHg1+MXZX5vE7snMgPDusPJJnYV7ogj6/NVTQDLEmLpIndfGJ/jCb+TlLVjM43DBoIlpd+AwM261iNAtNIQJMRgRHZoei/aKBDhywT8/G4tG8QAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('01171fa476c3e523142a1338f5042b5a')
flex = flexTemplate()
#===================[ LINKE STARTO ]=====================	
@app.route('/')
def helo():
    return 'Hi there.. this is working :D'
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:handler.handle(body, signature)
    except InvalidSignatureError:abort(400)
    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	"""
	text message 
	"""
	text = event.message.text.lower()

	"""
	sender ID
	"""
	sender = event.source.user_id

	"""
	Group ID
	"""
	gid = event.source.sender_id
	
	"""
	BOT
	"""
	line = line_bot_api
#===============================================================================[ ARSYBAI FUNC ]
	def getProfile(sender):
		profile = line_bot_api.get_profile(sender).display_name
		"""
		argument:
		- display_name
		- status_message
		"""
		return profile

	def sendMessage(tx):
		"""
		easy sending a message
		param :
		- text/message (str)
		"""
		ggg = TextSendMessage(text=tx)
		return(line_bot_api.reply_message(event.reply_token,ggg))

	def sendAudio(audio):
		"""
		Sending a audio
		param :
		- audio URL (mp3/m4a)
		"""
		message = AudioSendMessage(original_content_url=audio,duration=240000)
		line_bot_api.reply_message(event.reply_token, message)

	def sendVideo(thumb, video):
		"""
		Sending a Video
		param :
		- Video URL (must url)
		- Thumbnail URL (image url)
		"""
		message = VideoSendMessage(original_content_url=thumb,preview_image_url=video)
		line_bot_api.reply_message(event.reply_token, message)

	def sendMessageV2(lst):
		"""
		Send Message more than one
		param :
		- Message List
		"""
		return(line_bot_api.reply_message(event.reply_token,lst))

	def carouselMapping(contents):
		"""
		DO NOT CHANGE THIS MADAFAKA!
		"""
		this = {"type": "carousel","contents": contents}
		return this

	def sendFlex(alt, contents):
		"""
		SEND A FLEX MESSAGE
		param :
		- list flex message (max 10)

		this will automatically send with carousel :3
		"""
		message = FlexSendMessage(alt_text="{}".format(str(alt)), contents=carouselMapping(contents))
		line.reply_message(event.reply_token,message)

	def sendImage(url):
		"""
		Sending a Image
		param :
		- Image URL (must url)
		"""
		message = ImageSendMessage(original_content_url='{}'.format(str(url)),preview_image_url='{}'.format(str(url)))
		line_bot_api.reply_message(event.reply_token, message)
		
	def quickItem(label, tx):
		qi = QuickReplyButton(action=MessageAction(label=label, text=tx))
		return qi
	def sendMessageWithQuickReply(tx,items):
		message = TextSendMessage(text=tx,quick_reply=QuickReply(items=items))
		line_bot_api.reply_message(event.reply_token, message)
#===============================================================================[ STARTO ]
	if text == 'quickReply':
		"""
		This is for send Text message with quick reply
		"""
		items = [quickItem('Hello','Hello')]
		sendMessageWithQuickReply('hi',items)
	
	if text == 'huy':
		"""
		this is example if u just want to send a text message
		"""
		sendMessage('Wayaaeee~')

	if text == 'quotes twitch':
		r = requests.get("https://api.haipbis.xyz/randomtwitchquotes")
		data = r.text
		data = json.loads(data)
		qts1 = "{}".format(data["quotes"])
		strm = "{}".format(data["streamer"])
		r2 = requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=in&text={}".format(qts1))
		data = r2.text
		data2 = json.loads(data)
		qts2 = "{}".format(data2["result"]["translated"])
		ret_ = "╭─「 Quotes Twitch 」"
		ret_ += "\n├ Quotes EN : {}".format(qts1)
		ret_ += "\n├ Quotes ID : {}".format(qts2)
		ret_ += "\n├ Streamer : {}".format(strm)
		ret_ += "\n╰─「 Test 」"
		sendMessage(ret_)

	if text.lower().startswith('zodiaks '):
		sep = text.split(" ")
		q = text.replace(sep[0] + " ","")
		r = requests.get("https://api.fckveza.com/zodiak?query={}&apikey=AsaTZZK".format(str(q)))
		data=r.text
		data=json.loads(data)
		hasil = "╭─「 Quotes Twitch 」"
		hasil += "\n├ Zodiak : "+str(data["result"][0]["zodiak"])
		hasil += "\n├ Ramalan Asmara : " +str(data["result"][0]["ramalan"]["asmara"])
		hasil += "\n├ Ramalan Kehidupan : " +str(data["result"][0]["ramalan"]["hidup"])
		hasil += "\n╰─「 Test 」"
		sendMessage(hasil)

	if text == 'heyy':
		"""
		this is example if you want to send more than one message
		"""
		message1 = TextSendMessage(text='Halo babang')
		message2 = TextSendMessage(text='Ngape lo?')
		#and more (Max 5)
		sendMessageV2([message1,message2])

	if text == 'flex':
		"""
		This is example for send a flex message
		( template in flex.py file )
		"""
		message = [flex.contoh()] #use []
		sendFlex(alt='THIS IS FLEX MESSAGE', contents=message)

	if text == 'carousel':
		"""
		This is example for send a flex message carousel
		( template in flex.py file )
		"""
		message = [flex.contoh(), flex.contoh(), flex.contoh(), flex.contoh(), flex.contoh()]
		#just add more template :3 (Max 10)
		sendFlex(alt='THIS IS CAROUSEL MESSAGE', content=message)

#===============================================================================[ END ]
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

"""ALHAMDULILLAH"""
