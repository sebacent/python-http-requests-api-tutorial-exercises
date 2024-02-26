import requests

def get_post_tags(post_id):
    post_body = int
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    resp = requests.get(url).json()
    
    for post in resp['posts']:
        if (post["id"] == post_id):
            return post
        
    


print(get_post_tags(146))