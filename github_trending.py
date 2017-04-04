import requests
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    week_ago = (datetime.utcnow() - timedelta(days=7)).strftime('%Y-%m-%d')
    request_headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'wwarne'
    }
    request_params = {
        'q': 'created:>={}'.format(week_ago),
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_size
    }
    response = requests.get('https://api.github.com/search/repositories', params=request_params, headers=request_headers)
    if response.status_code == 200:
        return response.json()['items']


def print_trending_repositories(repos_data):
    if not repos_data:
        print('No information about repositories')
        return
    print('The most popular repositories created in the past week')
    for idx, repository in enumerate(repos_data, start=1):
        print('{}. Name: {} | Stars: {} | Issues: {} | URL: {}'.format(idx,
                                                                       repository['name'],
                                                                       repository['stargazers_count'],
                                                                       repository['open_issues_count'],
                                                                       repository['html_url']))


if __name__ == '__main__':
    trends = get_trending_repositories(20)
    print_trending_repositories(trends)
