from dash import dcc
import pandas as pd
import plotly.express as px
from layout.Funcs.API import APImir
import layout.Funcs.rosDiagnostics as ros
import csv
import time
import layout.Funcs.network as network


colours = {
    'excellent':"#2BC1D4",
    'good':"#44A744",
    'weak':"#ECB246",
    'dead':"#BD2D23"
}

#retrives location data from mir, and signal level from rosDiagnostics() and maps into a CSV file to be read by graph function in dashboard.py
def getData():
    #print('getting data')
    coords = APImir.mirRequest('GET', '/status').get('position')
    state = APImir.mirRequest('GET', '/status').get('state_text')
    x= coords.get('x')
    y= coords.get('y')

    signallevel = ros.getsignal()
    #print(x,y) 
    #print(strength)
    fields=['x','y','signallevel']
    data = [
        #['x','y','strength'],
        {'x':x,'y':y,'signallevel':signallevel}
    ]
    if state != 'Pause':
        with open('layout/assets/networkData.csv', mode = 'at', newline='') as d:
            writer = csv.DictWriter(d, fieldnames=fields)
            writer.writerows(data)
            d.close()
    return
