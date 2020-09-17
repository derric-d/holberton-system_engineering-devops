#!/usr/bin/python3
"""recursive api call"""
import requests


def recurse(subreddit, after=1, hot_list=[]):
    """get top post of sub w/ recursion"""
    url = "http://reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 200, 'after': after}
    headers = {'User-Agent': 'test-agent'}

    subr = requests.get(url, headers=headers, params=params)
    subj = subr.json()

    if subj.get('error', 200) == 404:
        return (None)
    if after is None:
        return hot_list

    a = subj.get('data').get('children')
    for d in a:
        hot_list.append(d.get('data').get('title'))
    p = subj.get('data').get('after')
    return (recurse(subreddit, p, hot_list))
