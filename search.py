import tweepy
from keys import consumerKey, consumerSecret, myAccessToken, myAccessTokenSecret
import time
import datetime
import os
import json
import sys

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(myAccessToken, myAccessTokenSecret)
api = tweepy.API(auth)

def userId(screen_name):
    userdata = api.get_user(screen_name)._json
    id = userdata["id"]
    return id

def getDelTweet(id):
    fullTL=_getFullTL(id)
    fullTweetIds=[int(key) for key in fullTL.keys()]
    oldestTweetId=min(fullTweetIds)
    nowTL=[]
    for tweet in _getNowTL(id,oldestTweetId):
        nowTL.append(tweet.id)
    nowTL=set(nowTL)
    retval=[]
    for tweetId in set(fullTweetIds)-nowTL:
        retval.append(fullTL[tweetId])
    return retval


def _getNowTL(id,since):
    i = 0
    while True:
        try:
            tweets = api.user_timeline(id=id, page=i)
            for tweet in tweets:
                yield tweet
                if int(tweet.id)<since:
                    return
            i += 1
            if len(tweets) == 0:
                return
        except tweepy.error.RateLimitError:
            time.sleep(60)
            continue


def _getFullTL(id):
    retval = {}
    folders = os.listdir("./data")
    for folder in folders:
        try:
            fp = open(os.path.join(".", "data", folder,
                                   "{}.txt".format(id)), "r")
        except:
            continue
        for line in fp:
            tweet = json.loads(line.split("\t")[1])
            retval[line.split("\t")[0]] = tweet
    return retval


if __name__=="__main__":
    if sys.argc==1:
        friend=api.friend_ids()
    else:
        friend=[userId(screen_name) for screen_name in sys.argv[1::]]

    for friend in api.friends_ids():
        for tweet in getDelTweet(friend):
            print(tweet)
