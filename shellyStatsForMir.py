#sends status to mir api for mir dashboard?

#info about shelly

import APIshelly
import shellyGateControl

get = APIshelly.get
request = APIshelly.Request
post = APIshelly.post

#funcs----------------------------------------------
def info():
    info =  get("Shelly.GetDeviceInfo")
    return print(info)

def status():
    status = get("Shelly.GetStatus")
    return print(status)

def config():
    config = get("Shelly.GetConfig")
    return print(config)

def methods():
    methods = get("Shelly.ListMethods")
    return print(methods)

def currScriptID():

    return currScriptID




#simplify down to important ones for dashboard***

#main-----------------------------------------------
   
#info()
#status()

#config()
#methods()