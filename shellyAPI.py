import requests
import json
import ShellyPy

ip = "192.168.30.25"
id = "shellyplus1pm-fcb467285ecc"
baseURL = "http://192.168.30.25"

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
    
    print(response.text)
    return print(response.text)
#GET--------------
def get(url):
    url = baseURL + url
    response = requests.get(
        url
    )

    return response.json()
#POST--------------
def post(url, body):
    url = baseURL + url
    response = requests.post(
        url,
        body
    )

    return response.json()
#testing----
#funcs----------------------------------------------
def info():
    return get("/shelly")



#main-----------------------------------------------
if __name__ == "__main__":
   
   print(info())
    


















