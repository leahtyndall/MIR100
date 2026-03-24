import APImir
import shellyStatsForMir
import shellyGateControl
import json
import pandas as pd
import base64

dataCache = {}
statusData = APImir.mirRequest("GET", "/status") 

def status():
    global dataCache
    dataCache = APImir.mirRequest("GET", "/status") 

def isAvailable():
    check = statusData.get('mission_text')
    print(check)
    true = 'Waiting for new missions...'
    if check == true:
        return True
    else:
        return False
    
def imu():
    imu = statusData.get("imu_data")
    return print(imu)

def getBattery():
    
    batteryStat = round(statusData.get("battery_percentage"))
    #return print[f"Battery: {round(batteryStat)}%"]
    return batteryStat

def timeRemaining(): 
    totalSec = statusData.get("battery_time_remaining")
    sec = totalSec%60
    totalMinRem = (totalSec - sec)/60
    min = round(totalMinRem%60)
    hrs = round((totalMinRem - min)/60)
    #text = f"{hrs} hours, {min} minutes, {sec} seconds"
    return hrs, min, sec
    
def mapData():
    encoded = base64.b64encode(open("AllBays.png", "rb").read()).decode()
    return encoded 

def shellyStatus():
    status = shellyStatsForMir.status()
    return status

def disToTarget():
    dis = statusData.get("distance_to_next_target")  
    return round(dis)
    
def MissionQ():
    curr = APImir.mirRequest('GET', '/mission_queue')
    #curr = curr.json()

    executing = [x for x in curr if x['state'] in ['Executing']]
    pending = [y for y in curr if y['state'] in ['Pending']]

    return executing, pending

def getNet():
    try:
        if statusData.status_code == 200:
            return 1 #connected
        else:
            return 2 # error
    except:
        return 3 #emergency stop/ offline
    
    print(all)
    #return connected

def getHookStat():

    return 




#df = pd.read_csv("MIRstatus.csv")
#main------------------------------------------

print(getNet())