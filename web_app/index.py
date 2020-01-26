import sys
sys.path.append('/Users/jarvis/Desktop/CODE/sadrat')


from dash.dependencies import Input, Output
import pickle
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
#import plotly.graph_objs as go
#import plotly
import chart_studio
#import pandas as pd


# TODO: Load Pickle file for dropdown city options [DONE]
with open ("/Users/jarvis/Desktop/CODE/sadrat/web_app/appdata/options.pickle","rb") as file1:
    options = pickle.load(file1)
file1.close()


# setting user, api key and access token for plotly and mapbox

chart_studio.tools.set_credentials_file(username='shaswat_lenka', api_key='oU5UoiMtKckyNa2f2ErI')
mapbox_access_token = 'pk.eyJ1Ijoic2hhc3dhdGxlbmthIiwiYSI6ImNrNW1zaWc0aTB6eGQza3FrbWd6d2M2N3AifQ.VFSQzSMQHRZHyT8eqT-uOw'

from web_app.app import app, server
from web_app.watchman_test import gettweet
from web_app.utilities.bounding_box import get_bounding_box

colors = {
    'background': '#00000',
    'text': '#7FDBFF'
}

text_style_common = {
            'textAlign': 'left',
            'color': colors['text']
        }

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
dbc.NavbarSimple(
    children=[],
    brand="SADRAT v1.0.0 DEMO",
    brand_href="#",
    sticky="top",
    color="dark"
),
    html.Br(),
    html.Div([
    dbc.Row(dbc.Col(
    html.Div([
    html.H6(
        children="Select Location",
        style={
            'textAlign': "left",
            'color': colors['text']
        }
    ),
    dcc.Dropdown(
        id="cities",
        options=options,
        value="0.00 0.00",
        style={
        'color': "black"
        }
    )
    ]),width=4))
    ]),

    html.Div(id='output-container',

    style=text_style_common
             ),

    html.Br(),

    html.Div([
        dbc.Row(
            dbc.Col(
                html.Div([
                    html.H6(
                        children="Recent Tweets:",
                        style=text_style_common
                    ),
                    html.Div(
                        id='tweets-display-container'
                    )
                ]), width=4
            )
        )
    ])

])


@app.callback(
     Output('output-container', 'children'),
    [Input('cities', 'value')]
)
def update_output(value):
    value_array = value.split()
    return "latitude = " + value_array[0]+ " longitude = " + value_array[1]


@app.callback(
    Output('tweets-display-container', 'children'),
    [Input('cities', 'value')]
)
def update_recent_tweets(value):
    value_arr = value.split()
    half_side_in_miles = 50
    bounding_box = get_bounding_box(float(value_arr[0]), float(value_arr[1]), half_side_in_miles)
    tweet = gettweet(bounding_box.lat_max, bounding_box.lat_min, half_side_in_miles)
    return tweet


if __name__ == '__main__':
    app.run_server(debug=True)