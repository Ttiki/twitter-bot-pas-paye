import os
import tweepy
from datetime import datetime, date
import schedule  
from keep_alive import keep_alive

#Twitter Keys & Token
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

#Twitter init
#Auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#Create api object
api = tweepy.API(auth)

def newTweet():
  #Create a tweet (only if date of today > today_date date)
  #date & time
  d1 = date(2020, 11, 11)
  print(d1)
  d2 = datetime.now().date()
  print(d2)
  result = d2 - d1
  print(result.days)

  api.update_status("Jour n°%s depuis la fin du contrat sans être payé." % (result.days))
  print("Jour n°%s depuis la fin du contrat sans être payé." % (result.days))

# run the function job() every 30 minutes  
schedule.every(1).days.do(newTweet)  

while True:  
  schedule.run_pending()  

keep_alive()