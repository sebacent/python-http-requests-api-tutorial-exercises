import requests

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
resp = requests.get(url).json()

print(resp[1]['name'])