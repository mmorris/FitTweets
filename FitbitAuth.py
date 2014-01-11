from rauth import OAuth1Service, oauth

def fitbit_consumer_key():
  f = open('fitbit_consumer_key', 'r')
  k = f.read()
  return k.rstrip('\n')

def fitbit_consumer_secret():
  f = open('fitbit_consumer_secret', 'r')
  k = f.read()
  return k.rstrip('\n')

def fitbit_oauth_token():
  f = open('fitbit_oauth_token', 'r')
  k = f.read()
  return k.rstrip('\n')

def fitbit_oauth_secret():
  f = open('fitbit_oauth_secret', 'r')
  k = f.read()
  return k.rstrip('\n')

def acquireFitbitTokens():
  fitbit = OAuth1Service(
    name='fitbit',
    consumer_key=fitbit_consumer_key(),
    consumer_secret=fitbit_consumer_secret(),
    request_token_url='https://api.fitbit.com/oauth/request_token',
    access_token_url='https://api.fitbit.com/oauth/access_token',
    authorize_url='https://api.fitbit.com/oauth/authorize',
    base_url='https://api.fitbit.com/1/')

  request_token, request_token_secret = fitbit.get_request_token()

  authorize_url = fitbit.get_authorize_url(request_token)
  print 'Go to this URL in a browser: ' + authorize_url
  pin = raw_input('Enter PIN: ')

  session = fitbit.get_auth_session(
  request_token,
  request_token_secret,
  method='POST',
  data={'oauth_verifier': pin})

  f = open('fitbit_oauth_token', 'w')
  f.write(session.access_token)
  f.close()
  f = open('fitbit_oauth_secret', 'w')
  f.write(session.access_token_secret)
  f.close()

