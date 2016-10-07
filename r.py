import telepot
import time

welcomeMsg = 'Welcome! I am your friend for today(forever:P).'
lyrics = 'lyrics'
songs = 'song'
helpMsg = 'To get started, type "Song " and enter the name of the song and the bot will fetch you a youtube video link. To get lyrics, just type "Lyrics Artist name Song name"'
def handle(msg):
	print(msg)
	chat_id = msg['from']['id']
	command = msg['text']
	if command == '/start':
		bot.sendMessage(chat_id,welcomeMsg)
		return 
	if command == '/help':
		bot.sendMessage(chat_id,helpMsg)
		return 
	if lyrics.lower() in command.lower():
		bot.sendMessage(chat_id,'Hello,your lyrics are on there way!')
		first_word = command.split()[0]
		second_word = command.split()[1]
		third_word = command.split()[2]
		base_url = 'http://www.azlyrics.com/lyrics/'
		bot.sendMessage(chat_id,base_url+second_word+'/'+third_word+'.html')
		return
	if songs.lower() in command.lower():
		song_url = 'https://www.youtube.com/results?search_query='
		yolo = command.split()
		url = ''
		for word in yolo[1:]:
			url = url + word + '+'
		
		final_url = song_url + url
		bot.sendMessage(chat_id,final_url)		
		return 
		
bot = telepot.Bot('Your Token Here')
bot.message_loop(handle)
print 'listening'

while 1:
	time.sleep(10)
	
