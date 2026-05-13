import layout.Funcs.defs as defs, layout.Funcs.API.APImir as APImir

def doMission(mission_id):
    data = {"mission_id": mission_id}
    return APImir.mirRequest("POST","/mission_queue", data)

