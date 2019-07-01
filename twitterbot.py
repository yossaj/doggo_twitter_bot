import tweepy

print('this is my twitter bot')

CONSUMER_KEY = 'v1DkBLPjtACtvWwCABworreNi',
CONSUMER_SECRET = '35qhW8bzlPUMHVGOQCfXvJRgreHKujvnOXjF5XcXOPF9tW6lyN'
ACCESS_KEY = '1144955407028408321-rcB279KkouRHteW7kggXjtF9V35vqW'
ACCESS_SECRET = 'IPIagFYVIxdFF3wL2Y4kC4HBD63b1TpiYQVs8u6NC0NTT'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id))
