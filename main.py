#!/usr/bin/python

import sys
from datetime import date
from rauth import OAuth1Session, oauth
from FitbitAuth import *
from TwitterAuth import *

def getYTDFloors():
  base_url = "https://api.fitbit.com"
  request_token_url = base_url + "/oauth/request_token"
  access_token_url = base_url + "/oauth/access_token"
  authorize_url = "http://www.fitbit.com/oauth/authorize"
  api_version = "/1"

  session = OAuth1Session(fitbit_consumer_key(),
                          fitbit_consumer_secret(),
			  fitbit_oauth_token(),
			  fitbit_oauth_secret())

  jan_first_date = str(date.today().year) + "-01-01"
  url = base_url + api_version + "/user/-/activities/floors/date/"+jan_first_date+"/today.json"
  r = session.get(url, params={}, header_auth=True)

  # add values for each day
  total = 0
  d = r.json()["activities-floors"]
  for day in d:
    total += int(day['value'])
  print "total: ", total
  return total

def postTweet(messageBody):
  base_url = "https://api.twitter.com"
  api_version = "/1.1"

  session = OAuth1Session(twitter_consumer_key(),
                          twitter_consumer_secret(),
			  twitter_oauth_token(),
			  twitter_oauth_secret())
			
  url = base_url + api_version + "/statuses/update.json"
  params = {'status' : messageBody}

  r = session.post(url, data=params, header_auth=True)
  print r.json()

#acquireFitbitTokens()
num = getYTDFloors()
tweet_text = 'Floors climbed year-to-date: ' + str(num)# + ' #fitbit #fitstats'
postTweet(tweet_text)
