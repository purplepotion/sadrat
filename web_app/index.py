import sys
sys.path.append('/Users/jarvis/Desktop/CODE/sadrat')


from dash.dependencies import Input, Output, State
import pickle
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
#import plotly.graph_objs as go
#import plotly
import chart_studio
import pandas as pd
import  random

# TODO: Load Pickle file for dropdown city options [DONE]
with open ("/Users/jarvis/Desktop/CODE/sadrat/web_app/appdata/options.pickle","rb") as file1:
    options = pickle.load(file1)
file1.close()

# setting user, api key and access token for plotly and mapbox

chart_studio.tools.set_credentials_file(username='shaswat_lenka', api_key='oU5UoiMtKckyNa2f2ErI')
mapbox_access_token = 'pk.eyJ1Ijoic2hhc3dhdGxlbmthIiwiYSI6ImNrNW1zaWc0aTB6eGQza3FrbWd6d2M2N3AifQ.VFSQzSMQHRZHyT8eqT-uOw'
mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"

from web_app.app import app, server
from web_app.utilities.bounding_box import get_bounding_box
from web_app.utilities.live_tweets import obj_func
from web_app.models.disease_prediction import disease_from_tweet

colors = {
    'background': '#00000',
    'text': '#7FDBFF'
}

#colorscale for map
DEFAULT_COLORSCALE = [
    "#f2fffb",
    "#bbffeb",
    "#98ffe0",
    "#79ffd6",
    "#6df0c8",
    "#69e7c0",
    "#59dab2",
    "#45d0a5",
    "#31c194",
    "#2bb489",
    "#25a27b",
    "#1e906d",
    "#188463",
    "#157658",
    "#11684d",
    "#10523e",
]

BINS = [
    "1-2",
    "3-4",
    "4-5",
    "6-7",
    "8-9",
    "10-11",
    "12-13",
    "14-15",
    "16-17",
    "18-19",
    "20-21",
    "22-23",
    "24-25",
    "26-27",
    "28-29",
    ">30"
]

DEFAULT_OPACITY = 0.8


text_style_common = {
            'textAlign': 'left',
            'color': colors['text']
        }

# import dataset
df = pd.read_csv("/Users/jarvis/Desktop/CODE/sadrat/web_app/appdata/adrmine_tweets_with_locations.csv")
latitudes = df["latitude"]
longitudes = df["longitude"]

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
dbc.NavbarSimple(
    children=[],
    brand="SADRAT v1.0.0 DEMO",
    brand_href="#",
    sticky="top",
    color="dark"
),
    html.Br(),
    html.H5(
        children="Disease Trend Analysis and ADR Metrics",
        style={
            'color':'#FF8364',
            'textAlign': "center"
        }
    ),
    html.Br(),
    html.Div([
    dbc.Row([
        dbc.Col(
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
            value="12.986865 77.580994",
            style={
            'color': "black"
            }
        ),
        html.Div(id='output-container',

            style=text_style_common
                     ),

            html.Br(),

            html.Div([
                html.H6(
                    children="Recent Tweets:",
                    style=text_style_common
                ),
                dbc.Alert(
                    id='fetching-message',
                    color='info'
                ),

            html.Div([
            dcc.Textarea(id='tweet',
                placeholder='No tweet found',
                value='',
                style={'width': '100%',
                       'color':'rgba(34,34,34,1)'
                       }
                ),
            html.Button('Refresh', id='button'),
                 ]),
                html.Div([
                 html.Br(),
                    html.P("Detected diseases/conditions: ", style={"color": colors['text']}),
                    dbc.Alert(id = "detected-diseases",color="success")
                ]),
                html.Div([
                 html.Br(),
                    html.P("ADR Probability: ", style={"color": colors['text']}),
                    dbc.Alert(id="adr-proba",color="success")
                ])
            ]),

    ]), width=4),

    dbc.Col(
    html.Div(
        id="heatmap-container",
        children=[
            html.P("Choropleth map of Disease Trends from streamed tweets",
                   id="heatmap-title",
                   style={
                       'textAlign':'center'
                   }),

            dcc.Graph(
                id="country-choropleth",
                figure=dict(
                    data=[
                        dict(
                            lat=latitudes,
                            lon=longitudes,
                            # text=df_lat_lon["Hover"],
                            type="scattermapbox",
                        )
                    ],
                    layout=dict(
                        paper_bgcolor="rgba(34,34,34,1)",
                        mapbox=dict(
                            layers=[],
                            accesstoken=mapbox_access_token,
                            style=mapbox_style,
                            center=dict(
                                lat=38.72490, lon=-95.61446
                            ),
                            pitch=0,
                            zoom=3.5,
                        ),
                        autosize=True,
                    ),
                ),
            ),

    ]),width=8)])
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
    Output('fetching-message', 'children'),
    [Input('cities', 'value')]
)
def update_recent_tweets(value):
    value_arr = value.split()
    half_side_in_miles = 50
    bb_coordinates = get_bounding_box(float(value_arr[0]), float(value_arr[1]), half_side_in_miles)
    obj_func([bb_coordinates.lon_min, bb_coordinates.lat_min,bb_coordinates.lon_max, bb_coordinates.lat_max])
    return "fetching recent tweets at 50 miles radius from {}...".format(value)


# display map
@app.callback(
    Output("country-choropleth", "figure")
)
def display_map(figure):
    cm = dict(zip(BINS, DEFAULT_COLORSCALE))

    data = [
        dict(
            lat=latitudes,
            lon=longitudes,
            # text=df_lat_lon["Hover"],
            type="scattermapbox",
            # hoverinfo="text",
            marker=dict(size=5, color="white", opacity=0),
        )
    ]

    annotations = [
        dict(
            showarrow=False,
            align="right",
            text="test-text-to-be-replaced",
            font=dict(color="#2cfec1"),
            bgcolor="#1f2630",
            x=0.95,
            y=0.95,
        )
    ]

    for i, bin in enumerate(reversed(BINS)):
        color = cm[bin]
        annotations.append(
            dict(
                arrowcolor=color,
                text=bin,
                x=0.95,
                y=0.85 - (i / 20),
                ax=-60,
                ay=0,
                arrowwidth=5,
                arrowhead=0,
                bgcolor="#1f2630",
                font=dict(color="#2cfec1"),
            )
        )

    if "layout" in figure:
        lat = figure["layout"]["mapbox"]["center"]["lat"]
        lon = figure["layout"]["mapbox"]["center"]["lon"]
        zoom = figure["layout"]["mapbox"]["zoom"]
    else:
        lat = (38.72490,)
        lon = (-95.61446,)
        zoom = 3.5

    layout = dict(
        paper_bgcolor="rgba(34,34,34,1)",
        mapbox=dict(
            layers=[],
            accesstoken=mapbox_access_token,
            style=mapbox_style,
            center=dict(lat=lat, lon=lon),
            zoom=zoom,
        ),
        hovermode="closest",
        margin=dict(r=0, l=0, t=0, b=0),
        annotations=annotations,
        # dragmode="lasso",
    )

    # base_url = "https://raw.githubusercontent.com/jackparmer/mapbox-counties/master/"
    # for bin in BINS:
    #     geo_layer = dict(
    #         sourcetype="geojson",
    #         source=base_url + str(year) + "/" + bin + ".geojson",
    #         type="fill",
    #         color=cm[bin],
    #         opacity=DEFAULT_OPACITY,
    #         # CHANGE THIS
    #         fill=dict(outlinecolor="#afafaf"),
    #     )
    #     layout["mapbox"]["layers"].append(geo_layer)

    fig = dict(data=data, layout=layout)
    return fig


@app.callback(
    Output(component_id='tweet', component_property='value'),
    [Input('button', 'n_clicks')],
    state=[State(component_id='tweet', component_property='value')]
)
def update_output_div(n_clicks, value):
    df = pd.read_csv("/Users/jarvis/Desktop/CODE/sadrat/web_app/appdata/adrmine_tweets_with_locations.csv")

    return (df.iloc[random.randrange(1,100,1)]["tweet"])

@app.callback(
    Output("detected-diseases", "children"),
    [Input('tweet', 'value')]
)
def update_disease(value):
    disease_list = disease_from_tweet(value)
    dstr = ""
    if len(disease_list) > 0:
        for disease in disease_list:
            dstr = dstr + disease + " , "
        dstr = dstr[:-2]
    else:
        dstr = "This tweet does not indicate a possible disease or condition"

    return dstr

@app.callback(
    Output("adr-proba", "children"),
    [Input('tweet', 'value')]
)
def update_adr_proba(value):
    df = pd.read_csv("/Users/jarvis/Desktop/CODE/sadrat/web_app/appdata/adrmine_tweets_with_locations.csv")
    for _, x in df.loc[df["tweet"] == str(value)].iterrows():
        label = x.label_proba
        break
    return  label

if __name__ == '__main__':
    app.run_server(debug=True)