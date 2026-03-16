import APImir
import json

statusData = APImir.mirRequest("GET", "/status") 

def getBattery():
    
    batteryStat = statusData.get("battery_percentage")  
    return round(batteryStat)

def timeRemaining():
    
    totalSec = statusData.get("battery_time_remaining")
    sec = totalSec%60
    totalMinRem = (totalSec - sec)/60
    min = round(totalMinRem%60)
    hrs = round((totalMinRem - min)/60)
    
    text = f"{hrs} hours, {min} minutes, {sec} seconds"

    return text
        
        


#main------------------------------------------
if __name__ == "__main__":

    battery = getBattery()
    timeRem = timeRemaining()
    print(f"Battery: {battery}%")
    print(f"Time remaining: {timeRem}")