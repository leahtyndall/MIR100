from basicFunctions import doMission, checkPLC1, pickUp, placeDown, enterGate1, exitGate1
import defs, APImir
import time

skipfix = 1

def charge():
    check()
    misText = 'Going to charger'
    doMission(defs.chargingStation)
    return 

def cfb1():#collect shelf from bay 1
    check()
    global misText
    misText = 'Collecting trolley from Bay 1'
    doMission(defs.dockToShelfB1)
    doMission(defs.footprintWithShelf)
    pickUp()
    doMission(defs.leaveDock)   
    doMission(defs.plc2add) 
    return

def dab1(): #deposit shelf at b1
    check()
    global misText
    misText = 'Depositing trolley at Bay 1'

    doMission(defs.dockToShelfB1)
    doMission(defs.defaultFootprint)
    placeDown()


    doMission(defs.leaveDock)   
    return

def dab2(): #deposit bay 2 dock
    check()
    global misText
    misText = 'Depositing trolley at Bay 2'
    doMission(defs.dockToShelfB2)
    doMission(defs.defaultFootprint)
    placeDown()
    doMission(defs.leaveDock)   
    doMission(defs.plc2add)   
    doMission(defs.plc2add)  
    return



def cfb2(): #collect from bay2
    #global varInGate1
    check()
    global misText
    misText = 'Collecting trolley from Bay 2'
    doMission(defs.dockToShelfB2)
    doMission(defs.footprintWithShelf)
    pickUp()

    doMission(defs.leaveDock)   
    doMission(defs.plc2add) 
    return

def da(): #testing for now
    check()
    global misText
    doMission(defs.LeahsDesk)
    
    return
def bay3():
    doMission(defs.LeahsDesk)
    doMission(defs.plc2add) 
    return

def marathon():
    i = 0
    while i <= 100:
        doMission(defs.plc2reset)
        print('Marathon Lap {i}')
        cfb1()
        if checkPLC2 == 1:
            dab2()
        if checkPLC2 == 2:
            bay3()
            time.sleep(10)
        if checkPLC2 == 3:
            cfb2()
        if checkPLC2 == 4:
            dab1()
        i = i + 1

    return

def clearQ():
    return APImir.mirRequest("DELETE", "/mission_queue")


def checkPLC2():
    plc1 = APImir.mirRequest('GET','/registers/2')
    value = plc1.get('value')
    return value
#----------------BAY 2 logic ------------------------------------

def b2LEFT(): #deposit left bay2
    doMission(enterGate1())
    doMission(defs.Desk1)
    inc()
    return 

def check():
    print('checking if in gate 1')
    with open('data.txt', 'rt') as f:
        x = f.read()
        f.close()
        if '1' in x:
            print('In gate, executing exit mission.')
            exitGate1()
            dec()
        if '0' in x:
            print('Not in gate.')
        return

def inc(): #inside gate
    with open('data.txt', 'wt') as f:
        f.write('1')
    return 
def dec(): #not in gate
    with open('data.txt', 'wt') as f:
        f.write('0')
    return 


# -------------testing----------------------
def checktest():
    print('checking if in gate 1')
    with open('data.txt', 'rt') as f:
        x = f.read()
        f.close()
        print(x)
        if '1' in x:
            print('In gate, executing exit mission.')
            dec()
        if '0' in x:
            print('Not in gate, continuing.')
        return

