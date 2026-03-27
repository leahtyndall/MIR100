from dash import Dash, html, dcc, ctx
import defs
import dash_ag_grid as dag
import pandas as pd
from dash.dependencies import Input, Output, State
from MIRstatus import getBattery, timeRemaining, isAvailable, getNet, misText, modekeystate
import CallTo
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
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#################################################################    
#Title bar         
#################################################################    
app.layout = html.Div(
    style = {'backgroundColor': COLOURS['backgnd'],'font-family':'Monospace'}, children= [ 
    
    
    dbc.Container([  
        dbc.Row([#title bar - row 1
            dbc.Col(html.Div([ #r1c1
                html.H1('MiR Stats',
                    style={
                        'color': COLOURS['black'],
                        'width':'100%',
                        'padding':'5px',
                        #'backgroundColor': COLOURS['red'],
                        'borderRadius':'10px',
                        'margin':'0px',
                        'verticalAlign':'top'})
            ]), width = 8),

            dbc.Col(html.Div([ # r1c2
                html.Img(src='assets/IMR-Primary Logo_RGB.png',
                    style ={'width': '100%',
                        'verticalAlign':'top', 
                        'float':'right',
                        'margin':'0px'})
            ]), width = 2),               
            dbc.Col(html.Div([ #r1c3
                html.Img(src='assets/vodafone.png',
                    style ={'width': '60%',
                        'verticalAlign':'top', 
                        'float':'right',
                        'margin':'0px'})
            ]), width = 2)
        ]), #row2
  #fine^
#################################################################    
#LEFT COL         
#################################################################      
# #1st column------------------------------------
                
        dbc.Row([ #row 4                  
            dbc.Col(html.Div([     #left left            
                html.H2('Status',
                    style = {'color': COLOURS['white'],
                        'backgroundColor': COLOURS['red'],
                        'padding':'10px',
                        'borderRadius':'10px',
                        'margin':'0px',
                        'verticalAlign':'top'}),
                html.P(id= 'battery'),
                html.P(id='time'),
                dcc.Interval(id='interval',interval=1*1000,n_intervals=0)], 
                #other data in this block enter here
                    style={
                        'color': COLOURS['black'],
                        'width':'100%',
                        'padding':'10px',
                        'backgroundColor': COLOURS['white'],
                        'borderRadius':'10px',
                        'margin':'0px',
                        'verticalAlign':'top',
                        'display': 'inline-block'})),
#fine^
#----------------mission queue-----------------------------(middle column)
            dbc.Col(html.Div([ #right left
                html.H2('Mission Queue', 
                    style = {'color': COLOURS['white'],
                        'backgroundColor': COLOURS['red'],
                        'padding':'10px',
                        'borderRadius':'10px',
                        'margin':'0px',
                        'verticalAlign':'top'}),
                #html.P('Executing: '),
                html.P(id = 'text'),
                html.P(id = 'pending')], 
                    style={
                        'color': COLOURS['black'],
                        'width':'100%',
                        'padding':'10px',
                        'backgroundColor': COLOURS['white'],
                        'borderRadius':'10px',
                        'margin':'0px',
                        'verticalAlign':'top',
                        'display': 'inline-block'}
                )),

        ]), #row 4
#fine^
            dbc.Row([ #row 5
                dbc.Col(html.Div([ #col 3
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
                    html.Div(id ='container', children = '')
                ], #col 3

                        style={
                            'color': COLOURS['black'],
                            'width':'100%',
                            'padding':'10px',
                            'backgroundColor': COLOURS['white'],
                            'borderRadius':'10px',
                            'margin':'10px',
                            'verticalAlign':'top',
                            'display': 'inline-block'}
                )), #col 3

            dbc.Col( #right half col
                html.Div([ 
                    html.Img(src='assets/AllBays.png', 
                        style={'width': '100%',
                            'width': '100%',
                            'padding':'10px',
                            'backgroundColor': COLOURS['red'],
                            'borderRadius':'10px',
                            'margin':'10px',
                            'verticalAlign':'top',
                            'display': 'inline-block'})])
            )

            ])#row 5
    ])
])

#################################################################    
#RIGHT COL         
#################################################################            
            






 

#------------------------status section---------------------------------

#----------------mission queue-----------------------------
#------------TASKS LIST-------------------------------------------
#---------------map------------------------------------------------  
    



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
        #Output('state', 'children'),
        #Output('pending','children'),
        Input('interval','n_intervals')
)

def updatemisQue(n):
    text = misText()
    state = modekeystate()
    return text, state


if __name__ == '__main__':
    app.run(debug=True)