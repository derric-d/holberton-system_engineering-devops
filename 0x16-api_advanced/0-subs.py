#!/usr/bin/python3
"""api call to get subcount for subreddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    """returns number of subs in subreddit"""
    url = "http://reddit.com/r/{}/about.json".format(subreddit)
    sr = requests.post(url, headers={"User-Agent": "test-user-agent"})
    subjson = sr.json()

    try:
        if "data" in subjson and "subscribers" in subjson["data"]:
            number_subs = subjson["data"]["subscribers"]
        else:
            number_subs = 0
    except ValueError:
        number_subs = 0

    return (number_subs)
