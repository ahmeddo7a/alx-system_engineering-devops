#!/usr/bin/python3
"""
function that queries reddit api and returns number
of subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    function definition of getting number of subs
    """
    url = f"https://api.reddit.com/r/{subreddit}/about"
    header = {'User-Agent': 'CustomClient/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        return (0)
    req = req.json()
    if "data" in req:
        return (req.get("data").get("subscribers"))
    else:
        return (0)
