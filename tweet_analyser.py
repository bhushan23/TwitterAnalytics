import json
import pandas as pd
import matplotlib.pyplot as plt
import re
from textblob import TextBlob
import unicodedata
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets_data_path="./data/twitter_data.txt"
tweets_data=[]
tweets_file=open(tweets_data_path,'r')

for line in tweets_file:
	try:
		tweet=json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

print len(tweets_data)
tweets=pd.DataFrame()
tweets['text']=map(lambda tweet:tweet['text'],tweets_data)
tweets['lang']=map(lambda tweet:tweet['lang'],tweets_data)
tweets['country']=map(lambda tweet:tweet['place']['country'] if tweet['place']!=None else None, tweets_data)
#print tweets['text'][1]

for i in tweets['text']:
	print i
	tb = TextBlob(unicodedata.normalize('NFKD', i).encode('ascii','ignore'))
	print(tb.sentiment)
