import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token="2709506006-i2H04O9UYebZbU1NDivY5xfIVmem4qxUJ8w3wap"
access_token_secret="33Tdk61xv1jKADNkBIAXl1U6DbHwTKMuIxKk6wvIzPvJp"
consumer_key="s9580tDWREATQPU39PXH5Im3t"
consumer_key_secret="Xwm98mqxsQ2ZAes1oWBXIsXRQKAhOxm3RTGhzzSFcwxRtio6Ow"

class StdOutListener(StreamListener):
	def on_data(self, data):
		print data
		return True

	def on_error(self,error):
		print "error"


if __name__ == '__main__':
	l=StdOutListener()
	sys.stdout=open("./data/twitter_data.txt","w+")
	auth=OAuthHandler(consumer_key,consumer_key_secret)
	auth.set_access_token(access_token,access_token_secret)
	stream=Stream(auth,l)
	stream.filter(track=['modi'])