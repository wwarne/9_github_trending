import requests
import urllib.parse
from datetime import datetime, timedelta


GITHUB_API_ENDPOINT = 'https://api.github.com/'


def get_trending_repositories(top_size):
    week_ago = (datetime.utcnow() - timedelta(days=7)).strftime('%Y-%m-%d')
    request_url = urllib.parse.urljoin(GITHUB_API_ENDPOINT, '/search/repositories')
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
    response = requests.get(request_url, params=request_params, headers=request_headers)
    if response.status_code == 200:
        return response.json()['items']
    return None


def print_trending_repositories(repos_data):
    if repos_data:
        print('The most popular repositories created in the past week')
        for idx, repository in enumerate(repos_data, start=1):
            print('{}. Name: {} | Stars: {} | Issues: {} | URL: {}'.format(idx,
                                                                           repository['name'],
                                                                           repository['stargazers_count'],
                                                                           repository['open_issues_count'],
                                                                           repository['html_url']))
    else:
        print('No information about repositories')


if __name__ == '__main__':
    trends = get_trending_repositories(20)
    print_trending_repositories(trends)
