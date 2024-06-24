#!/usr/bin/python3
""" Return the total number of subscribers on a subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    uri = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    head = {'user-agent': 'PC-EKSCM'}
    info = requests.get(uri, headers=head).json()
    info = info['data']
    a = info['subscribers']
    return(a)
