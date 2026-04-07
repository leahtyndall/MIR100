from layout.Funcs.API import APImir
from layout.Funcs import basicFunctions, defs
import layout.Funcs.shellyStatsForMir as shellyStatsForMir
import layout.Funcs.shellyGateControl as shellyGateControl
import time, json
import pandas as pd
import base64


statusData = APImir.mirRequest("GET", "/status") 

def status():
    
    dataCache = APImir.mirRequest("GET", "/status") 
    
def getBattery():
    statusData = APImir.mirRequest("GET", "/status")
    battery = round(statusData.get("battery_percentage"))
    if battery < 20:
        basicFunctions.doMission(defs.chargingStation)
    return battery
   # elif battery <= 53:
    #    
    #return battery
    
           
def isAvailable():
    statusData = APImir.mirRequest("GET", "/status")
    check = statusData.get('mission_text')
    print(check)
    true = 'Waiting for new missions...'
    if check == true:
        return 'available'
    else:
        return False            

    #return print[f"Battery: {round(batteryStat)}%"]
    return 
def timeRemaining(): 
    statusData = APImir.mirRequest("GET", "/status")
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
    statusData = APImir.mirRequest("GET", "/status")
    dis = statusData.get("distance_to_next_target")  
    return round(dis)
    
def misText():
    statusData = APImir.mirRequest("GET", "/status")
    text = statusData.get('mission_text')
    return text

def modekeystate():
    statusData = APImir.mirRequest("GET", "/status")
    state = statusData.get('mode_key_state')
    if state == 'idle' and getBattery() > 20:
        return 'Available'
    else:
        return 'On a mission'

def getNet():
    statusData = APImir.mirRequest("GET", "/status")
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

#################################################################    
#State IDs       
################################################################# 
def stateID():
    statusData = APImir.mirRequest("GET", "/status")
    stateid = statusData.get('state_id')
    if stateid == 0:
        return 'Starting up'
    elif stateid == 3:
        return 'Ready for mission'
    elif stateid == 4:
        return 'Executing mission'
    elif stateid == 11:
        return 'Emergency stop'
    elif stateid ==12:
        return 'Paused'

def error():
    statusData = APImir.mirRequest("GET", "/status")
    error = statusData.get('errors')

    return error



#df = pd.read_csv("MIRstatus.csv")
#main------------------------------------------
