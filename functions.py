import APImir, shellyGateControl, defs
import time


def clearqueue():
    return APImir.mirRequest("DELETE", "/mission_queue")   

def doMission(mission_id):
    data = {"mission_id": mission_id}
    return APImir.mirRequest("POST","/mission_queue", data)

def disToTarget():
    statusData = APImir.mirRequest("GET", "/status") 
    return round(statusData.get("distance_to_next_target"))

def openGate():
    while disToTarget() > 5 or disToTarget() == 0:
        time.sleep(1)
        #print(disToTarget())     

        if disToTarget() < 5:
            break
    print(f"{disToTarget()}m away, Opening gates")
    return shellyGateControl.open()

def checkPLC1():
    plc1 = APImir.mirRequest('GET','/registers/1')
    value = plc1.get('value')
    return value
def resetPLC1():
    APImir.mirRequest('PUT','/registers/1', {'value':'0'})

def pickUp():
    while checkPLC1() == 0  :
        time.sleep(1)  

        if checkPLC1() == 1:
            print("Preparing pistons")
            defs.pick()
            resetPLC1()    
    return 

def placeDown():
    while checkPLC1() == 0  :
        time.sleep(1)  

        if checkPLC1() == 1:
            print("Preparing pistons")
            defs.place()
            resetPLC1()
    return



