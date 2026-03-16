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
    print("Status: ",flush=True)
    status = get("Switch.GetStatus" + id)
    return status

def status2():
    print("Status: ",flush=True)
    status = get("Zigbee.GetStatus")
    return status

def extend():
    extend = get("Switch.Set" + id+on)
    print("Extending", flush = True)
    return extend

def retract():
    retract = get("Switch.Set" +id+off)
    print("Retracting",flush=True)
    return retract






#main-----------------------------------------------



status2()
'''
time.sleep(1)
extend()
status()
time.sleep(3)
retract()'''