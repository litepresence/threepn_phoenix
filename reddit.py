"""
https://www.jcchouinard.com/reddit-api-without-api-credentials/
"""
import time

import requests


def get_reddit(subreddit, listing, count, timeframe):

    """
    :param str(subreddit):
    :param str(listing): [controversial, best, hot, new, random, rising, top]
    :param int(count): # count of returned posts
    :param str(timeframe): [hour, day, week, month, year, all]




    url = f"https://www.reddit.com/r/{subreddit}/{listing}.json"
    params = {
        "limit": count,
        "t": timeframe,
    }

    time.sleep(2)
    return requests.get(url, params=params).json()

    """
    url = f"https://www.reddit.com/r/{subreddit}/{listing}.json?limit={count}&t={timeframe}"

    time.sleep(2)
    return requests.get(url).json()


print(get_reddit("printedguns", "top", 100, "new"))
