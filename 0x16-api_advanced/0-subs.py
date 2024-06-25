#!/usr/bin/python3
"""Count the number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Count the number of subscribers for a subreddit."""
    base_url = "https://www.reddit.com"
    headers = {
        "User-Agent": "ALXProjectBot:Devops_0x16 v1.0.0 Advanced API",
    }
    resp = requests.get(
        "{}/r/{}/about.json".format(base_url, subreddit),
        headers=headers,
    )
    return resp.json().get("data", {}).get("subscribers", 0)
