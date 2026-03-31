import APImir, shellyGateControl, defs, MIRstatus
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
def setPLC1():
    APImir.mirRequest('PUT','/registers/1', {'value':'2'})

def pickUp():
    while checkPLC1() == 0  :
        time.sleep(1)  

        if checkPLC1() == 1:
            print("Preparing pistons")
            defs.pick()
            setPLC1()
            time.sleep(10)    
    return 

def placeDown():
    while checkPLC1() == 0  :
        time.sleep(1)  

        if checkPLC1() == 1:
            print("Preparing pistons")
            defs.place()
            setPLC1()
            time.sleep(10)    
    return
#################################################################    
#BAY 1        
#################################################################  
def pickUpSequenceB1():
    doMission(defs.dockToShelfB1)
    doMission(defs.footprintWithShelf)
    pickUp()
    while checkPLC1() == 1:
        time.sleep(1)
        if checkPLC1() == 2:
            time.sleep(5)
            doMission(defs.leaveDock)
    return
def depositSequenceB1():
    doMission(defs.dockToShelfB1)
    doMission(defs.defaultFootprint)
    placeDown()
    while checkPLC1() == 1:
        time.sleep(1)
        if checkPLC1() == 2:
            time.sleep(5)
            doMission(defs.leaveDock)
    return
#################################################################    
#BAY 2         
#################################################################  
def pickUpSequenceB2():
    doMission(defs.dockToShelfB2)
    doMission(defs.footprintWithShelf)
    pickUp()
    while checkPLC1() == 1:
        time.sleep(1)
        if checkPLC1() == 2:
            time.sleep(5)
            doMission(defs.leaveDock)
    return

def depositSequenceB2():
    doMission(defs.dockToShelfB2)
    doMission(defs.defaultFootprint)
    placeDown()
    while checkPLC1() == 1:
        time.sleep(1)
        if checkPLC1() == 2:
            time.sleep(5)
            doMission(defs.leaveDock)
    return

