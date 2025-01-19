import requests
import json
url = 'http://127.0.0.1:5000'
headers = {'Content-Type': 'application/json'}
request = input("Would you like to update your name or display the DBZ dashboard?(u/d)")
if (request == 'u'):
    requests.post(url + '/update_name', json={'newname': input("What is your new name?")})

elif (request== 'd'):
    print(json.loads(requests.get(url + '/handle_get',headers=headers).json()))



