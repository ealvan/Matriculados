#aqui se muestran a los estudiantes por su año de ingreso los primeors 4 digitos
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import process
import json
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.io as pio
from dash.dependencies import Input, Output
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)#init de application
fileData = open('2020_B_version2.json','r',encoding='utf-8')
jsonDict = json.load(fileData)

app.layout = html.Div([
    html.H1("Numero de alumnos por año de ingreso, en una carrera de la UNSA", style={'text-align': 'center'}),
    html.Div(
        [
            html.Div([
                dcc.Dropdown(id="carrera",
                 options=[ {'label': i, 'value': i} for i in jsonDict.keys()],
                 multi=False,
                 value='AGRONOMÍA',
                 style={'width': "50%"}
                ),

            ],className= 'six columns'),
            html.Div([
                    dcc.Dropdown(
                        id="typeG",
                        options=[
                            {'label':"Grafico de Barras","value":"barChart"},
                            {'label':"Grafico de Tortas","value":"pieChart"},
                            {'label':"Grafico de Linea","value":"lineChart"},
                        ],
                        multi=False,
                        value="barChart",
                        style={'width':"50%"},
                    ),
            ],className= 'six columns'),
        ],
        className= 'row'
    ),
    

    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='figGraph', figure={}),
    html.Div(
        html.Center(
            children=[
                dcc.Dropdown(
                        id="typeA",
                        options=[
                            {'label':"Grafico de Barras","value":"barChart"},
                            {'label':"Grafico de Tortas","value":"pieChart"},
                            {'label':"Grafico de Linea","value":"lineChart"},
                        ],
                        multi=False,
                        value="barChart",
                        style={'width':"37%"},
                        
                ),
            ]

        ),
    ),
    dcc.Graph(id="newFig", figure = {}),
    html.Div(
        children=[
            html.Div(
                children=[
                    dcc.Dropdown(
                        id="drop1",
                        options=[{'label':j,"value":j} for j in jsonDict.keys()],
                        value="AGRONOMÍA",
                        multi=False,
                        style={'width':"60%"},
                    ),
                ]
                ,className="six columns"),
            html.Div(
                children=[dcc.Dropdown(
                        id="drop2",
                        options=[{'label':j,"value":j} for j in jsonDict.keys()],
                        value="AGRONOMÍA",
                        multi=False,
                        style={'width':"60%"},
                    ),]               
                ,className="six columns"), 
        ],
        className="row",
        style={
            'width':"80%",
        }
    ),
    dcc.Graph(
        id="twoDropsGraph",
        
    )
])
@app.callback(
    [Output(component_id='twoDropsGraph', component_property='figure'),],
    [Input(component_id='drop1', component_property='value'),
    Input(component_id="drop2",component_property='value'),]
)
def updateGraph(drop1,drop2):
    dict1 = process.getCuisEsc(jsonDict,str(drop1),3)
    dict2 =  process.getCuisEsc(jsonDict,str(drop2),3)

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=list(dict1.keys()),
            y=list(dict1.values()),
            name="Carrera {}".format(drop1),
            marker_color='indianred',
        ),
    )
    fig.add_trace(
        go.Bar(
            x=list(dict2.keys()),
            y=list(dict2.values()),
            name="Carrera {}".format(drop2),
            marker_color='lightsalmon',

        )
    )
    #fig.update_layout(barmode='group', xaxis_tickangle=-45)

    return (fig,)
    








# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='figGraph', component_property='figure'),
     Output(component_id="newFig", component_property="figure")],
    [Input(component_id='carrera', component_property='value'),
    Input(component_id="typeG",component_property='value'),
    Input(component_id="typeA",component_property='value'),]
)
def update_graph(option_slctd,optSltd,optGeneral):
    lista = ["lineChart","pieChart","barChart"]
    figure1 = None
    dictCuis = process.getCuisEsc(jsonDict,str(option_slctd),3)
    cuisAll = process.getCuisAll(jsonDict)
    cuisList = []
    for i in dictCuis.keys():
        cuisList.append(int(i))
    colors= []
    for i in range(len(dictCuis.keys())):
        colors.append(i)
    if str(optSltd) == lista[2]:
        figure1 = px.bar(
            x=list(dictCuis.keys()),
            y=list(dictCuis.values()),
            color=colors
        )
    elif str(optSltd) == lista[1]:
        figure1 = px.pie(
            names = list(dictCuis.keys()),
            values = list(dictCuis.values()),
            hole=.3,
        )
    else:
        figure1 = go.Figure()
        figure1.add_trace(
            go.Scatter(
                x=cuisList,
                y=list(dictCuis.values()),
                mode='lines+markers',
                name='lines+markers',    
            )
        )
    cuisList1 = []
    for i in cuisAll.keys():
        cuisList1.append(int(i))       
    if str(optGeneral) == lista[2]:
        fig1 = px.bar(
            x=list(cuisAll.keys()),
            y=list(cuisAll.values()),
            color=list(cuisAll.keys())
        )
    elif str(optGeneral) == lista[1]:
        fig1 = px.pie(
            names = list(cuisAll.keys()),
            values = list(cuisAll.values()),
            hole=.3,
        )
    else:
        fig1 = go.Figure()
        fig1.add_trace(
            go.Scatter(
                x=list(cuisAll.keys()),
                y=list(cuisAll.values()),
                mode='lines+markers',
                name='lines+markers',
            )
        )
    container = "La opcion que elegiste fue: {}".format(option_slctd)
    
    
    
    #fig1={}
    #if "button" in changed_id:
    #    fig1 = px.bar(
    #        x=list(cuisAll.keys()),
    #        y=list(cuisAll.values()),
    #        color=list(cuisAll.keys()),
    #    )
    return (container, figure1,fig1)









def main():
    app.run_server(debug=True,port=8053)

main()