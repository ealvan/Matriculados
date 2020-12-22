import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px 

df = pd.read_csv('estudiantes.csv')


app = dash.Dash(__name__)#init de application

dataTable = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    row_deletable=True,
    filter_action="native",
    page_size=15,
    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
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
            color_discrete_sequence=['#00FF7F','red'],

        )),
])

if __name__ == '__main__':
    app.run_server(debug=True)