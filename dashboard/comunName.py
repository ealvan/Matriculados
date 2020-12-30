#los primeros nombres mas comunes de la universidad
import pandas as pd
import process
import plotly.graph_objects as go
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

list1 = ['150','200','250','300']#numero de alumnos que tienen el mismo primer nombre
list2 = ['50','60','80','100','130','150','200']
#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.H1(['Los nombres mas comunes en la Universidad Nacional de San Agustin'],style={'text-align':'center'}),
        html.Div([
            html.Div([
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
            ],className="six columns"),
            html.Div([
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
            ],className="six columns"),
        ],className="row")
    ]),
    html.Div([
        dcc.Graph(id='the_graph',figure={})
    ]),
    html.Center(
        children=[
            html.H3("Los apellidos paternos mas comunes en la UNSA"),
            dcc.Dropdown(
                id="drop1",
                options=[
                    {'label':"Grafico de Barras","value":"barChart"},
                    {'label':"Grafico de Tortas","value":"pieChart"},
                    {'label':"Grafico de Linea","value":"lineChart"},
                ],
                value="barChart",
                multi=False,
                style={'width':"37%"},
            ),
                dcc.Dropdown(
                    id='drop2',
                    options=[
                             {'label': i, 'value': i} for i in list2
                    ],
                    value=50,
                    multi=False,
                    clearable=False,
                    style={"width": "30%"}
                ),
            dcc.Graph(
                id = "lastNameGraph",
                figure={}
            )
        ],
    )
])
@app.callback(
    Output(component_id='lastNameGraph', component_property='figure'),
    [Input(component_id='drop1', component_property='value'),
    Input(component_id='drop2', component_property='value'),
    ]
)
def updateGraph(drop_option,drop2):
    lista = ["lineChart","pieChart","barChart"]
    lastNamedict = process.comunLastName(jsonDict,int(drop2))
    if str(drop_option) == lista[2]:
        fig12 = px.bar(
            x=list(lastNamedict.keys()),
            y=list(lastNamedict.values()),
            color=list(lastNamedict.keys())
        )
    elif str(drop_option) == lista[1]:
        fig12 = px.pie(
            names = list(lastNamedict.keys()),
            values = list(lastNamedict.values()),
            hole=.3,
        )
    else:
        fig12 = go.Figure()
        fig12.add_trace(
            go.Scatter(
                x=list(lastNamedict.keys()),
                y= list(lastNamedict.values()),
                mode='lines+markers',
                name='lines+markers',    
            )
        )
    return fig12

#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value'),
    Input(component_id='myDrop', component_property='value'),
    ]
)
def update_graph(my_dropdown,drop2):
    lista = ["lineChart","pieChart","barChart"]
    comunNames = process.comunName(jsonDict,int(my_dropdown))
    if str(drop2) == lista[2]:
        fig12 = px.bar(
            x=list(comunNames.keys()),
            y=list(comunNames.values()),
            color=list(comunNames.keys())
        )
    elif str(drop2) == lista[1]:
        fig12 = px.pie(
            names = list(comunNames.keys()),
            values = list(comunNames.values()),
            hole=.3,
        )
    else:
        fig12 = go.Figure()
        fig12.add_trace(
            go.Scatter(
                x=list(comunNames.keys()),
                y= list(comunNames.values()),
                mode='lines+markers',
                name='lines+markers',    
            )
        )
    
    return (fig12)

def main():
    app.run_server(debug=True,port=8055)

main()