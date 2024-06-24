#!/usr/bin/python3
""" Return the total number of subscribers on a subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    uri = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    head = {'user-agent': 'PC-EKSCM'}
    try:
        response = requests.get(uri, headers=head, allow_redirects=False)
        info = (response.json())['data']
        a = info['subscribers']
        return(a)
    except Exception:
        return (0)
