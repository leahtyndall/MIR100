import APImir
import MIRstatus
import misID
import shellyGateControl
import time
#
statusData = APImir.mirRequest("GET", "/status") 
dis = MIRstatus.disToTarget()
#robot actions

def clearqueue():
    return APImir.mirRequest("DELETE", "/mission_queue")                   
                      
def doMission(mission_id):
    data = {"mission_id": mission_id}
    return APImir.mirRequest("POST","/mission_queue", data)

def disToTarget():
    statusData = APImir.mirRequest("GET", "/status") 
    return round(statusData.get("distance_to_next_target"))

def openGate():
    while disToTarget() > 4 or disToTarget() == 0:
        time.sleep(1)
        print(disToTarget())     

        if disToTarget() < 5:
            break
    print(f"{disToTarget()} Opening gates")
    return shellyGateControl.open()


#--------------------------------------------------------------------------------------------------------------------------
#main method
if __name__ == "__main__":

    #doMission(misID.MarathonTest)
    '''
    print("on my way dawg")
    clearqueue()
    #approach gate
    doMission(misID.ApproachGate1)
    #check if open??????????
        #closed -> open it
    openGate()
    time.sleep(1)
    doMission(misID.Desk1)
    time.sleep(2)
    doMission(misID.ExitGate1)
    openGate()
    time.sleep(2)
    doMission(misID.LeahsDesk)
   '''
    #go to pos
