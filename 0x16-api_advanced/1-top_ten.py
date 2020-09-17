#!/usr/bin/python3
"""api call to get subcount for subreddit"""
import requests
import sys


def top_ten(subreddit):
    """returns number of subs in subreddit"""
    url = "http://reddit.com/r/{}/hot.json".format(subreddit)
    sr = requests.post(url, headers={"User-Agent": "test-user-agent"})
    subjson = sr.json()

    if "data" in subjson:
        posts = subjson["data"]["children"]
        for p in posts[:10]:
            print(p["data"]["title"])
    else:
        print(None)
