import basicFunctions, defs

def collectShelf():
    basicFunctions.doMission(defs.dockToShelf)
    basicFunctions.doMission(defs.footprintWithShelf)
    
    basicFunctions.pickUp()
    return

def replaceShelf():
    basicFunctions.doMission(defs.dockToShelf)
    basicFunctions.doMission(defs.defaultFootprint)
    basicFunctions.placeDown()
    return


collectShelf()
basicFunctions.doMission(defs.ExcusemeTest)
replaceShelf()