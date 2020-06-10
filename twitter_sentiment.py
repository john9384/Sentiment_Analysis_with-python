import string
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3 as got
from main import sentiment, plot_graph, analysis


def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus') \
        .setSince("2019-08-01") \
        .setUntil("2020-02-28") \
        .setMaxTweets(10)

    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length)
	text = text_tweets[i][0] + " " + text

analysis(text)