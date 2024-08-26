#!/usr/bin/python3
"""Script to make an API call to Reddit API"""

import requests as req


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number"""
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "praisegee"}

    res = req.get(api_url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0
    return res.json().get("data", {}).get("subscribers")
