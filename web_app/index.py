from dash.dependencies import Input, Output
import pickle
import dash_core_components as dcc
import dash_html_components as html

import sys
sys.path.append('/Users/jarvis/Desktop/CODE/sadrat')

import plotly.graph_objs as go
import plotly
import chart_studio
import pandas as pd


# TODO: Load Pickle file for dropdown city options [DONE]
with open ("/Users/jarvis/Desktop/CODE/sadrat/web_app/appdata/options.pickle","rb") as file:
    options = pickle.load(file)
file.close()

# setting user, api key and access token for plotly and mapbox
chart_studio.tools.set_credentials_file(username='shaswat_lenka', api_key='oU5UoiMtKckyNa2f2ErI')
mapbox_access_token = 'pk.eyJ1Ijoic2hhc3dhdGxlbmthIiwiYSI6ImNrNW1zaWc0aTB6eGQza3FrbWd6d2M2N3AifQ.VFSQzSMQHRZHyT8eqT-uOw'

from web_app.app import app, server

style = {'maxWidth': '960px', 'margin': 'auto'}
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H5(
        children='SADRAT v1.0.0',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),
    dcc.Dropdown(
        id="cities",
        options=options,
        value="NA NA"
    ),

    html.Div(id='output-container',
    style={
            'textAlign': 'left',
            'color': colors['text']
        }
             )
])

@app.callback(
     Output('output-container', 'children'),
    [Input('cities', 'value')]
)

def update_output(value):
    value_array = value.split()
    return "latitude = " + value_array[0]+ " longitude = " + value_array[1]

if __name__ == '__main__':
    app.run_server(debug=True)