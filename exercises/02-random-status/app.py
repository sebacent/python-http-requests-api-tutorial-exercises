import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

def error_code (status):
    if (status == 200):
        return "Everything went perfect\n"
    elif (status == 400):
        return "Something is wrong on the request params\n"
    elif (status == 404):
        return "The URL you asked is not found\n"
    elif (status == 503):
        return "Unavailable right now\n"

# TEST FALLAN AUNQUE LAS RESPUETAS SEAN LA CORRECTAS: SyntaxError: invalid decimal literal
    
print(error_code(response.status_code))