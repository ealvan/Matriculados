import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px 

df = pd.read_csv('estudiantes.csv')

app = dash.Dash(__name__)

dataTable = dash_table.DataTable(
    id='table',
    style_cell={
        'minWidth':33,
        'maxWitdh':33,
        'width':33,
    },
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    row_deletable=True,
    filter_action="native",
    page_size=15
    
)

app.layout = html.Div([
    html.H1("Estudiantes con mas de una carrera",style={'text-align': 'center'}),
    html.Center(
        html.Div(
            dataTable,
            style={'width': "50%", 'height':"auto"}
            )
    ),
    html.Button('Submit', id='submit-val', n_clicks=0),
    dcc.Graph(id="figGraph",figure= px.bar(
            x=['TOTAL de Alumnos de la UNSA con 1 carrera',"TOTAL de alumnos de la UNSA con 2 carreras"],
            y=[23265-240,240],
        )),
])

if __name__ == '__main__':
    app.run_server(debug=True)