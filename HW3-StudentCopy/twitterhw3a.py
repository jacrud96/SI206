# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

#3 for twitter

import tweepy 

consumer_key = 'no1y4zMxXrpmKNaSeBWWP1BFy'
consumer_secret = 'R8smVQlWwUFEPZzNWtPlznTskYKXjYP4dvO4aV7whYTpRbSqXo'
access_token = '341297169-tprPKGkydTIn7cA2vKu91ik7PO7Cd15HA9keQ9mR'
access_secret = 'S4gOGuWqypNQhGkCQgPBLeNbbCyYYocu1KiDRQTX8JpfC'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

imag = 'mouse.png' 
txt = '#UMSI-206 #Proj3'



api.update_with_media(img,status=txt)

print ('No output')