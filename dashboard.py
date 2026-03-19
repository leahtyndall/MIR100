from dash import Dash, html,dcc
import dash_ag_grid as dag
import pandas as pd
from dash.dependencies import Input, Output
from MIRstatus import getBattery, timeRemaining
from layout import layout
#from MIRstatus import df



app = Dash()
#app.layout = layout
app.layout = html.Div([
    html.H1('MiR Robot'),

    dcc.Interval(id='interval',interval=2000),

    html.Div(id='battery'),
    html.Div(id='status')
])
#LAYOUT-----------------------------------

@app.callback(
    Output('battery', 'children'),
    Output('time', 'children'),
    Input('interval','n_intervals')
)

def updateBattery(n):
    battery = getBattery()
    return f"Battery: {battery}%"


def updateTime(n):
    hrs, min, sec = timeRemaining()
    return f"Time remaining: {hrs}hrs, {min}min, {sec}sec"


if __name__ == '__main__':
    app.run(debug=True)