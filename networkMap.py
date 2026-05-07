from dash import dcc
import pandas as pd
import plotly.express as px
import APImir
import csv
import time
import network

mulLab = '4d5efe2a-f6c3-d3fe-556f-077cd8313b0c'

colours = {
    'excellent':"#2BC1D4",
    'good':"#44A744",
    'weak':"#ECB246",
    'dead':"#BD2D23"
}

def getData():
    #print('getting data')
    coords = APImir.mirRequest('GET', '/status').get('position')
    x= coords.get('x')
    y= coords.get('y')
    
    strength = network.mullab()
    #print(x,y) 
    #print(strength)
    fields=['x','y','strength']
    data = [
        #['x','y','strength'],
        {'x':x,'y':y,'strength':strength}
    ]

    with open('networkData.csv', mode = 'at', newline='') as d:
        writer = csv.DictWriter(d, fieldnames=fields)
        writer.writerows(data)
        d.close()

    return
'''
def plot():
    i = 0
    getData()
    #time.sleep(2)
    with open('networkData.csv', mode = 'r') as d:
        df = pd.read_csv(d)
        reader = csv.reader(d)
        next(reader,None) #skip header
        for row in reader:
            fig = px.scatter(df, x='x_column',y='y_column', title='plot')
            fig.update_traces(marker=dict(size=10, color='red', symbol='circle'))
            fig.show()

        
            return fig'''

