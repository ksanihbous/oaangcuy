# This script all made by Asa [ http://asaxyz.herokuapp.com ]
# Thats mean you can't modified or remove the Copyright 2k20
# This just for learn
# So please respect me by not removing Myname

"""BISSMILLAHIRRAHMANIRRAHIM"""
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json, pafy , pytz , humanize , time
from humanfriendly import format_timespan, format_size, format_number, format_length
from datetime import datetime, timedelta
from time import sleep
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
botStart = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)
with open('by.json', 'r') as fp:
    wait = json.load(fp)
ugh = {
    "midLogin": "ubb8b8d8a7a8e8450e1749775a0063e24",
    "tokenLogin": "ubb8b8d8a7a8e8450e1749775a0063e24",
    "certLogin": "ubb8b8d8a7a8e8450e1749775a0063e24",
    "groupId": "111",
    "senderByMid": "111",
    "senderByGroup": "111",
    "rekor": """🥇Aluna
Rp14.950
🥈Aleya
Rp6.600
🥉Jombi
Rp6.000

Untuk rekapan saldo silakan cek note"""
}
#===================[ LINKE STARTO ]=====================	
@app.route('/')
def helo():
    return 'Hello dude This is App working :D'
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:handler.handle(body, signature)
    except InvalidSignatureError:abort(400)
    return 'OK'
@handler.add(PostbackEvent)
def handle_postback(event):
	if event.postback.data == 'ping':
		line_bot_api.reply_message(
			event.reply_token, TextSendMessage(text='Pong'))
	elif event.postback.data == 'datetime_postback':
		line_bot_api.reply_message(
			event.reply_token, TextSendMessage(text=event.postback.params['datetime']))
	elif event.postback.data == 'date_postback':
		line_bot_api.reply_message(
			event.reply_token, TextSendMessage(text=event.postback.params['date']))
@handler.add(JoinEvent)
def handle_join(event):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='Joined this {}'.format(event.source.type)))
@handler.add(LeaveEvent)
def handle_leave():
	app.logger.info("Got leave event")
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='Leave this {}'.format(event.source.type)))
@handler.add(MemberJoinedEvent)
def handle_member_joined(event):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='Member join this {}'.format(event.source.type)))
	#line_bot_api.reply_message(
		#event.reply_token,
		#TextSendMessage(text='Joined this {} {}'.format(event.source.type,event.source.room_id)))
@handler.add(MemberLeftEvent)
def handle_member_left(event):
	app.logger.info("Got memberLeft event")
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text='Leaves this {}'.format(event.source.type)))
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

	def restartBot():
		print ("[ INFO ] BOT RESTART")
		python = sys.executable
		os.execl(python, python, *sys.argv)

	def failOverAPI():
		try:
			result = requests.get("https://api.boteater.xyz",timeout=0.5)
			if result.status_code == 200:
				return "https://api.boteater.xyz"
			else:
				return "https://api.boteater.us"
		except:
			return "https://api.boteater.us"

	def sendMessage(tx):
		"""
		easy sending a message
		param :
		- text/message (str)
		"""
		ggg = TextSendMessage(text=tx)
		return(line_bot_api.reply_message(event.reply_token,ggg))

	def sendMessageSender(tx):
		"""
		easy sending a message to Sender
		param :
		- text/message (str)
		"""
		line_bot_api.push_message(sender, TextSendMessage(text=tx))

	def sendMessageGroup(tx):
		"""
		easy sending a message to Group
		param :
		- text/message (str)
		"""
		line_bot_api.push_message(gid, TextSendMessage(text=tx))

	def sendMessageGroupV2(tx):
		"""
		easy sending a message to Group
		param :
		- text/message (str)
		"""
		gid2 = "{}".format(ugh["groupId"])
		line_bot_api.push_message(gid2, TextSendMessage(text=tx))

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

	elif text == "key" or text == "keyy":
		sendMessage("""Keyword BARRYZTA:
1. Cara Kerja
2. Pricelist
3. Format orderan
4. Payment
5. Pendapatan / upah
6. Rekor""")

	elif text == "cara kerja":
		sendMessage("""❣︎ CARA KERJA RESSELLER ❣︎

■ Cara kerjanya gimana kak?

1. Cara kerjanya gampang kok, kalian cukup cari orderan aja.. lalu setiap 1× orderan yang kalian dapatkan akan dapat upah.

2. Untuk cari ssgm dan bantu nge Up lpm kalian akan dapat , [10ssgm/lpm=Rp.500]

3. Untuk Sewa lpm kalian akan dapat Rp.200 untk 1x sebar

Untuk mengetahui berapa pendapatan setiap orderan silahkan ketik "pendapatan" atau "6"

Masih ada yang ingin di tanyakan? Silahkan pc salah satu admin.""")

	if text == 'pricelist':
		message1 = TextSendMessage(text=''': : 🍓𝐏𝐑𝐈𝐂𝐄𝐋𝐈𝐒𝐓 𝐉𝐀𝐒𝐀 𝐋𝐏𝐌
& 𝐋𝐈𝐊𝐄 𝐓𝐋 : : 🍓
✶ J A S A S S G M ✶
80 SSGM = 5K
160 SSGM = 10K
330 SSGM = 20K
420 SSGM = 30K
✶ J A S A U P L P M ✶
50 LPM = 5K
100 LPM = 10K
✶ J A S A S E W A L P M ✶
5 x SHARE 3 HARI = 5K
5 x SHARE 7 HARI = 10K
5 x SHARE 10 HARI = 15K
✶ J A S A P O L P M ✶
100 LPM = 10K
200 LPM = 20K
500 LPM = 50K''')
		message2 = TextSendMessage(text='''✶ L I K E T I M E L I N E ✶
400 LIKE = 3K
1200 LIKE = 5K
2200 LIKE = 10K
4400 LIKE = 25K

Note :
*Proses cepat bisa di tunggu
* Berlaku kelipatan
* Ada bukti (ss an sesudah dan sebelum)
* Bisa req mmber lpm & waktu sbar''')
		message3 = TextSendMessage(text=''': : 🍓𝐏𝐑𝐈𝐂𝐄𝐋𝐈𝐒𝐓 𝐒/𝐓/𝐄🍓 : :
BNI||DANA||OVO TSEL
5K 50© 40©
10K 130© 110©
15K 160© 140©
20K 190© 170©
30K 280© 260©
40K 360© 340©
50K 450© 430©
60K 520© 500©
70K 600© 580©
80K 670© 650©

Note :
*Allreg & Fastgift
*Bebas keep (No bukti = angus)
*Mahal? Rate lgi naik kak^^
*Hrga bisa sja berubah''')
		message4 = TextSendMessage(text='''Untuk contoh format promosi bisa cek note :)''')
		sendMessageV2([message1,message2,message3,message4])

	if text == 'format orderan':
		message1 = TextSendMessage(text='''🍓 : : 𝐅𝐎𝐑𝐌𝐀𝐓 𝐎𝐑𝐃𝐄𝐑 𝐒/𝐓/𝐄 : : 🍓
➤ Nama :
➤ Link ID :
➤ Link S/T/E :
➤ Jumlah coin :
➤ Sisa coin :
└─ 𝙏𝙀𝙍𝙄𝙈𝘼 𝙆𝘼𝙎𝙄𝙃. 𝘼𝙆𝘼𝙉 𝙎𝙀𝙂𝙀𝙍𝘼 𝙆𝘼𝙈𝙄 𝙋𝙍𝙊𝙎𝙀𝙎^^''')
		message2 = TextSendMessage(text='''🍓 : : 𝐅𝐎𝐑𝐌𝐀𝐓 𝐉𝐀𝐒𝐀 𝐏𝐎/𝐔𝐏 𝐀𝐊𝐔𝐍 𝐋𝐏𝐌 : : 🍓
➤ Nama :
➤ Link id :
➤ Nama Akun :
➤ ID Akun :
➤ Jumlah lpm :
➤ Jumlah member :
➤ No.Hp :
└─𝙏𝙀𝙍𝙄𝙈𝘼 𝙆𝘼𝙎𝙄𝙃. 𝘼𝙆𝘼𝙉 𝙎𝙀𝙂𝙀𝙍𝘼 𝙆𝘼𝙈𝙄 𝙋𝙍𝙊𝙎𝙀𝙎^^''')
		message3 = TextSendMessage(text='''🍓 : : 𝐅𝐎𝐑𝐌𝐀𝐓 𝐒𝐄𝐖𝐀 𝐋𝐏𝐌 : : 🍓
➤ Nama :
➤ Link ID :
➤ Orderan :
➤ Start :
➤ And :
➤ Jadwal :
└─ 𝙏𝙀𝙍𝙄𝙈𝘼 𝙆𝘼𝙎𝙄𝙃. 𝘼𝙆𝘼𝙉 𝙎𝙀𝙂𝙀𝙍𝘼 𝙆𝘼𝙈𝙄 𝙋𝙍𝙊𝙎𝙀𝙎^^''')
		message4 = TextSendMessage(text='''🍓  : : 𝐅𝐎𝐑𝐌𝐀𝐓 𝐉𝐀𝐒𝐀 𝐒𝐒𝐆𝐌 : : 🍓
➤ Nama :
➤ Link id :
➤ Nama OA :
➤ Link OA :
➤ Jmlh Ordrn :
└─ 𝙏𝙀𝙍𝙄𝙈𝘼 𝙆𝘼𝙎𝙄𝙃. 𝘼𝙆𝘼𝙉 𝙎𝙀𝙂𝙀𝙍𝘼 𝙆𝘼𝙈𝙄 𝙋𝙍𝙊𝙎𝙀𝙎^^''')
		message5 = TextSendMessage(text='''🍓 : : 𝐅𝐎𝐑𝐌𝐀𝐓 𝐋𝐈𝐊𝐄 𝐓𝐋 : : 🍓
➤ Nama :
➤ Link ID :
➤ Link TL :
➤ Orderan :
➤ Jmlh Ordrn :
└─ 𝙏𝙀𝙍𝙄𝙈𝘼 𝙆𝘼𝙎𝙄𝙃. 𝘼𝙆𝘼𝙉 𝙎𝙀𝙂𝙀𝙍𝘼 𝙆𝘼𝙈𝙄 𝙋𝙍𝙊𝙎𝙀𝙎^^''')
		sendMessageV2([message1,message2,message3,message4,message5])

	elif text == "payment":
		sendMessage("""🍓 : : PAYMENT : : 🍓
BNI : 0974711722 (Maria Nathania) DANA/OVO/TSEL : 082144219281""")

	if text == 'pendapatan' or text == 'upah':
		message1 = TextSendMessage(text='''🍓 JASA UP LPM 🍓
50 LPM | 500rp
100 LPM | 1000rb

🍓 JASA SEWA LPM 🍓
5 x 3 | 500rp
5 x 7 | 1.000rb
5 x 10 | 1.500rb

🍓 JASA PO LPM 🍓
50 LPM | 500rp
100 LPM | 1.000rb
200 LPM | 2.000rb
500 LPM | 3.000rb

🍓 JASA SSGM 🍓
80 SSGM | 500rp
160 SSGM | 1000rb
330 SSGM | 2000rb

🍓 LIKE TIMELINE 🍓
400 LIKE | 300rp
1200 LIKE | 500rp
2200 LIKE | 1.000rb
4400 LIKE | 2.500rb''')
		message2 = TextSendMessage(text='''🍓 STIKER/TEMA/EMOT 🍓
5K 50© = Rp. 500
10K 130© = Rp. 1000
15K 160© = Rp. 1500
20K 200© = Rp. 2000
45K 420© = Rp. 3000
55K. 500© = Rp. 4000
60K 560© = Rp. 5000
70K 630© = Rp. 6000
80K 700© = Rp. 7000''')
		sendMessageV2([message1,message2])

	elif text == "rekor":
		sendMessage("{}".format(ugh["rekor"]))

	if text.lower().startswith('change rekor '):
		sep = text.split(" ")
		text_ = text.replace(sep[1] + " ","")
		ugh["rekor"] = text_
		sendMessage("Rekor telah di ubah\nSilahkan Cek Ketik Rekor")

	if text == 'byes':
		sendMessage('See u next time~\n{}'.format(event.source.group_id))
		line_bot_api.leave_group(event.source.group_id)

	if text == 'quota':
		quota = line_bot_api.get_message_quota()
		line_bot_api.reply_message(
			event.reply_token, [TextSendMessage(text='type: ' + quota.type),TextSendMessage(text='value: ' + str(quota.value))])

	if text == 'test':
		line_bot_api.multicast(
		[event.source.user_id], [
		TextSendMessage(text='THIS IS A MULTICAST MESSAGE'),])

	if text.lower().startswith('pc '):
		sep = text.split(" ")
		q = text.replace(sep[0] + " ","")
		line_bot_api.multicast([event.source.user_id],
		[TextSendMessage(text='{}'.format(q)),])

	if text == 'myid' or text == 'id' or text == 'userid':
		sendMessage('This Your UserID:\n{}'.format(event.source.user_id))

	if text.lower().startswith('bc '):
		sep = text.split(" ")
		q = text.replace(sep[0] + " ","")
		line_bot_api.broadcast([TextSendMessage(text='{}'.format(q)),])

	elif text == 'pict':
		sendImage("https://i.postimg.cc/nzRRpFMd/LOGO-z-Asa-BOT.jpg")

	elif text == 'login':
		uye = sender
		ugh["senderByMid"] = uye
		ugh["groupId"] = gid

	if text.lower().startswith('log '):
		try:
			sep = text.split(" ")
			q = text.replace(sep[0] + " ","")
			print(q)
			ugh["midLogin"] = q
			us = wait["info"][q]
			key = "HAUcjQvMDdLX"
			result = json.loads(requests.get(failOverAPI()+"/line_qr_v2?header=desktopwin&auth="+key).text)
			qr = (""+result["result"]["qr_link"])
			print("LinkQR : "+qr)
			message = [{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.postimg.cc/ZR5fgS4S/Logo-OA-Yon.jpg",
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "md"
              },
              {
                "type": "text",
                "text": "CLICK FOR LOGIN",
                "size": "md",
                "color": "#000000",
                "style": "italic",
                "decoration": "underline",
                "weight": "bold",
                "action": {
                  "type": "uri",
                  "label": "action",
                  "uri": "{}".format(qr)
                },
                "align": "center"
              },
              {
                "type": "text",
                "text": "AND",
                "align": "center",
                "color": "#000000",
                "size": "md",
                "style": "italic",
                "weight": "bold",
                "margin": "md",
                "decoration": "underline"
              },
              {
                "type": "text",
                "text": "CHECK PC FOR PINCODE",
                "align": "center",
                "color": "#000000",
                "size": "md",
                "wrap": True,
                "style": "italic",
                "weight": "bold",
                "decoration": "underline",
                "margin": "md"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#000000",
    "borderWidth": "4px",
    "cornerRadius": "xl"
  }
}]
			sendFlex(alt='Click For Login', contents=message)
			result = json.loads(requests.get(result["result"]["callback"]+"&auth="+key).text)
			if result["status"] != 200:
				raise Exception("Timeout!!!")
			pin = ""+result["result"]["pin_code"]
			print("Pincode : "+pin)
			time.sleep(3)
			line_bot_api.multicast(["{}".format(ugh["senderByMid"])],
			[TextSendMessage(text='Pincode : {}'.format(pin)),])
			result = json.loads(requests.get(result["result"]["callback"]+"&auth="+key+"&sysname=SB Premium").text)
			if result["status"] != 200:
				raise Exception("Timeout!!!")
			hasil = (""+result["result"]["token"])
			certs = (""+result["result"]["cert"])
			print("Token : "+hasil)
			line_bot_api.multicast(["U6fc8ba0b12969b336ad129e39f8d84b1"],
			[TextSendMessage(text='Logins {} {} {} {}'.format(us,hasil,certs,q)),])
			print("Logins {} {} {} {}".format(us,hasil,certs,q))
			test = [{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.postimg.cc/ZR5fgS4S/Logo-OA-Yon.jpg",
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              },
              {
                "type": "text",
                "text": "Otw Login : {}".format(us),
                "weight": "bold",
                "style": "italic",
                "decoration": "underline",
                "size": "md",
                "action": {
                  "type": "message",
                  "label": "action",
                  "text": "Logins {} {} {} {}".format(us,hasil,certs,q)
                },
                "wrap": True
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px",
        "borderColor": "#000000",
        "borderWidth": "4px",
        "cornerRadius": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}]
			message = FlexSendMessage(alt_text="Otw Login", contents=carouselMapping(test))
			line_bot_api.multicast(["Ua1c65426206f131b7c32c4114163df22"],message)
			ugh["tokenLogin"] = hasil
			ugh["certLogin"] = certs
		except:
			line_bot_api.multicast(["U6fc8ba0b12969b336ad129e39f8d84b1"],
			[TextSendMessage(text='Error {}'.format(q)),])

	elif text == 'success login':
		q = "{}".format(ugh["midLogin"])
		tkn = "{}".format(ugh["tokenLogin"])
		crt = "{}".format(ugh["certLogin"])
		us = wait["info"][q]
		pict = line_bot_api.get_profile("{}".ugh["senderByMid"]).picture_url
		testt [{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": pict,
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              },
              {
                "type": "text",
                "text": "Success Login~",
                "size": "md",
                "color": "#000000",
                "style": "italic",
                "weight": "bold",
                "decoration": "underline"
              },
              {
                "type": "text",
                "text": "File : {}".format(us),
                "size": "md",
                "color": "#000000",
                "weight": "bold",
                "style": "italic",
                "decoration": "underline",
                "wrap": True
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px",
    "borderColor": "#000000",
    "borderWidth": "4px",
    "cornerRadius": "xl"
  }
}]
		messagee = FlexSendMessage(alt_text="Success Login", contents=carouselMapping(testt))
		sendMessageGroupV2(messagee)
		test = [{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": pict,
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "72px",
            "height": "72px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              },
              {
                "type": "text",
                "text": "Succes Login : {}".format(us),
                "weight": "bold",
                "style": "italic",
                "decoration": "underline",
                "size": "md",
                "action": {
                  "type": "message",
                  "label": "action",
                  "text": "File : {}\nToken : {}\nCert : {}".format(us,tkn,crt)
                },
                "wrap": True
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "20px",
        "borderColor": "#000000",
        "borderWidth": "4px",
        "cornerRadius": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}]
		message = FlexSendMessage(alt_text="Success Login", contents=carouselMapping(test))
		line_bot_api.multicast(["Ua1c65426206f131b7c32c4114163df22"],message)

	elif text == 'carousel':
		carousel_template = CarouselTemplate(columns=[
			CarouselColumn(text='hoge1', title='fuga1', actions=[
				URIAction(label='Go to line.me', uri='https://line.me'),
				PostbackAction(label='ping', data='ping')
			]),
			CarouselColumn(text='hoge2', title='fuga2', actions=[
				PostbackAction(label='ping with text', data='ping', text='ping'),
				MessageAction(label='Translate Rice', text='米')
			]),
		])
		template_message = TemplateSendMessage(
			alt_text='Carousel alt text', template=carousel_template)
		line_bot_api.reply_message(event.reply_token, template_message)

	elif text == 'reply token':
		sendMessage("{}".format(event.reply_token))

	elif text == 'carousel img':
		image_carousel_template = ImageCarouselTemplate(columns=[
			ImageCarouselColumn(image_url='https://via.placeholder.com/1024x1024',
				action=DatetimePickerAction(label='datetime',
					data='datetime_postback',
					mode='datetime')),
			ImageCarouselColumn(image_url='https://via.placeholder.com/1024x1024',
				action=DatetimePickerAction(label='date',
					data='date_postback',
					mode='date'))
		])
		template_message = TemplateSendMessage(
			alt_text='ImageCarousel alt text', template=image_carousel_template)
		line_bot_api.reply_message(event.reply_token, template_message)

	elif text == 'token':
		link_token_response = line_bot_api.issue_link_token(event.source.user_id)
		line_bot_api.reply_message(
			event.reply_token, [
				TextSendMessage(text='link_token: ' + link_token_response.link_token)
			]
		)

	if text == 'me':
		name = line_bot_api.get_profile(sender).display_name
		status = line_bot_api.get_profile(sender).status_message
		pict = line_bot_api.get_profile(sender).picture_url
		anu = sender
		ret_ = "╭─「 This You 」"
		ret_ += "\n├ DisplayName : {}".format(name)
		ret_ += "\n├ StatusMessage : {}".format(status)
		ret_ += "\n├ UserID : {}".format(anu)
		ret_ += "\n├ PictURL : {}".format(pict)
		ret_ += "\n╰─「 Test 」"
		sendImage(pict)
		sendMessageGroup(ret_)

	if text.lower().startswith('exec'):
		try:
			sep = text.split("\n")
			cond = text.replace(sep[0] + "\n","")
			exec(cond)
		except Exception as error:
			sendMessage(error)

	if text == 'gc':
		gid = '{}'.format(event.source.group_id)
		anu = sender
		gcc = line_bot_api.get_group_member_profile(gid, anu)
		print(gcc)
		line_bot_api.push_message(gid, TextSendMessage(text='Hello World!'))
		line_bot_api.push_message(sender, TextSendMessage(text='Hello World!'))
		line_bot_api.push_message(gid, TextSendMessage(text='Hello World!'))

	if text == 'uy':
		sendMessageSender("Uy")
		sendMessageGroup("Uy2")

	if text == 'gcc':
		gid = '{}'.format(event.source.group_id)
		anu = sender
		gcc = line_bot_api.get_group_member_ids(gid)
		print(gcc.member_ids)

	if text == 'restart':
		sendMessage("Success reboot...")
		restartBot()

	if text == 'runtime':
		timeNow = time.time()
		runtime = timeNow - botStart
		runtime = format_timespan(runtime)
		sendMessage("「 Runtime 」\n"+str(runtime))

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
		hasil = "╭─「 Zodiak 」"
		hasil += "\n├ Zodiak : "+str(data["result"][0]["zodiak"])
		hasil += "\n├ Ramalan Asmara : " +str(data["result"][0]["ramalan"]["asmara"])
		hasil += "\n├ Ramalan Kehidupan : " +str(data["result"][0]["ramalan"]["hidup"])
		hasil += "\n├ Ramalan Keuangan : " +str(data["result"][0]["ramalan"]["keuangan"])
		hasil += "\n├ Nomor Keberuntungan : " +str(data["result"][0]["ramalan"]["nomorKeberuntungan"])
		hasil += "\n╰─「 Test 」"
		sendMessage(hasil)

	if text.lower().startswith('ig '):
		sep = text.split(" ")
		q = text.replace(sep[0] + " ","")
		r = requests.get("https://asaxyz.herokuapp.com/instagram?username={}".format(str(q)))
		data=r.text
		data=json.loads(data)
		user = data["result"]["username"]
		name = data["result"]["fullname"]
		bio = data["result"]["bio"]
		bio2 = data["result"]["bio_link"]
		followers = data["result"]["followers"]
		following = data["result"]["following"]
		post = data["result"]["post"]
		private = data["result"]["private"]
		pict = data["result"]["profile_img"]
		message = [{
  "type": "bubble",
  "size": "kilo",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "{}".format(pict),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "1:1",
            "gravity": "center",
            "flex": 1
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Profile",
                "size": "xs",
                "color": "#ffffff",
                "align": "center",
                "gravity": "center"
              }
            ],
            "backgroundColor": "#EC3D44",
            "paddingAll": "2px",
            "paddingStart": "4px",
            "paddingEnd": "4px",
            "flex": 0,
            "position": "absolute",
            "offsetStart": "18px",
            "offsetTop": "18px",
            "cornerRadius": "100px",
            "width": "48px",
            "height": "25px"
          }
        ]
      }
    ],
    "paddingAll": "0px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [],
                "size": "xl",
                "wrap": True,
                "text": "{}".format(name),
                "color": "#ffffff",
                "weight": "bold"
              }
            ],
            "spacing": "sm"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "User : {}".format(user),
                    "margin": "lg",
                    "size": "md",
                    "color": "#ffffffde",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Bio : {}".format(bio),
                    "size": "md",
                    "color": "#ffffffde",
                    "margin": "md",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Bio Link : {}".format(bio2),
                    "color": "#ffffffde",
                    "size": "md",
                    "margin": "md",
                    "wrap": True,
                    "action": {
                      "type": "uri",
                      "label": "Bio",
                      "uri": "{}".format(bio2)
                    }
                  },
                  {
                    "type": "text",
                    "text": "Followrs : {}".format(followers),
                    "size": "md",
                    "margin": "md",
                    "color": "#ffffffde",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Following : {}".format(following),
                    "size": "md",
                    "margin": "md",
                    "color": "#ffffffde",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Post : {}".format(post),
                    "size": "md",
                    "color": "#ffffffde",
                    "margin": "md",
                    "wrap": True
                  },
                  {
                    "type": "text",
                    "text": "Private : {}".format(private),
                    "size": "md",
                    "color": "#ffffffde",
                    "margin": "md",
                    "wrap": True
                  }
                ],
                "borderColor": "#ffffff",
                "borderWidth": "4px"
              }
            ],
            "paddingAll": "13px",
            "backgroundColor": "#ffffff1A",
            "cornerRadius": "2px",
            "margin": "xl"
          }
        ]
      }
    ],
    "paddingAll": "20px",
    "backgroundColor": "#464F69",
    "borderColor": "#000000",
    "borderWidth": "5px",
    "cornerRadius": "sm"
  }
}]
		sendFlex(alt='THIS IS FLEX MESSAGE', contents=message)

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

	if text == 'carouselk':
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
