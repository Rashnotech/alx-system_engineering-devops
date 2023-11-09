#!/usr/bin/python3
""" a module that recursively queries the reddit API """
from requests import get


def count_words(subreddit, word_list):
    """
        A function that count the word_list
        Args:
            subreddit (str): list of keywords
            word_list (list): contains final count
    """
    count = {}
    recurse(subreddit, word_list, count)
    for key, val in sorted(count.items(), key=lambda x: x[0]):
        print('{}: {}'.format(key, val))


def recurse(subreddit, word_list, count={}, after=None):
    """ recursively count """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyRedditScrapper/1.0'}
    param = {'limit': 100, 'after': after}
    response = get(url, headers=headers, params=param, allow_redirects=False)
    try:
        data = response.json().get('data')
        if data['after']:
            recurse(subreddit, word_list, count, data['after'])
        for val in data['children']:
            titles = val['data']['title']
            for word in word_list:
                for title in titles.split():
                    if title.lower() == word.lower():
                        count[word.lower()] = count.get(word.lower(), 0) + 1
    except Exception:
        return
