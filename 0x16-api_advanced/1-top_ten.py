#!/usr/bin/python3
""" a module that queries API """
from requests import get


def top_ten(subreddit):
    """ A function that queries the Reddit API
        Args:
            subreddit (str): the name of the subreddit
        Returns:
            str: print valid titles
    """
    load = {'limit': 10}
    headers = {'User-Agent': 'MyRedditScraper/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    # Set a custom User-Agent to avoid API rate limiting
    response = get(url, headers=headers, params=load, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        for val in data['children']:
            print(val['data']['title'])
    else:
        print(None)
