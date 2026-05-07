from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
import dash_player
import plotly.graph_objects as go

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

layout2 = html.Div(
    style = {'backgroundColor': COLOURS['backgnd'],'font-family':'Arial', 'font-size':'18px', 'line-height':'1','wdth':'100%', 'height':'100vh'}, children= [
        dcc.Tabs(style = {'height':'40px'}, children = [
            dcc.Tab(label='Dashboard', children=[
                dbc.Container([  
                    dbc.Row([#title bar - row 1
                        dbc.Col(html.Div([ #r1c1
                            html.H1('MiR100',
                                style={
                                    'color': COLOURS['black'],
                                    'width':'100%',
                                    'padding':'5px',
                                    #'backgroundColor': COLOURS['red'],
                                    'borderRadius':'5px',
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

                    ],   
                    style = {
                        'backgroundColor': COLOURS['white'],
                        'width':'100%',
                        'box-shadow':'5px 5px 5px grey'
                        }
                    ), #row1 close
                    #################################################################    
                    #LEFT COL         
                    #################################################################      
                            
                    dbc.Row([ #row 2 open                
                        dbc.Col( #r2c1
                            dbc.Row([ #inside r2c1
                                dbc.Col(html.Div([  #LEFT r2c1          
                                    html.H4('Robot Status:',
                                        style = {
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px'}),

                                        html.Div(id= 'battery'),
                                        html.Div(id='time')],
                                    #other data in this block enter here
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'10px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '150px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }
                                )),

                                dbc.Col(html.Div([ #r2c1c2 
                                    html.H4('Current State:', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px'
                                        }),
                                    #html.P('Executing: '),
                                    html.P(id = 'state'),
                                    html.P(id = 'text')], 
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'10px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '150px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }
                                )),
                            
                            dbc.Row([ #R2c1r2 {middle}
                                dbc.Col(html.Div([ #col 3
                                    html.H3('Tasks:', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top'
                                            }
                                    ),
                                    
                                            
                                    dcc.Button('Go to charger', id = 'charge', n_clicks = 0, style={'color':COLOURS['black'], 'outline':COLOURS['black']}),
                                    dcc.Button('Collect from B1', id = 'cfb1', n_clicks = 0, style={'color':COLOURS['black']}),
                                    dcc.Button('Deposit at B1',id = 'dab1', n_clicks = 0, style={'color':COLOURS['black']} ),
                                    dcc.Button('Collect from B2', id='cfb2', n_clicks = 0, style={'color':COLOURS['black']}),
                                    dcc.Button('Deposit at B2', id='dab2', n_clicks = 0, style={'color':COLOURS['black']}),
                                    dcc.Button('Dashboard Area', id='da', n_clicks = 0, style={'color':COLOURS['black']}),
                                    dcc.Button('Left side of B2', id ='b2LEFT', n_clicks = 0, style={'color':COLOURS['black']}),
                                    dcc.Button('Marathon', id ='marathon', n_clicks = 0, style={'color':COLOURS['black']}),
                                    dcc.Button('Clear Queue', id ='clear', n_clicks = 0, style={'color':COLOURS['black']}),

                                    html.Div(id ='container', children = '')], 

                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'10px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '180px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }
                                )) #r2c1r2 close                
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([ #col 3
                                    html.H3('Errors: ',
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top'
                                            }
                                    ),

                                    html.P(id = 'errors')],

                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'10px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '180px',
                                            'box-shadow':'5px 5px 5px grey'
                                        }
                                    


                                ))


                            ])
                            ])
                        ),
                    #################################################################    
                    #map
                    #################################################################            
                        dbc.Col( #r2c2 MAP
                            html.Div([ 
                                html.Img(src='http://192.168.30.100:8080/stream?topic=/image_raw&type=ros_compressed', 
                                    style={'width': '100%',
                                        'width': '100%',
                                        'padding':'10px',
                                        'backgroundColor': COLOURS['red'],
                                        'borderRadius':'10px',
                                        'margin':'10px',
                                        'verticalAlign':'top',
                                        'display': 'inline-block',
                                        'box-shadow':'5px 5px 5px grey'})])
                        ) #r2c2 close

                    ]),
                ]),

            ]),
############################################################################################  
# TAB 2
############################################################################################ 
            dcc.Tab(label='Info', children=[
                dbc.Container([  
                    dbc.Row([#title bar - row 1
                        dbc.Col(html.Div([ #r1c1
                            html.H1('MiR100',
                                style={
                                    'color': COLOURS['black'],
                                    'width':'100%',
                                    'padding':'5px',
                                    #'backgroundColor': COLOURS['red'],
                                    'borderRadius':'5px',
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

                    ],   
                    style = {
                        'backgroundColor': COLOURS['white'],
                        'width':'100%',
                        'box-shadow':'5px 5px 5px grey'
                        }

                    ), #row1 close
                    #fine^
                    #################################################################    
                    #LEFT COL         
                    #################################################################      
                            
                    dbc.Row([ #row 2 open                
                        dbc.Col( #r2c1
                            dbc.Row([ #inside r2c1
                                dbc.Col(html.Div([  #LEFT r2c1          
                                    html.P('Status response:', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px',
                                            }),
                                    #html.P('Executing: '),
                                    html.P(id = 'latency')],
                                    #html.P(id = '')], 
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'20px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '120px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }                                   #other data in this block enter here

                                )),

                                dbc.Col(html.Div([ #r2c1c2 
                                    html.P('Average stream rate: ', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px'}),
                                    #html.P('Executing: '),
                                    html.P(id = 'fps')],
                                    #html.P('Delay: ~4-5ms')],
                                    #html.P(id = '')], 
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'20px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '120px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }  
                            

                                )),
                            
                            dbc.Row([ #R2c1r2 {middle}
                                dbc.Col(html.Div([ #col 3
                                    html.P('Task response: ', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px'
                                        }
                                    ),
                                    #html.P('Executing: '),
                                    html.P(id = 'taskLatency'),
                                    html.P('')],

                                         style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'20px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '120px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }           
                                )) #r2c1r2 close                
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([ #col 3
                                    html.P('Network:', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'5px',
                                            'verticalAlign':'top',
                                            'height':'40px'
                                        }
                                    ),
                                        html.Div(id = 'netstrength')],
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin':'20px',
                                            'verticalAlign':'top',
                                            'display': 'inline-block',
                                            'height': '120px',
                                            'box-shadow':'5px 5px 5px grey'
                                        }    
                                ))


                            ])
                            ])
                        ),
                    #################################################################    
                    #RIGHT COL         
                    #################################################################            
                        dbc.Col( #r2c2 MAP
                            html.Div([ 
                                dcc.Graph(id='plot'),
                                dcc.Interval(id='interval-comp2', interval = 6*1000, n_intervals = 0)
                            ])
                        ) #r2c2 close

                
                    ]),
        

                ]),


            ]),#row 5
            dcc.Tab(label='Project Summary',children =[
                dbc.Container([
                    dbc.Row([#title bar - row 1
                        dbc.Col(html.Div([ #r1c1
                            html.H1('MiR100',
                                style={
                                    'color': COLOURS['black'],
                                    'width':'100%',
                                    'padding':'5px',
                                    #'backgroundColor': COLOURS['red'],
                                    'borderRadius':'5px',
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

                    ],   
                    style = {
                        'backgroundColor': COLOURS['white'],
                        'width':'100%',
                        'box-shadow':'5px 5px 5px grey'
                        }

                    ), #row1 close
                    #################################################################    
                    #LEFT COL         
                    #################################################################      
                            
                    dbc.Row([ #row 2 open                
                        dbc.Col( #r2c1
                            dbc.Row([ #inside r2c1
                                dbc.Col(html.Div([  #LEFT r2c1          
                                    html.H2('Overview', 
                                        style={
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'width':'14%',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            #'verticalAlign':'top',
                                            'height':'50px'}),
                                    #html.P('Executing: '),
                                    html.P('This project demonstrates the use of mobile robots to automate delivery tasks '
                                    'in an industrial/manufacturing enviornment. ' \
                                    'Our MiR100 robot is equipped with an automated shelf pickup system, and communication' \
                                    ' with external gates, allowing it to deliver cargo between bays, with no human interaction. ' \
                                    'A user simply orders the robot to the desired location via its custom dashboard, and its ' \
                                    'programming handles the rest. The Dashboard brings all of the robots information into one ' \
                                    'easily accessible location. As well as control, it provides real time monitoring of the MiR, ' \
                                    'including - status updates, network speeds and an egocentric live-stream. ')],
                                    #html.P(id = '')], 
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'98%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin-top':'20px',
                                            'verticalAlign':'top',
                                            'word-spacing':'3px',
                                            'line-height':'1.3',
                                            'display': 'inline-block',
                                            'height': '200px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }                                   #other data in this block enter here

                                )),

                                
                            
                            dbc.Row([ #R2c1r2 {middle}
                                dbc.Col(html.Div([ #col 3
                                    html.H2('Network', 
                                        style={
                                            'width':'12%',
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'height':'50px'}),
                                    html.P('The main objective of this project is to showcase a precise benchmark comparison between ' \
                                    'telecommunication speeds over Wi-Fi networks and Vodafones 5G Mobile Private Network. With ' \
                                    'autonomous robots, having fast network speeds is the key to automation - especially in a busy ' \
                                    'working enviornement where real-time feedback is essential. Standard Wi-Fi networks alone may keep ' \
                                    'up with the robots demands. By gathering latency and bandwidth data from both Wi-Fi and Vodafones 5G ' \
                                    'MPN, we will measure the definitive contrast of the twos capabilties.' \
                                    )],
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin-top':'20px',
                                            'verticalAlign':'top',
                                            'word-spacing':'3px',
                                            'line-height':'1.3',
                                            'display': 'inline-block',
                                            'height': '180px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }                                 



                                )) #r2c1r2 close                
                            ]),
                            dbc.Row([ #R2c1r2 {middle}
                                dbc.Col(html.Div([ #col 3
                                    html.H2('Robots in the Workplace', 
                                        style={
                                            'width':'31%',
                                            'color': COLOURS['white'],
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['red'],
                                            'borderRadius':'10px',
                                            'margin':'10px',
                                            'verticalAlign':'top',
                                            'height':'50px'}),
                                    html.P('The demo gives in insight as to what robot - human interaction could look like in the ' \
                                           'workplace. When implemented correctly, and tailored to the specific ask, automation can ' \
                                           'cause an exponetial increase in efficiency. However - it all goes back to the question - ' \
                                           'what network to best to manage this technology?')],
                                        style={
                                            'color': COLOURS['black'],
                                            'width':'100%',
                                            'padding':'8px',
                                            'backgroundColor': COLOURS['white'],
                                            'borderRadius':'10px',
                                            'margin-top':'20px',
                                            'verticalAlign':'top',
                                            'word-spacing':'3px',
                                            'line-height':'1.3',
                                            'display': 'inline-block',
                                            'height': '180px',
                                            'box-shadow':'5px 5px 5px grey'
                                            }                                 



                                )) #r2c1r2 close                
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([ #col 3

                                ]))


                            ])
                            ])
                        ),
                    #################################################################    
                    #RIGHT COL         
                    #################################################################            

                
                    ]),
        

                ]),
                ])

            ]),
        dcc.Interval(
            id='interval-component',
            interval=2*1000,
            n_intervals=0),

       



])