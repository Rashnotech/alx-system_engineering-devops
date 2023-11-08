#!/usr/bin/python3
""" a module that queries recursively """
from requests import get


def recurse(subreddit, hot_list=[]):
    """
        A function that queries an API
        Args:
            subreddit (str): subreddit articles title
            host_list (list): 
        Returns:
            list: a list containing the titles of all hot articles
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    reponse = get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
