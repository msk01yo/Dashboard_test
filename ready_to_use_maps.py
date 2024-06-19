import dash
from dash import html
from dash import dcc
import dash_leaflet as dl
from dash import Dash, Output, Input, State

from dash_extensions.javascript import assign

import json

app = dash.Dash(__name__)

with open('counties_r_states.geojson') as f:
    geojson_data = json.load(f)

app.layout = html.Div([
    dl.Map([
    dl.TileLayer(),
    dl.GeoJSON(data = geojson_data, zoomToBounds=True, id="geojson")
], style={'maxWidth': '1000px', 'height': '500px', 'margin': 'auto'}, center=[12, 85], zoom=5)
]),html.Div([
html.Button('States Map', id='show-map1', n_clicks=0),
html.Button('County Map', id='show-map2', n_clicks=0)
], style={'textAlign': 'center', 'padding': '10px'})
@app.callback(
    Output('geojson', 'data', allow_duplicate=True),
    Input('show-map1', 'n_clicks'),
    prevent_initial_call=True
)
def show_map1(n_clicks):
    if n_clicks > 0:
        with open('us_states.geojson') as f:
            return json.load(f)

@app.callback(
    Output('geojson', 'data'),
    [Input('show-map2', 'n_clicks')]
)
def show_map2(n_clicks):
    if n_clicks > 0:
        with open('counties_r_states.geojson', 'r') as f:
            return json.load(f)

if __name__ == "__main__":
    app.run_server(port = '8050', debug=True)