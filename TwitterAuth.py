def twitter_consumer_key():
  f = open('twitter_consumer_key', 'r')
  k = f.read()
  return k.rstrip('\n')

def twitter_consumer_secret():
  f = open('twitter_consumer_secret', 'r')
  k = f.read()
  return k.rstrip('\n')

def twitter_oauth_token():
  f = open('twitter_oauth_token', 'r')
  k = f.read()
  return k.rstrip('\n')

def twitter_oauth_secret():
  f = open('twitter_oauth_secret', 'r')
  k = f.read()
  return k.rstrip('\n')
