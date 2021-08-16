#aqui se muestran a los estudiantes por su año de ingreso los primeors 4 digitos
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import process
import json
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)#init de application
fileData = open('2021_A.json','r',encoding='utf-8')
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
    dcc.Graph(id='figGraph', figure={}),
    html.Div(
        html.Center(
            html.Button("Crear grafica entera!!",id="button",n_clicks=0),
        ),
    ),
    dcc.Graph(id="newFig", figure = {}),
])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='figGraph', component_property='figure'),
     Output(component_id="newFig", component_property="figure")],
    [Input(component_id='carrera', component_property='value'),
    Input(component_id="button",component_property='n_clicks')]
)
def update_graph(option_slctd,clicks):
    dictCuis = process.getCuisEsc(jsonDict,str(option_slctd),3)
    cuisAll = process.getCuisAll(jsonDict)
    container = "La opcion que elegiste fue: {}".format(option_slctd)
    if dictCuis:
        fig = px.bar(
            x=list(dictCuis.keys()),
            y=list(dictCuis.values()),
            color=list(dictCuis.keys())
        )
    
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    fig1={}
    if "button" in changed_id:
        fig1 = px.bar(
            x=list(cuisAll.keys())[5:],
            y=list(cuisAll.values())[5:],
            color=list(cuisAll.keys())[5:],
        )
    return (container, fig,fig1)

def main():
    app.run_server(debug=True,port=8053)

main()