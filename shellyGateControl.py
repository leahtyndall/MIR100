import APIshelly


import time
get = APIshelly.get
request = APIshelly.Request
post = APIshelly.post

id = "?id=0"
on = "&on=true"
off = "&on=false"


#funcs----------------------------------------------
def status():
    print("Switch status: ",flush=True)
    status = get("Switch.GetStatus" + id)

    return status ##

def open():
    extend = get("Switch.Set" + id+on)
    print("Opening", flush = True)
    return extend

def close():
    retract = get("Switch.Set" +id+off)
    print("Closing",flush=True)
    return retract

def shellyStatus():
    print("Shelly Status: ")
    status = get("Shelly.GetStatus")
    return status


'''def isOpen():
    get("Switch.GetStatus"+id)
    out = {"output":  }
    response = out
    return print(response)'''



    



    

#main-----------------------------------------------
#close()

"""
status()
open()
time.sleep(5)
status()
close()
time.sleep(5)
status()

open()
time.sleep(15)
close()

status()

#Stays open for ~40 seconds

status()
close()
status()

"""

