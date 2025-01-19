import requests, json
url = 'http://127.0.0.1:5000'
name = input("For which member would you like to update their points?")
if name in json.loads(requests.get(url+'/handle_get').text):
    name.post(url + '/update_point', json={'new point':  int(input("Insert new point for this member:"))})
else: 
    print("Nonexistent member.")


    


    

    
