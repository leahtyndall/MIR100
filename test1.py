import functions, defs

def collectShelf():
    functions.doMission(defs.dockToShelf)
    functions.doMission(defs.footprintWithShelf)
    
    functions.pickUp()
    return

def replaceShelf():
    functions.doMission(defs.dockToShelf)
    functions.doMission(defs.defaultFootprint)
    functions.placeDown()
    return


collectShelf()
functions.doMission(defs.ExcusemeTest)
replaceShelf()