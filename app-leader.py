import requests, json
url = 'http://127.0.0.1:5000'
name = input("For which member would you like to update their points?")


factions = json.loads(requests.get(url+'/handle_get').text)
for key in factions:
    if name in factions[key]['members']:
        requests.post(url + '/update_point', json={'faction': key, 'name' : name, 'point':  int(input("Insert new point for this member:"))})


    


    

    
