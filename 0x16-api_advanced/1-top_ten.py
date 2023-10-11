#!/usr/bin/python3
"""
reddit api querry
"""
import requests


def top_ten(subreddit):
    """
    function definition that prints the titles of first 10 hot posts listed
    for a given subreddit
    """
    url = f"https://api.reddit.com/r/{subreddit}?sort=hot&limit=10"
    header = {'User-Agent': 'CustomClient/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        print(None)
        return
    req = req.json()
    if "data" in req:
        for post in req.get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
