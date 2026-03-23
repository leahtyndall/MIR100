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
    
def reply():
    battery = getBattery()
    timeRem = timeRemaining()
    dis = disToTarget()
    #print(shellyStatus())
    print(f"Battery: {battery}%")
    print(f"Time remaining: {timeRem}")
    #print(f"Distance to next target: {dis}m")  
      
    return print(f"Battery: {battery}% & Time remaining: {timeRem}")




#df = pd.read_csv("MIRstatus.csv")
#main------------------------------------------

