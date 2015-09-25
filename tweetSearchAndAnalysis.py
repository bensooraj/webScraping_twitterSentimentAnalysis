import tweepy

############################## ** Note ** ####################
# The following two imports need not be performed.          ##
# I am just letting them stay :D                            ##
from tweepy import Stream                                   ##
from tweepy.streaming import StreamListener                 ##
##############################################################

from tweepy import OAuthHandler
import codecs
from string import punctuation

class tweetSearchAndAnalysis():

    # The consumer key, consumer secret, access token and access secret should
	# be obtained from the Twitter UI when registering an application
	ckey = '9XKyjq769fZ883HfB8KbWT7AN'
    csecret = 'sLXPcbkMEE90EfeaQMw7w89mg8O0yap5QXqryueQ7xw5pUG0St'
	
    atoken = '393538660-CpHqO86niQJVBCdPgDYd7uKtF1ubDogIlSZ3DtQo'
    asecret = '3VfgebGM7IAdLqsz5Hm1hKD5pCN5KrJlocSco8lmBx0DP'
	
    # OAuth Authentication
	auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    # Twitter API wrapper
	api = tweepy.API(auth)
	
    # Load the list of positive and negative words
	# These will be used for analysing the tweets
	pos_sent = open("positive_words.txt").read()
    positive_words = pos_sent.split('\n')
    	
    neg_sent = open('negative_words.txt').read()
    negative_words = neg_sent.split('\n')
    	
    # tweetSearch() searches for 100 tweets containing the "Celebrity name"
	# and saves them to "testTweets.txt" for sentiment analysis at
	# tweetSentimentAnalysis
	def tweetSearch(self, celebrityName):

        outFile = codecs.open("testTweets.txt", 'w', "utf-8")
        results = self.api.search(q=celebrityName, lang="en", locale="en", count=100)
	
        for result in results:
            outFile.write(result.text + '\n')
            
        outFile.close()
	
    # This is the core of the analysis logic
	# I've kept it really simple, i.e., count the total number
	# of positive and negative words cumulated across all the
	# tweets stored in "testTweets.txt" and decide the sentiment.
	def posNegCount(self, tweet):

        pos = 0
        neg = 0

        for p in list(punctuation):
            tweet = tweet.replace(p, '')

        tweet = tweet.lower() #.encode('utf8')
        words = tweet.split(' ')
        word_count = len(words)

        for word in words:
            if word in self.positive_words:
                pos = pos + 1
            elif word in self.negative_words:
                neg = neg + 1

        return pos, neg
	
    # 
	def tweetSentimentAnalysis(self):

        # Read all the tweets from "testTweets.txt" and 
		# split + store them to tweets_list
		tweets = codecs.open("testTweets.txt", 'r', "utf-8").read()
        tweets_list = tweets.split('\n')
        #tweets.close()           - AttributeError: 'str' object has no attribute 'close'

        positive_counter = 0
        negative_counter = 0

        # Call posNegCount() on each tweet stored in tweets_list and
		# increment positive_counter and negative_counter accordingly
		for tweet in tweets_list:
            if(len(tweet)):
                p, n = self.posNegCount(tweet)
                positive_counter += p
                negative_counter += n
                
        #print("positive_counter:", positive_counter, "negative_counter:", negative_counter)

        # Hopefully, this is self-explanatory
		if positive_counter > negative_counter:
            return "POSITIVE"

        elif positive_counter < negative_counter:
            return "NEGATIVE"

        else:
            return "NEUTRAL"



