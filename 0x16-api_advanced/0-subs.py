#!/usr/bin/python3
"""
Function that query reddit api and return a number 
"""
import requests

def number_of_subscribers(subreddit):
    """
    function definition to gert number of subs
    """
    url = f"https://api.reddit.com/r/{subreddit}/about"
    header = {'User-Agent': 'CustomClient/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        return(0)
    req = req.json()
    if "data" in req:
        return (req.get("data").get("subscribers"))
    else:
        return(0)
