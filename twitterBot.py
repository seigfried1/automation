import tweepy
from tweepy import OAuthHandler
import requests
 
consumer_key = 'Secretkey'
consumer_secret = 'SecretPw'
access_token = 'SecretToken'
access_secret = 'SecretPw'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

# prints the user name on the console
user = api.me()
print(user.name)

# follow everyone who follows you
# for follower in tweepy.Cursor(api.followers).items():
# 	follower.follow()
# 	print("Followed everyone that followed " + user.name)

search = "Keyword to search"

numberofTweets = 100 # or any other number

# To retweet a tweet
# for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
# 	try:
# 		tweet.retweet()
# 		print('Retweeted the tweet')
# 	except tweepy.TweepError as e:
# 		print(e.reason)
# 	except StopIteration:
# 		break

# To favourite a tweet
for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
	try:
		tweet.favorite()
		print('Favourited the tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break







