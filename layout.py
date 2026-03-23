'''
from dash import Dash, html, dcc
import dash_ag_grid as dag
import pandas as pd
from dash.dependencies import Input, Output
from MIRstatus import getBattery, timeRemaining
from layout import layout
#from MIRstatus import df

COLOURS = {
    'navy':'#1f2442',
    'blue': '#a9afd4',
    'backgnd': '#dadded'
}

app = Dash()
#app.layout = layout
#**************prev working

app.layout = html.Div([
    html.H1('MiR Robot',
            style={'color': COLOURS['blue']}),
    dcc.Interval(id='interval',interval=1000),
    html.Div(id='battery',
             style={'color': COLOURS['blue']}),
    html.Div(id='time',
             style={'color': COLOURS['blue']}),
], style ={
    'width':'30%',
    'padding':'20px',
    'backgroundColor': COLOURS['navy'],
    

    'borderRadius':'10px',
    'margin':'10px',
    'verticalAlign':'top',

}),


#LAYOUT-----------------------------------

@app.callback(
    Output('battery', 'children'),
    Output('time', 'children'),
    Input('interval','n_intervals')
)

def updateBattery(n):
    battery = getBattery()
    hrs, min, sec = timeRemaining()

    return f"Battery: {battery}%",f"Time remaining: {hrs}hrs, {min}min, {sec}sec"

    

if __name__ == '__main__':
    app.run(debug=True)
'''