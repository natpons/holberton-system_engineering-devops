#!/usr/bin/python3
"""
Queries the Reddit API.
Returns the number of subscribers for a given subreddit
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function queries the Reddit API and returns the number of subscribers
    """
    if subreddit is None or type(subreddit) is not str:
        return (0)

    headers = {'User-Agent':
               'Python/requests: APIadvancedproject: v1.0.0 (by /u/natpons)'}
    req = requests.get('http://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=headers).json()

    num_subs = req.get('data', {}).get('subscribers')
    return num_subs
