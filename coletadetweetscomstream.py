import tweepy
from datetime import datetime

now = datetime.now().strftime('%Y%m%d%H%M%S')
log_file = open('manifestacao-20161204-coletaem-%s.log' % now,'w')
tweets_file = open('manifestacao-20161204-coletaem-%s.json' % now,'w')

class MyStreamListener(tweepy.StreamListener):

	def on_connect(self):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write("%s [CONNECTED]" % now)

	def on_error(self, status_code):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [ERROR] %s' % (now,status_code))

	def on_status(self, status):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [STATUS] %s' % (now,status))

	def on_exception(self, exception):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [EXCEPTION] %s' % (now,exception))

	def on_delete(self, status_id, user_id):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [DELETED] StatusId=%s UserId=%s' % (now,status_id,user_id))

	def on_event(self, status):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [EVENT] %s' % (now,status))

	def on_direct_message(self, status):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [DIRECT_MESSAGE] %s' % (now,status))

	def on_friends(self, friends):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [FRENDS] %s' % (now,friends))

	def on_limit(self, track):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [LIMIT] %s' % (now,track))

	def on_timeout(self):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [TIMEOUT]' % now)

    #  https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
	def on_disconnect(self,notice):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [DISCONNECT] %s' % (now,notice))

	def on_warning(self,notice):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [WARNING] %s' % (now,notice))

	def on_data(self, data):
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		log_file.write('%s [DATA]' % (now))
		tweets_file.write(data)

consumer_key="suachave"
consumer_secret="suachave"
access_token="suachave"
access_token_secret="suachave"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# criterio = ["#VetaTemer","#ForaRenan","#VaiTerTroco","#AnistiaCaixa2Nao","#4DezVemPraRua","#4DezembroVemPraRua","#10MedidasContraCorrupcao","#SubstitutivoNao"]
# criterio = ["#4DezVemPraRua"]
criterio = ["#VemPraRuaBrasil","#MarchaDosPatinhosPamonhas","Esplanada","#antagonistasnasruas","Moro e Janot","#protesto"]



# Definindo a via pela qual trafegam os tweets
stream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())

# Declarando os tweets do meu interesse
log_file.write("Iniciando coleta de %s\n" % criterio)
stream.filter(track=criterio)