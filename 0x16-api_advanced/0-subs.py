#!/usr/bin/python3
""" a module that queries API """
import requests


def number_of_subscribers(subreddit):
    """ A function that queries the Reddit API
        Args:
            subreddit (str): the name of the subreddit
        Returns:
            int: number of subscribers
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    # Set a custom User-Agent to avoid API rate limiting
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    return 0
