from dash import Dash, html, dcc, ctx
import layout.Funcs.defs as defs
import dash_ag_grid as dag
import pandas as pd
from dash.dependencies import Input, Output, State
from layout.Funcs.MIRstatus import getBattery, timeRemaining, isAvailable, getNet, misText, modekeystate
import layout.Funcs.CallTo as CallTo
import base64
import dash_bootstrap_components as dbc


#from layout import layout
#from MIRstatus import df
#------------------------------------------
#LAYOUT-----------------------------------
#------------------------------------------
#logic--------------------------------------
COLOURS = { #CHANGE TO VODAFONE THEME + ADD LOGOS
    'red':"#AF1D18",
    'white': "#FFFFFF",
    'backgnd': "#EBEBEB",
    'black': "#1A1A1A",
    'green': '#8FC78F',
    'orange': "#E2870F",
    #'red': "#C52620"
}
COLOURS3 ={'colour'}
if isAvailable() == True:
    COLOURS2 = {'colour': '#8FC78F'}
else:
    COLOURS2 = {'colour': '#AF6A6A' }

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
            'color': COLOURS['red'],
            'width':'100%',
            'padding':'5px',
            #'backgroundColor': COLOURS['red'],
            'borderRadius':'10px',
            'margin':'0px',
            'flex':'1',
            'verticalAlign':'top',
            
         }),
#------------------------status section---------------------------------
    
    
    html.Div([  
          
        html.H2('Status',
            style = {'color': COLOURS['white'],
                'backgroundColor': COLOURS['red'],
                'padding':'10px',
                'borderRadius':'10px',
                'margin':'10px',
                'verticalAlign':'top'}
        ),
        html.P(id= 'battery'),
        html.P(id='time'),
        dcc.Interval(id='interval',interval=1*1000,n_intervals=0)], 
        #other data in this block enter here
            style={
                'color': COLOURS['black'],
                'width':'22%',
                'padding':'10px',
                'backgroundColor': COLOURS['white'],
                'borderRadius':'10px',
                'margin':'10px',
                'verticalAlign':'top',
                'display': 'inline-block'
                } 
    ),
 #----------------mission queue-----------------------------
        html.Div([ 
            html.H2('Mission Queue', 
                style = {'color': COLOURS['white'],
                    'backgroundColor': COLOURS['red'],
                    'padding':'10px',
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top'},
            ),
            #html.P('Executing: '),
            html.P(id = 'text'),
            html.P(id = 'pending')], 
                style={
                    'color': COLOURS['black'],
                    'width':'22%',
                    'padding':'10px',
                    'backgroundColor': COLOURS['white'],
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top',
                    'display': 'inline-block'},
            
        ), 
#------------TASKS LIST-------------------------------------------
        html.Div([
            html.H1(id = 'state', 
                style={
                    'color': COLOURS2['colour'],
                    'padding':'10px',
                    'backgroundColor': COLOURS['red'],
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top'}
            ),
            html.H3('Call to:',
                style = {'color': COLOURS['red'],
                    'backgroundColor': COLOURS['white'],
                    'padding':'10px',
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top'},
                    ),
            dcc.Button('Leahs Desk', id = 'mydesk', n_clicks = 0),
            dcc.Button('Dock', id = 'dock', n_clicks = 0),
            dcc.Button('Pick up',id = 'pick', n_clicks = 0 ),
            dcc.Button('Place down', id='place', n_clicks = 0),
            html.Div(id ='container', children = '')],

                style={
                    'color': COLOURS['black'],
                    'width':'20%',
                    'padding':'10px',
                    'backgroundColor': COLOURS['white'],
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top',
                    'display': 'inline-block'}),    
    html.Div([
        html.H2('Network', 
            style = {'color': COLOURS['white'],
                    'backgroundColor': COLOURS3['colour'],
                    'padding':'10px',
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top'},
        )],
        
            style={
                    'color': COLOURS['red'],
                    'width':'15%',
                    'padding':'10px',
                    'backgroundColor': COLOURS['white'],
                    'borderRadius':'10px',
                    'margin':'10px',
                    'verticalAlign':'top',
                    'display': 'inline-block'}
        ), 
    
#---------------map------------------------------------------------
        html.Div([ 
            html.Img(src='assets/AllBays.png', 
                style={'width': '100%',
                    'width':'45%',
                    'padding':'10px',
                    'backgroundColor': COLOURS['red'],
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
    Input('interval','n_intervals')
)
def updateBattery(n):
    battery = getBattery()
    hrs, min, sec = timeRemaining()    

    return(
        f"Battery: {battery}%",
        f"Time remaining: {hrs}hrs, {min}mins, {sec}secs",
       )

@app.callback(
        Output('text','children'),
        Output('state', 'children'),
        #Output('pending','children'),
        Input('interval','n_intervals')
)

def updatemisQue(n):
    text = misText()
    state = modekeystate()
    return text, state
  

@app.callback( #buttons
    Output('container', 'children'),
    
    Input('mydesk', 'n_clicks'),
    Input('pick', 'n_clicks'),
    Input('place', 'n_clicks')
    #Input('dock', 'n_clicks'),
    #State('inputOnClick', 'id')
)
def buttonClicked(b1,b2,b3):
    if 'mydesk' == ctx.triggered_id:
        return CallTo.doMission(defs.LeahsDesk)


    elif 'pick' == ctx.triggered_id:
        return defs.pick()
    elif 'place' == ctx.triggered_id:
        return defs.place()


if __name__ == '__main__':
    app.run(debug=True)