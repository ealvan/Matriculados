#aqui se muestra la distibucion de los estudiantes por grupo en el que estan
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
    html.H1("Alumnos de la UNSA, por distribuciòn de Grupos", style={'text-align': 'center'}),
    
    html.Div(
        children=[
            dcc.Dropdown(
                id="myDrop",
                options=[
                    {'label':"Grafico de Barras","value":"barChart"},
                    {'label':"Grafico de Tortas","value":"pieChart"},
                    {'label':"Grafico de Linea","value":"lineChart"},
                ],
                value="barChart",
                multi=False,
                style={'width':"37%"},
            ),
            html.H4(
                "En el año 2020, se matricularon {} estudiantes en la UNSA".format(sum(sizes.values())),
            ),
            dcc.Graph(
                id="typeGraph",
            ),           
        ],
    ),
    html.Br(),
])
@app.callback(
    [Output(component_id='typeGraph', component_property='figure'),],
    [Input(component_id='myDrop', component_property='value'),]
)
def updateGraph(drop_option):
    lista = ["lineChart","pieChart","barChart"]
    fig12=None
    if str(drop_option) == lista[2]:
        fig12 = px.bar(
            x=list(sizes.keys()),
            y=list(sizes.values()),
            color=list(sizes.keys())
        )
    elif str(drop_option) == lista[1]:
        fig12 = px.pie(
            names = list(sizes.keys()),
            values = list(sizes.values()),
            hole=.3,
        )
    else:
        fig12 = go.Figure()
        fig12.add_trace(
            go.Scatter(
                x=[1,2,3],
                y= list(sizes.values()),
                mode='lines+markers',
                name='lines+markers',    
            )
        )
    return (fig12,)

def main():
    app.run_server(debug=True,port=8052)

main()
