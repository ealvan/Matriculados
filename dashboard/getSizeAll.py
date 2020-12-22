import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import process
import json
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)#init de application
fileData = open('2020_B_version2.json','r',encoding='utf-8')
jsonDict = json.load(fileData)
dic1 = process.getSize(jsonDict)

df = pd.read_csv('escuelasSize.csv')
table  = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_as_list_view=True,
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                } for c in ['CARRERAS UNIVERSITARIAS','NUMERO DE ESTUDIANTES']
            ],
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'

                }
            ],
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            }
        )

app.layout = html.Div([
    html.H1("Numero de estudiantes por Escuela Profesional.", style={'text-align': 'center'}),
    html.H3(f"Tenemos {len(dic1.keys())} escuelas profesionales, la carrera mas elegida es la carrera de EDUCACIÒN"),
    html.Br(),
    dcc.Graph(id='figGraph', 
        figure=px.bar(
            x=list(dic1.keys()),
            y=list(dic1.values()),
            color=list(dic1.keys())
        )
    ),
    html.H2("Tabla de las carreras. "),
    html.H5(f"El numero total de estudiantes matriculados de la UNSA es {sum(dic1.values())}"),
    html.Center(
        html.Div(
            table,
            style={'width': "20%", 'height':"auto"}
            )
    ),
])
def main():
    app.run_server(debug=True)
if __name__ == '__main__':
    main()