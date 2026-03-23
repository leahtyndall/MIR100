from dash import Dash, html, dcc
import dash_ag_grid as dag
import pandas as pd
from dash.dependencies import Input, Output
from MIRstatus import getBattery, timeRemaining, mapData
import base64


#from layout import layout
#from MIRstatus import df

COLOURS = {
    'navy':'#1f2442',
    'blue': '#a9afd4',
    'backgnd': '#dadded'
}

app = Dash()
#app.layout = layout
#
#app.layout = html.Div(style={'backgroundColor': COLOURS['backgnd']})

app.layout = html.Div(style = {'backgroundColor': COLOURS['backgnd']}, children=[
   
   #title bar
    html.H1('MiR Stats',
        style={
            'color': COLOURS['blue'],
            'width':'100%',
            'padding':'5px',
            'backgroundColor': COLOURS['navy'],
            'borderRadius':'0px',
            'margin':'0px',
            'verticalAlign':'top'
         }),
#status section
    dcc.Interval(id='interval',interval=1000,n_intervals=0),
    html.Div([    
        html.H2('Status'),
        html.P(id= 'battery'),
        html.P(id='time')],
        #other data in this block enter here
            style={
                'color': COLOURS['blue'],
                'width':'20%',
                'padding':'10px',
                'backgroundColor': COLOURS['navy'],
                'borderRadius':'10px',
                'margin':'10px',
                'verticalAlign':'top'}
    ),
    html.Img(src='assets/AllBays.png', 
        style={'width': '100%',
            'width':'50%',
            'padding':'10px',
            'backgroundColor': COLOURS['navy'],
            'borderRadius':'10px',
            'margin':'10px',
            'verticalAlign':'bottom'              
        }),
        #html.Img(src=f"data:image/png;base64,{mapData()}")

])


    #other blocks here




#LAYOUT-----------------------------------

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


if __name__ == '__main__':
    app.run(debug=True)