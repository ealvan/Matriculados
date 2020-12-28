#los primeros nombres mas comunes de la universidad
import pandas as pd
import process
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px #(need to pip install plotly==4.4.1)
import json

fileData = open('2020_B_version2.json','r',encoding='utf-8')
jsonDict = json.load(fileData)
# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__)

list1 = ['150','200','250','300']
#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.H1(['Los nombres mas comunes en la Universidad Nacional de San Agustin'],style={'text-align':'center'}),
        dcc.Dropdown(
            id='my_dropdown',
            options=[
                     {'label': i, 'value': i} for i in list1
            ],
            value='150',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='the_graph',figure={})
    ]),

])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def update_graph(my_dropdown):
    
    comunNames = process.comunName(jsonDict,int(my_dropdown))
    piechart=px.pie( 
            names=list(comunNames.keys()),
            values=list(comunNames.values()),
            hole=.3,
            )
    return (piechart)

def main():
    app.run_server(debug=True,port=8055)

main()