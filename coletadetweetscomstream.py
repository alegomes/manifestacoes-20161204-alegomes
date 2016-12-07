import tweepy
from datetime import datetime

now = datetime.now().strftime('%Y%m%d%H%M%S')
log_file = open('manifestacao-20161204-coletaem-%s.log' % now,'w')
tweets_file = open('manifestacao-20161204-coletaem-%s.json' % now,'w')

class MyStreamListener(tweepy.StreamListener):

	def on_connect(self):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write("%s [CONNECTED]\n" % now)
		log_file.flush()

	def on_error(self, status_code):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [ERROR] %s\n' % (now,status_code))
		log_file.flush()

		if status_code == 401:
			msg = "Bla"
		else:
			msg = "%d" % status_code


	def on_status(self, status):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [STATUS] %s\n' % (now,status))
		log_file.flush()

	def on_exception(self, exception):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [EXCEPTION] %s do tipo %s\n' % (now,exception,type(exception)))
		log_file.flush()

		# HTTPSConnectionPool(host='stream.twitter.com', port=443): Read timed out.
		# ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response',))

		# if exception == requests.exceptions.ConnectionError:
			# pensar no que fazer

	def on_delete(self, status_id, user_id):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [DELETED] StatusId=%s UserId=%s\n' % (now,status_id,user_id))
		log_file.flush()

	def on_event(self, status):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [EVENT] %s\n' % (now,status))
		log_file.flush()

	def on_direct_message(self, status):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [DIRECT_MESSAGE] %s\n' % (now,status))
		log_file.flush()

	def on_friends(self, friends):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [FRENDS] %s\n' % (now,friends))
		log_file.flush()

	def on_limit(self, track):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [LIMIT] %s\n' % (now,track))
		log_file.flush()

	def on_timeout(self):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [TIMEOUT]\n' % now)
		log_file.flush()

    #  https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
	def on_disconnect(self,notice):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [DISCONNECT] %s\n' % (now,notice))
		log_file.flush()

	def on_warning(self,notice):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [WARNING] %s\n' % (now,notice))
		log_file.flush()

	def on_data(self, data):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [DATA]\n' % (now))
		tweets_file.write(data)
		log_file.flush()

# consumer_key="suachave"
# consumer_secret="suachave"
# access_token="suachave"
# access_token_secret="suachave"

consumer_key="T00TCHCTXTmCdh6vVsqU84D9i"
consumer_secret="ZJHKVWaCQAatlzJATluk0K6EdHCNkLyniPztYRug9zCCgvOGVL"
access_token="14147108-5msuw61fHHCmzkIDPJBbVtwkv3TPd3jQiaRbp5QeW"
access_token_secret="MZ72wvleYUCQeWDnudF2fEhanjGREP51msTYAF9vpbNKa"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# criterio = ["#VetaTemer","#ForaRenan","#VaiTerTroco","#AnistiaCaixa2Nao","#4DezVemPraRua","#4DezembroVemPraRua","#10MedidasContraCorrupcao","#SubstitutivoNao"]
# criterio = ["#4DezVemPraRua"]
criterio = ["#VemPraRuaBrasil","#MarchaDosPatinhosPamonhas","Esplanada","#antagonistasnasruas","Moro e Janot","#protesto"]



# Definindo a via pela qual trafegam os tweets
stream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())

# Declarando os tweets do meu interesse
msg = "%s Iniciando coleta de %s" % (now,criterio)
log_file.write(msg+"\n")
print(msg)
stream.filter(track=criterio)