from dash import Dash, html, dcc, ctx, callback
import defs
from dash.dependencies import Input, Output
from MIRstatus import getBattery, timeRemaining, getNet, misText, stateID, isAvailable
import CallTo, basicFunctions
import datetime
import dash_bootstrap_components as dbc
import dash_player as dp
from layout import layout

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
 
app.layout = layout

#callbacks-----------------------------------

@app.callback(
    Output('battery', 'children'),
    Output('time', 'children'),
    Input('interval-component','n_intervals')
)
def updateBattery(n):
    battery = getBattery()
    hrs, min, sec = timeRemaining()    
    return(
        html.P("Battery: {}%".format(battery)),
        html.P("Time remaining: {}hrs, {}mins, {}secs".format(hrs, min, sec)),
       )

@app.callback(
    Output('text','children'),
    Output('state', 'children'),
    #Output('pending','children'),
    Input('interval-component','n_intervals')
)
def updatemisQue(n):
    text = misText()
    state = stateID()
    return text, state

@app.callback( #buttons
    Output('container', 'children'),
    
    Input('mydesk', 'n_clicks'),
    Input('pick', 'n_clicks'),
    Input('place', 'n_clicks'),
    Input('pickUpSequenceB1', 'n_clicks'),
    Input('depositSequenceB1', 'n_clicks')

    #Input('dock', 'n_clicks'),
    #State('inputOnClick', 'id')
)
def buttonClicked(b1,b2,b3,b4,b5):
    if 'mydesk' == ctx.triggered_id:
        return CallTo.doMission(defs.LeahsDesk)
    elif 'pick' == ctx.triggered_id:
        return defs.pick()
    elif 'place' == ctx.triggered_id:
        return defs.place()
    elif 'pickUpSequenceB1' == ctx.triggered_id:
        return basicFunctions.pickUpSequenceB1()
    elif 'depositSequenceB1' == ctx.triggered_id:
        return basicFunctions.depositSequenceB1()

if __name__ == '__main__':
    app.run(debug=True)