from dash import Dash, html, dcc
from MIRstatus import getBattery, timeRemaining, mapData
from dashboard import app


@app.callback(
    Output('battery', 'children'),
    Output('time', 'children'),
    #Output('map','children'),
    Input('interval','n_intervals')
)
def updateBattery(n):
    battery = getBattery()
    hrs, min, sec = timeRemaining()
    #map = mapData()
    return(
        f"Battery: {battery}%",
        f"Time remaining: {hrs}hrs, {min}mins, {sec}secs",
           
    )

