from dash import Dash, html,dcc
from dash.dependencies import Input, Output
import requests
import dash_ag_grid as dag
import pandas as pd

layout = html.Div([
    html.H1('MiR Robot'),

    dcc.Interval(id='interval',interval=2000),

    html.Div(id='battery'),
    html.Div(id='status')
])
