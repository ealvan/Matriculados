#muestra a los estudiantes con mas de una carrera
import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output 
import plotly.express as px
df = pd.read_csv('estudiantes3.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)#init de application

#****************************************************
#obteniendo datos para el grafico
file4 = open('estudiantes3.csv','r',encoding='utf-8')
lines2 = file4.readlines()
carreers = {}
orderCarrs = {}
for l in lines2:
    lista4 = l.split(',')[1].split('/')
    for car in lista4:
        if car not in carreers:
            carreers[car] = 1
        else:
            carreers[car] += 1
sort_orders = sorted(carreers.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    orderCarrs.setdefault(i[0],i[1])
#****************************************************


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
        } for c in ['APELLIDOS Y NOMBRES', 'CARRERAS UNIVERSITARIAS']
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
    dcc.Graph(id="figGraph",figure= px.pie(
            names=['TOTAL de Alumnos de la UNSA con 1 carrera',"TOTAL de alumnos de la UNSA con 2 carreras"],
            values=[23265-240,240],
        )
    ),

    html.Center(
        children = [
            html.Div(
        dcc.Input(
            id='input-on-submit', 
            type='text',
            value="SISTEMAS",
            )
        ),
        html.Button('Buscar carrera', 
            id='submit-val', 
            n_clicks=0,
                        
        ),
        html.Div(id='container-button-basic',
             children='Ingresa la carrera que quieres buscar, y presiona "buscar"'
        ),
        html.Div(
            id="tableBest",
            children=[

            ],
            style={
               'width': "50%", 'height':"auto", 
            }
        ),
        dcc.Graph(
            id="carreras",
            figure=px.bar(
                x=list(orderCarrs.keys()),
                y=list(orderCarrs.values()),
                labels={'x':"Carreras universitarias",'y':'Numero de alumnos'},
                color= list(orderCarrs.keys()),       
            )
        )
        

        
        ]
    ),
    
])
@app.callback(
    dash.dependencies.Output('tableBest', 'children'),#para mostrar la busqueda
    [dash.dependencies.Input('submit-val', 'n_clicks')],#para enviar la busqueda
    [dash.dependencies.State('input-on-submit', 'value')])#para ingresar busqueda
def update_output(n_clicks, value):
    try:
        file2 = open('estudiantes3.csv',"r",encoding='utf-8')
        lines = file2.readlines()
    except:
        print("ocurrio un error")
    file2.close()
    str1 = "APELLIDOS Y NOMBRES,CARRERAS BUSCADAS,CUIS,GRUPOS \n"
    for line in lines:
        if str(value).upper() in line:
            str1 += line
    
    file3 = open('aux12.csv','w',encoding='utf-8')
    file3.write(str1)
    file3.close()
    parrafo = html.P(
            children=[
                "Se encontraron {} resultados".format(len(str1.split('\n'))-2),
            ]
    )
    if len(str1.split('\n'))-2 > 1:
        dataf = pd.read_csv('aux12.csv')
        table2 = dash_table.DataTable(
            data=dataf.to_dict("records"),
            id="tabla2",
            filter_action="native",
            columns=[{"name":i,"id":i} for i in dataf.columns],
            row_deletable=True,
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                }for c in ['APELLIDOS Y NOMBRES', 'CARRERAS UNIVERSITARIAS'] 
                
            ],  
            style_data_conditional=[
                    {
                    'if': {'row_index': 'odd'},    
                    'backgroundColor': 'rgb(248, 248, 248)'
                    }
            ],
            style_header={
                    'backgroundColor': 'rgb(248, 248, 248)',
                    'fontWeight': 'bold'
            }
            
        )           
    else:
        parrafo1 = html.P(
        children=[
            "No se encontraron resultados",
        ]
        )
             
        return [parrafo1,]
    return [parrafo,table2,]




def main():
    app.run_server(debug=True,port=8050)
main()

