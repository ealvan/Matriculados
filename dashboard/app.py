import json
import importlib
import process
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
fileData = open('../datos/2020_B_version2.json','r',encoding='utf-8')
jsonDict = json.load(fileData)

carreras = process.getSize(jsonDict)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "carreras": list(carreras.keys()),
    "alumnos": list(carreras.values()),
})
#
fig = px.bar(df, x="carreras", y="alumnos", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Contabilzacion_por_Carreras'),

    html.Div(children='''
        Carreras vs Numero de alumnos
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
])
def main():
    if __name__ == '__main__':
        app.run_server(debug=True)
    else:
        app.run_server(debug=True)
main()


    