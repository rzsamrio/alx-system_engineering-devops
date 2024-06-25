#!/usr/bin/python3
""" Return the total number of subscribers on a subreddit"""
import requests


def number_of_subscribers(subreddit):
    uri = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {'user-agent': 'PC_ALX'}
    try:
        response = requests.get(uri, headers=head, allow_redirects=False)
        info = (response.json()).get('data')
        val = info.get('subscribers')
        return (val)
    except Exception:
        return (0)
