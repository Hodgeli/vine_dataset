import tweepy
from tweepy import OAuthHandler
import re

list_consumer_key = ['3iOrezuLYC361nCZq5sPGiPTk', 'rUEewcYmZ29RENbK9Zys7BIju', 'lnuiXUBXwINyAMF6qz4yP9Efx',
                     'KcOOV0GO55nQGrodtdkn8pQmk']
list_consumer_secret = ['tMhO96rcDf3gjZr5gmiLPkMXvuJv7KuK2ybAVvYvgBlfJ6AXI7',
                        'MrDNw1i8DAM1t1uzMNww5txwJeAlYM9alNyQuXP4INDvK36KGJ',
                        'kqFHQ16gizG8UGtIxja4yple96vgvgxOJLChRU2wqoBiEtcaN2',
                        'd7KKdaVMK5Hc0XrlcCrWT6LdkUqCpGRg17hMv8PnFuMJDAa1oQ']
list_access_token = ['933167894174638082-ulbCNF3X9MGDX3MqsmfVtZ9KwNXOowz',
                     '933167894174638082-8JrZ60CdTL5LfWqaEzEVNWx7sfrrWum',
                     '933167894174638082-1JQ1QlHk6nWXSlIof9QfMM2AfVPuC9P',
                     '933167894174638082-D5HF3uRXqs0OXnebOHG1oXnY2AGh0zN']
list_access_secret = ['Puq70XWl5FBZ6dvlP5S8IUwoav4g5DVyQh72KXowrZedT', 'XXweYCt7YwsK1nJ3EEEgLsRSEXfbrrmTzNqVDCSZuX2ER',
                      'ydO3dghdnS0WUqj0osEpmZhVczToic1EqXX52QK8hiq8Q', 'DeGsdWaRR3u8ENGcPQXbh9lVoHUtoK5tRV4bJEH2AcyDc']

num_key = 0
consumer_key = list_consumer_key[num_key]
consumer_secret = list_consumer_secret[num_key]
access_token = list_access_token[num_key]
access_secret = list_access_secret[num_key]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# api = tweepy.API(auth) # 不使用代理
api = tweepy.API(auth, proxy="127.0.0.1:1080")

f_hash = open("count_hash.txt", encoding='utf8', errors='ignore')
list_hash = []
while 1:
    line_hash = f_hash.readline()
    if not line_hash:
        break
    else:
        list_hash.append(str(re.findall(r"'(.*?)'", line_hash, flags=0)[0]))
print('list_hash生成成功：' + str(len(list_hash)))

for id in range(1056, len(list_hash)):
    try:
        query = str(list_hash[id])
        print(query)
        # 获取推文
        tweets = tweepy.Cursor(api.search, q=query, count=100, lang='en', include_entities=False).items(300)
        f_twitter = open("./hash_twitter/" + str(list_hash[id]), 'w', encoding='utf8', errors='ignore')
        i = 0
        for tweet in tweets:
            f_twitter.write(str(tweet.text).replace('\n', ' ') + '\n')
            i += 1
        print(i)
        if (i < 300):
            f_short_hash = open("short_hash.txt", 'a', encoding='utf8', errors='ignore')
            f_short_hash.write(str(list_hash[id]) + '\n')
            f_short_hash.close()
        print(id)
    except(TypeError, tweepy.error.TweepError):
        print(str(list_hash[id]) + '爬取失败')
        f_error_hash = open("error_hash.txt", 'a', encoding='utf8', errors='ignore')
        f_error_hash.write(str(list_hash[id]) + '\n')
        f_error_hash.close()
        # 更换key
        num_key += 1
        if (num_key == 4):
            num_key = 0
        consumer_key = list_consumer_key[num_key]
        consumer_secret = list_consumer_secret[num_key]
        access_token = list_access_token[num_key]
        access_secret = list_access_secret[num_key]

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth, proxy="127.0.0.1:1080")
        print('key更换成功，继续下载------------------------->')
