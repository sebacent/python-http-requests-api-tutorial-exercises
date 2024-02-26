import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php").json()

print(f"Current time: {response['hours']} hrs {response['minutes']} and {response['seconds']} sec")