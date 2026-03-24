import misID, APImir

def doMission(mission_id):
    data = {"mission_id": mission_id}
    return APImir.mirRequest("POST","/mission_queue", data)

