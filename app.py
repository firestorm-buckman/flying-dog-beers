#Installing specific packages.
!pip install -q dash==1.19.0
!pip install -q jupyter_dash==0.3.0

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from jupyter_dash import JupyterDash
import plotly.express as px
from dash.dependencies import Input, Output, State# Load Data
from dash.exceptions import PreventUpdate
import dash_table
import pandas as pd
import numpy as np

########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": [1, 2, 3],
                        "y": [2, 3, 4],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": [1, 2, 3],
                        "y": [1, 3, 5],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
