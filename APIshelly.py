import requests
import json



#lab
ipX = "192.168.30.11"

id = "shellyplus1pm-fcb467285ecc"
baseURL = "http://192.168.30.116" #change backl to lab!!

#helper funcs--------------------------------------
#REQUEST---------------
def Request(method, url, body = None):
    url = baseURL + url
    #print(url)
    
    response = requests.request(
        method,
        url,
        json=body
    )
    data = response.json()
    return json.dumps(data, indent = 4)


#GET--------------
def get(url):
    url = baseURL + "/rpc/" + url
    response = requests.get(
        url
    )
    data = response.json()
    return json.dumps(data, indent = 4)


#POST--------------
def post(url, body):
    url = baseURL + "/rpc/" + url
    response = requests.post(
        url,
        body
    )
    data = response.json()
    return json.dumps(data, indent = 4)
#testing----



















