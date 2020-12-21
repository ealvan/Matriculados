import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import process
import json
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

app = dash.Dash(__name__)#init de application
fileData = open('2020_B_version2.json','r',encoding='utf-8')
jsonDict = json.load(fileData)

app.layout = html.Div([
    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="carrera",
                 options=[ {'label': i, 'value': i} for i in jsonDict.keys()],
                 multi=False,
                 value='AGRONOMÍA',
                 style={'width': "30%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='figGraph', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='figGraph', component_property='figure')],
    [Input(component_id='carrera', component_property='value')]
)
def update_graph(option_slctd):
    dictCuis = process.getCuisEsc(jsonDict,str(option_slctd))
    
    container = "La opcion que elegiste fue: {}".format(option_slctd)
    if dictCuis:
        fig = px.bar(
            x=list(dictCuis.keys()),
            y=list(dictCuis.values()),
        )
        
    return container, fig

if __name__ == '__main__':
    app.run_server(debug=True)