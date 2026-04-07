from layout.Funcs import shelfPistons 
import time
#######################################################################
#missions
#######################################################################
chargingStation = "8adac375-2c3d-11f1-8b7b-f44d306dcb63"

MarathonTest = "0dbf65b4-1c6b-11f1-9e24-f44d306dcb63"
ExcusemeTest = "37d167ab-1640-11f1-acd6-f44d306dcb63"
LeahsDesk = "79449806-1e17-11f1-9e24-f44d306dcb63"
ApproachGate1 = "47477595-22c4-11f1-8d1e-f44d306dcb63"
ExitGate1 = "7e510fc1-22d3-11f1-8d1e-f44d306dcb63"
Desk1 = "4f0d65a2-22d3-11f1-8d1e-f44d306dcb63"

#######################################################################
## footprints
#######################################################################
defaultFootprint = '11d39594-283c-11f1-8f8d-f44d306dcb63'
footprintWithShelf = '54b23ee4-283b-11f1-8f8d-f44d306dcb63'


#######################################################################
## Shelf 
#######################################################################
dockToShelfB1 = "6794c9a0-28e7-11f1-8f8d-f44d306dcb63"
dockToShelfB2 =  "b50b4ba2-29c2-11f1-8f8d-f44d306dcb63"
leaveDock = "40cab873-29bf-11f1-8f8d-f44d306dcb63"

def pick():
    shelfPistons.TuyaDeviceController.pick()
    return
    
def place():
    shelfPistons.TuyaDeviceController.place()
    return