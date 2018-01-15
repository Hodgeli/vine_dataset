import tweepy
from tweepy import OAuthHandler
import json

consumer_key = '3iOrezuLYC361nCZq5sPGiPTk'
consumer_secret = 'tMhO96rcDf3gjZr5gmiLPkMXvuJv7KuK2ybAVvYvgBlfJ6AXI7'
access_token = '933167894174638082-ulbCNF3X9MGDX3MqsmfVtZ9KwNXOowz'
access_secret = 'Puq70XWl5FBZ6dvlP5S8IUwoav4g5DVyQh72KXowrZedT'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# api = tweepy.API(auth)
api = tweepy.API(auth, proxy="127.0.0.1:1080")

##################################
f_twitter = open("funny", 'w', encoding='utf8', errors='ignore')

query = 'likeforlike'
tweets = tweepy.Cursor(api.search, q=query, count=100, lang='en', include_entities=False).items(250)
i = 0
for tweet in tweets:
    i += 1
    if (tweet.text):
        f_twitter.write(str(tweet.text).replace('\n', ' ') + '\n')
        print(i)


# while True:
#     tweet_page = tweets.pages().next()
#     print(json.dumps(tweet_page['statuses']))
#     break
f_twitter.close()
# query = '#funny'
# tweets = tweepy.Cursor(api.search, q=query, lang='en', since_id='1', result_type="mixed",
#                        include_entities=True).items(500)
#
# f_twitter = open("fun", 'w', encoding='utf8', errors='ignore')
# i = 0
# for tweet in tweets:
#     _json = tweet._json
#     dict_twitter = eval(str(_json))
#     f_twitter.write(str(dict_twitter['text']).replace('\n', ' ') + '\n')
#     i += 1
# print(i)

# i = 0
# for tweet in tweets:
#     i += 1
#     _json = tweet._json
#     dict_twitter = eval(str(_json))
#     f_twitter.write(str(dict_twitter['text']).replace('\n', ' ') + '\n')
#     if (i == 500):
#         f_twitter.close()
