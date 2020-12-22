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
sizes = process.sizeGroup(jsonDict)
app.layout = html.Div([
    html.H1("Alumnos de la UNSA, por Grupo", style={'text-align': 'center'}),
    html.Center(
            html.Div(
            dcc.Graph(figure=px.bar(
                x=list(sizes.keys()),
                y=list(sizes.values()),
                color=list(sizes.keys()),
            )),
            style={
                'width':"50%",
                'maxWidth':"70%",
            }
        ),
    ),
    html.Br(),
])
def main():
    app.run_server(debug=True)
if __name__ == '__main__':
    main()
