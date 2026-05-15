from layout.Funcs.basicFunctions import doMission, checkPLC1, pickUp, placeDown, enterGate1, exitGate1
import layout.Funcs.defs as defs
from layout.Funcs.API import APImir
import time

skipfix = 1

def charge():
    check()
    misText = 'Going to charger'
    doMission(defs.chargingStation)
    return 

def cfb1():#collect shelf from bay 1
    print('adding to plc2')
    check()
    print('Collecting trolley from Bay 1')
    doMission(defs.dockToShelfB1)
    doMission(defs.footprintWithShelf)
    print('picking up shelf')
    pickUp()
    print('leaving dock')
    doMission(defs.leaveDock)   
    doMission(defs.plc2add)
    return

def dab1(): #deposit shelf at b1
    check()
    print('Depositing trolley at Bay 1')
    doMission(defs.dockToShelfB1)
    doMission(defs.defaultFootprint)
    placeDown()
    print('leaving')
    doMission(defs.leaveDock)   
    doMission(defs.plc2add)
    return

def dab2(): #deposit bay 2 dock
    check()
    print('Depositing trolley at Bay 2')
    doMission(defs.dockToShelfB2)
    doMission(defs.defaultFootprint)
    placeDown()
    print('leaving')
    doMission(defs.leaveDock)   
    doMission(defs.plc2add)
    return



def cfb2(): #collect from bay2
    check()
    print('Collecting trolley from Bay 2')
    doMission(defs.dockToShelfB2)
    doMission(defs.footprintWithShelf)
    pickUp()
    print('leaving')
    doMission(defs.leaveDock)   
    doMission(defs.plc2add)  
    return

def da(): #testing for now
    check()
    doMission(defs.LeahsDesk)
    
    return
def bay3():
    doMission(defs.LeahsDesk)
    #doMission(defs.plc2add)   
    return

################
#decorator to only run each mission once:

def marathon():
    i = 0 #laps
    j = 1
    while i <= 100 and j < 10:
        print(f'Marathon Lap {i}')
        #print('checking plc')
        #doMission(defs.plc2reset)
        while checkPLC2() == 0:

            doMission(defs.plc2add)
            print('plc = 0, collecting from b1')
            cfb1()
       
            
        while checkPLC2() == 2:

            doMission(defs.plc2add)
            print('plc = 2, depositing at b2')
            dab2()
            
        while checkPLC2() == 4:

            doMission(defs.plc2add)
            print('plc = 4, going to b3')
            bay3()
            time.sleep(10)
            
        while checkPLC2() == 6:
 
            doMission(defs.plc2add)
            print('plc = 6, collecting from b2')
            cfb2()
            
        while checkPLC2()== 8:
            doMission(defs.plc2add)
            print('plc = 8, depositing at b1')
            dab1()
            i = i + 1
            print('resetting plc2')
            
            doMission(defs.plc12)
            doMission(defs.leaveDock)
            doMission(defs.plc2reset)
    return


def clearQ():
    return APImir.mirRequest("DELETE", "/mission_queue")


def checkPLC2():
    plc2 = APImir.mirRequest('GET','/registers/2')
    value = plc2.get('value')
    return value
#----------------BAY 2 logic ------------------------------------

def b2LEFT(): #deposit left bay2
    doMission(enterGate1())
    doMission(defs.Desk1)
    inc() #tells program mir is intside gate, & will need to run exit sequence to carry out next mission
    return 

def check(): #checks if mir is inside gate
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

