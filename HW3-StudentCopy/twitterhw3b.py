# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.


# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")


import tweepy
import tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from textblob import textblob

consumer_key = 'no1y4zMxXrpmKNaSeBWWP1BFy'
consumer_secret = 'R8smVQlWwUFEPZzNWtPlznTskYKXjYP4dvO4aV7whYTpRbSqXo'
access_token = '341297169-tprPKGkydTIn7cA2vKu91ik7PO7Cd15HA9keQ9mR'
access_secret = 'S4gOGuWqypNQhGkCQgPBLeNbbCyYYocu1KiDRQTX8JpfC'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

search_term = input('Input a term: ')
for tweets in tweepy.Cursor(api.search, q=search_term, result_type='recent', include_entities=True, lang='en', count=100).items(100): 
	print (tweets.text)

analysis = TextBlob(tweets.text)
print (analysis.sentiment)
sub = analysis.sentiment.subjectivity
pol = analysis.sentiment.polarity

print ('The average subjectivity is:', sub)
print ('The average polarity is', pol)




print("Average subjectivity is")
print("Average polarity is")
