#!/usr/bin/python3
""" Return the total number of subscribers on a subreddit"""
import urllib.request
import json


def number_of_subscribers(subreddit):
    uri = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {'User-Agent': 'PC_ALX'}
    request = urllib.request.Request(uri, headers=head)

    try:
        with urllib.request.urlopen(request) as response:
            data = response.read().decode('utf-8')
            info = json.loads(data).get('data')
            val = info.get('subscribers')
            return val
    except Exception:
        return 0
