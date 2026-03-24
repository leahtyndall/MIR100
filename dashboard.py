from dash import Dash, html, dcc, ctx
import misID
import dash_ag_grid as dag
import pandas as pd
from dash.dependencies import Input, Output, State
from MIRstatus import getBattery, timeRemaining, mapData, isAvailable,getNet
import CallTo
import base64


#from layout import layout
#from MIRstatus import df
#------------------------------------------
#LAYOUT-----------------------------------
#------------------------------------------
#logic--------------------------------------
COLOURS = {
    'navy':'#1f2442',
    'blue': '#a9afd4',
    'backgnd': '#dadded',
    'green': '#8FC78F',
    'orange': "#C7B38F",
    'red': "#AF6A6A"
}
COLOURS3 ={'colour'}
if isAvailable() == True:
    COLOURS2 = {'colour': '#8FC78F'}
else:
    COLOURS2 = {'colour': '#C78F8F' }

if getNet() == 1:
    netStat = 'Connected'
    COLOURS3 = {'colour': '#8FC78F'}
if getNet() == 2:
    netStat = 'Error'
    COLOURS3 = {'colour': "#C7B38F"}
if getNet() == 3:
    netStat = 'Offline'
    COLOURS3 = {'colour': '#AF6A6A'}
#-----------------------------------------
app = Dash()

app.layout = html.Div(
    style = {'backgroundColor': COLOURS['backgnd']

        }, children=[ 
   #title bar
    html.H1('MiR Stats',
        style={
            'color': COLOURS['blue'],
            'width':'100%',
            'padding':'5px',
            'backgroundColor': COLOURS['navy'],
            'borderRadius':'0px',
            'margin':'0px',
            'flex':'1',
            'verticalAlign':'top',
            
         }),
#------------------------status section---------------------------------
    dcc.Interval(id='interval',interval=1000,n_intervals=0),
    
    html.Div([    
        html.H2('Status',
            style = {'color': COLOURS['navy'],
                'backgroundColor': COLOURS['blue'],
                'padding':'10px',
                'borderRadius':'10px',
                'margin':'10px',
                'verticalAlign':'top'}
        ),
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
                'verticalAlign':'top',
                'display': 'inline-block'
                } 
    ),
 #----------------mission queue-----------------------------
        html.Div([ 
            html.H2('Mission Queue', 
                style = {'color': COLOURS['navy'],
                    'backgroundColor': COLOURS['blue'],
                    'padding':'10px',
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top'},
            ),
            html.P('**add data of mission queue**')], #id = 'mis names
                style={
                    'color': COLOURS['blue'],
                    'width':'20%',
                    'padding':'10px',
                    'backgroundColor': COLOURS['navy'],
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top',
                    'display': 'inline-block'}
        ), 
#------------TASKS LIST-------------------------------------------
        html.Div([
            html.H1('Available?', 
                style={
                    'color': COLOURS['navy'],
                    'padding':'10px',
                    'backgroundColor': COLOURS2['colour'],
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top'}
            ),
            html.H2('Call to:',
                style = {'color': COLOURS['navy'],
                    'backgroundColor': COLOURS['blue'],
                    'padding':'10px',
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top'},
                    ),
            dcc.Button('Leahs Desk', id = 'mydesk', n_clicks = 0),
            dcc.Button('Dock', id = 'dock', n_clicks = 0),

            html.P('test'),
            html.P('test'),
            html.P('test')],
                style={
                    'color': COLOURS['blue'],
                    'width':'20%',
                    'padding':'10px',
                    'backgroundColor': COLOURS['navy'],
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top',
                    'display': 'inline-block'}
        ),    
    html.Div([
        html.H2('Network', 
            style = {'color': COLOURS['navy'],
                    'backgroundColor': COLOURS['blue'],
                    'padding':'10px',
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top'},
        ),
        html.P('')],
            style={
                    'color': COLOURS['blue'],
                    'width':'20%',
                    'padding':'10px',
                    'backgroundColor': COLOURS['navy'],
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top',
                    'display': 'inline-block'}
        ), 
    
#---------------map------------------------------------------------
        html.Div([ 
            html.Img(src='assets/AllBays.png', 
                style={'width': '100%',
                    'width':'43%',
                    'padding':'10px',
                    'backgroundColor': COLOURS['navy'],
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top',
                    'display': 'inline-block'}
            ),
        #html.Img(src=f"data:image/png;base64,{mapData()}")
        ]),
        
    
])


    #other blocks here
#------------------------------------------
#callbacks-----------------------------------
#------------------------------------------
#import callbacks

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
        f"Time remaining: {hrs}hrs, {min}mins, {sec}secs"
       )

@app.callback(
    #Output('Moving', 'children'),
    Input('mydesk', 'n_clicks'),
    #Input('dock', 'n_clicks'),
    #State('inputOnClick', 'id')
)
def buttonClicked(n_clicks):
    if 'mydesk' == ctx.triggered_id:
        id = misID.LeahsDesk
    return CallTo.doMission(id)

#def updateQ(n)
    #queue = 
    #return 

if __name__ == '__main__':
    app.run(debug=True)