#!/usr/bin/python3
""" a module that queries recursively """
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
        A function that queries an API
        Args:
            subreddit (str): subreddit articles title
            host_list (list): A list to store the titles of hot articles
        Returns:
            list: a list containing the titles of all hot articles
    """
    if subreddit is None:
        return None
    headers = {'User-Agent': 'MyRedditScraper/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    param = {'limit': 100, 'after': after}
    response = get(url, headers=headers, params=param, allow_redirects=False)
    try:
        data = response.json().get('data')
        if data['after']:
            return recurse(subreddit, hot_list, data['after'])
        for val in data['children']:
            hot_list.append(val['data']['title'])
        return hot_list
    except Exception:
        return None
