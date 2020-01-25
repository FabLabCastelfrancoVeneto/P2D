import paho.mqtt.client as mqtt
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

current_topic = ""

#array per creazione keyboards
array_reply = ["Lamp", "Garage Doors","Demo"]

array_inline = [
    "Turn on", "Turn off", " ",
    "Open Indoor", "Open Outdoor", " ",
    "Turn Right", "Turn Left", " "]

keyboard_reply = []
keyboard_inline = []

#keyboard creation
def create_reply_kbd():
    global keyboard_reply
    keyboard_reply = []
    keyboard_reply = [array_reply[i:i+3] for i in range(0,len(array_reply),3)]
    #print keyboard_reply

def create_inline_kbd(node_name):
    global keyboard_inline
    keyboard_inline = []
	subarray_inline = []
    index = array_reply.index(node_name)*3
	#subarray_inline = array_inline[index:index+3] #all 3 elements even if empty
	for i in range(index, index+3):
		if (array_inline[i] != " "):
			#print array_inline[i]
			subarray_inline.append(array_inline[i])
	keyboard_inline = [[InlineKeyboardButton(s, callback_data=s) for s in subarray_inline]]
	#print keyboard_inline


#mqtt
#subscribe to topic "node_update"
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("node_alive")

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

#publish to node
def send_mqtt_msg(topic, msg):
    print "Publishing %s on %s" % (topic.replace(" ", "_"), msg.replace(" ", "_"))
    client.publish(topic.replace(" ", "_"), msg.replace(" ", "_"));
	client.loop()

def on_disconnect(client, userdata, rc):
    if rc != 0:
    	print("Unexpected disconnection.")
	client.reconnect()

#telegram
def hello(bot, update):
	update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))

def start(bot, update):
	#chiamata a db per recuperare i valori e inserirli in array_reply e array_inline
	create_reply_kbd()
	reply_markup = ReplyKeyboardMarkup(keyboard_reply, resize_keyboard=True)
	update.message.reply_text('Please choose:', reply_markup=reply_markup)

def incoming_text(bot, update):
	text = update.message.text
	global current_topic
	current_topic = text
	#print text
	send_mqtt_msg(current_topic, "abc") #chiamata mqtt per risvegliare il nodo ( se addormentato)
	send_mqtt_msg(current_topic, "def") #2^
	if text in array_reply:
		create_inline_kbd(text)
		reply_markup_custom = InlineKeyboardMarkup(keyboard_inline)
		update.message.reply_text('Scegli cosa vuoi gestire di %s' % text, reply_markup=reply_markup_custom) #ITA
		#update.message.reply_text('What dow you want to do with %s' % text, reply_markup=reply_markup_custom) #ENG

def button(bot, update):
	query = update.callback_query
	bot_msg = "Per %s hai scelto %s" % (current_topic, query.data) #ITA
	#bot_msg = "You chose to %s %s" % (current_topic, query.data) #ENG
	print bot_msg
	send_mqtt_msg(current_topic, query.data) #chiamata mqtt
	bot.editMessageText(text=bot_msg, chat_id=query.message.chat_id, message_id=query.message.message_id)


#mqtt connection
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1", 1883, 60)
client.on_disconnect = on_disconnect

#telegram connection
updater = Updater('your_telegram_bot_token')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.text, incoming_text))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()
