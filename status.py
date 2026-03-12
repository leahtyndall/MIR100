import mirAPI
import json

def getStat():
    return (mirAPI.mirRequest("GET", "/status"))

if __name__ == "__main__":

    getStat()