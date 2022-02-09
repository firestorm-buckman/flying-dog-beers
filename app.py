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

########### Set up the layout
df = px.data.tips()# Build App
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)
#app = dcc.Dash(__name__)
app.title = "Avocado Analytics: Understand Your Avocados!"

app.layout =  html.Div(
    children=[
        html.H1(children="Avocado Analytics",),
        html.P(
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018",
        ),
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
    ]
)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server()
