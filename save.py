import tweepy
from keys import consumerKey, consumerSecret, myAccessToken, myAccessTokenSecret
import time
import datetime
import os
import json

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(myAccessToken, myAccessTokenSecret)
api = tweepy.API(auth)
since = 1082469419694010368


while True:
    tl = api.home_timeline(since_id=since, count=1000)[::-1]
    if len(tl)>0:
        today = datetime.datetime.today()
        year = today.year
        month = today.month
        day = today.day
        path = os.path.join("data", "{0}-{1:02}-{2:02}".format(year, month, day))
        os.makedirs(path, exist_ok=True)

        for tweet in tl:
            with open(os.path.join(path, "{}.txt".format(tweet.user.id)), "a+") as fp:
                fp.write(tweet.id_str)
                fp.write("\t")
                fp.write(json.dumps(tweet._json,ensure_ascii=False))
                fp.write("\n")
        since = tl[-1].id

    print(since)
    time.sleep(15 * 60 / 14)
