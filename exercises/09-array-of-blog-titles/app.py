import requests


def get_titles():
    arr_titles = []
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    resp = requests.get(url).json()
    
    for post in resp['posts']:
        arr_titles.append(post['title'])\
        
    return arr_titles


print(get_titles())