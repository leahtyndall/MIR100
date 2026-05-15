from dash import Dash, html, ctx
import layout.Funcs.network as network, layout.Funcs.subscriber as subscriber
from dash.dependencies import Input, Output
from layout.Funcs.MIRstatus import getBattery, timeRemaining, stateID, getError
import layout.Funcs.missions as missions
import layout.Funcs.networkMap as networkMap
import pandas as pd
import plotly.express as px
import csv
import plotly.graph_objects as go
#import tuya_relay_python.connect_to_relay as relay
import layout.Funcs.basicFunctions as bf
import dash_bootstrap_components as dbc

from layout.layout2 import layout2




app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
 
app.layout = layout2
df = pd.read_csv('networkData.csv')
colourscale = px.colors.named_colorscales()
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
    Output('state','children'),
    #Output('text', 'children'),
    #Output('pending','children'),
    Input('interval-component','n_intervals')
)
def updatemisQue(n):
    state = stateID()
    #text = misText
    return state#, text

@app.callback( #buttons
    Output('container', 'children'),
    #Output('text','children'),
    
    Input('charge', 'n_clicks'),
    Input('cfb1', 'n_clicks'),
    Input('dab1', 'n_clicks'),
    Input('cfb2', 'n_clicks'),
    Input('b2LEFT', 'n_clicks'),
    Input('dab2', 'n_clicks'),
    Input('da', 'n_clicks'),
    Input('marathon', 'n_clicks'),
    Input('clear', 'n_clicks')
    )

def buttonClicked(b1,b2,b3,b4,b5,b6,b7, b8,b9):
    if 'charge' == ctx.triggered_id:
        missions.charge()
        network.taskResponse()
        return 
    elif 'cfb1' == ctx.triggered_id:
        missions.cfb1()
        network.taskResponse()
        return
    elif 'dab1' == ctx.triggered_id:
        missions.dab1()
        network.taskResponse()
        return
    elif 'cfb2' == ctx.triggered_id:
        missions.cfb2()
        network.taskResponse()
        return 
    elif 'b2LEFT' == ctx.triggered_id:
        missions.b2LEFT()
        network.taskResponse()
        return
    elif 'dab2' == ctx.triggered_id:
        missions.dab2()
        network.taskResponse()
        return 
    elif 'da' == ctx.triggered_id:  
        missions.da()
        network.taskResponse()
        return 
    elif 'marathon' == ctx.triggered_id:
        missions.marathon()
        network.taskResponse()
        return
    elif 'clear' == ctx.triggered_id:
        return bf.clearqueue()

@app.callback(
    Output('netstrength', 'children'),
    Input('interval-component','n_intervals')
)
def networkinfo(n):
    strength = network.mullab()
    freq = network.freq()
    return(
        html.P(f'Strength: -{strength} dBm'),
        html.P(f'Frequency: {freq}') 
    )
@app.callback(
    Output('latency', 'children'),
    Input('interval-component','n_intervals')
)
def latencyinfo(n):
    latency, status_code = network.ping()
    return(
        html.P(f'Latency: {latency}ms'),
        html.P(f'Status code: {status_code}')
    )   

@app.callback(
    Output('fps', 'children'),
    Input('interval-component','n_intervals')
)
def stream(n):
    fps = subscriber.getfps()
    return(
        html.P(f'FPS: {fps}')
    )
@app.callback(
    Output('taskLatency', 'children'),
    Input('container', 'children')
)
def taskResponseTime(n):
    time = network.taskResponse()
    return( 
        html.P(f'Time taken = {time}ms')
    )

@app.callback(
    Output('errors', 'children'),
    Input('interval-component', 'n_intervals')
)
def errors(n):
    errors = getError()
    if errors == 67:
        return html.P('No errors!')
    else:
        return html.P(errors)
#'''
@app.callback(
    Output('plot', 'figure'),
    Input('interval-comp2', 'n_intervals')
)

def graph(n):
    networkMap.getData() #uncomment to build network map
    df = pd.read_csv('networkData.csv')
    fig = go.Figure()
    
    #drawing site perimeter
    fig.add_trace(go.Scatter(
        x = [39.850, 41.35, 52.8, 52, 60.85,61.4,58.8,44.35,44.1,52.15,52.8, 70.9, 70.75,70.75, 64.35, 64.95,71.2,70.75, 81.85, 81.3, 77.25, 77.8,70.05,69.65, 39.85],
        y = [52.6, 19.85, 20.2, 40.5,40.75,27.8,22.7,22.05,31.35,31.5, 20.2, 21.3, 40.1,41.15,40.75,24.6,24.6,40.1, 40.35, 56.15, 55.9, 43.85, 43.6, 53.4, 52.6],

        mode='lines',
        #name='Perimeter',
        line=dict(color='red', width = 1),
        line_shape='linear',
        showlegend=False
    ))
    custom_colors = [
        #[0, 'rgba(255, 255, 255, 0)'], 
        
        #[0.1, 'rgba(255, 255, 255, 0)'], 
        [0, "#ec2626"],              
        [0.5, "#d8c731"],              
        [0.9, "#2A71DD"],
        [1.0, 'rgba(255, 255, 255, 0)' ]            
    ]
    #z = df['strength']
    #plotting coords
    fig.add_trace(
        go.Histogram2dContour(
            x=df['x'],
            y=df['y'],
            z = df['strength'],
            histfunc = 'avg',
            colorscale=custom_colors, #[[0, '#fffff]]
            showscale=True,
            #xbins = dict(start=35, end=85, size=3),
            #ybins= dict(start=17, end=56, size=3),
            nbinsx=25,
            nbinsy=20,
            zmin = 25,
            zmax = 75,
            reversescale = True,
            #showlegend=False
            #line=dict(width=0),
            contours_coloring = 'heatmap',
            ncontours =10,
            #text_auto = True
        ), 
    )

    fig.update_layout(
        #plot_bgcolor='white',
        xaxis_title='X coordinate',
        yaxis_title='Y coordinate',
        uirevision='constant',
        #yaxis_scaleanchor='x',
        xaxis = dict(
        tickmode = 'linear',  
        dtick = 5,
    ),
        yaxis=dict(
        tickmode= 'linear',
        dtick=5,
        )
        
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
    #   app.run(host='0.0.0.0', port=8055, debug=False)
