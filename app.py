# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import json
import formando
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
fileData = open('dataNew.json','r',encoding='utf-8')
jsonDict = json.load(fileData)

carreras = list(jsonDict.keys())
sizeCarrs = formando.getSize(jsonDict)


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "carreras": carreras,
    "alumnos": sizeCarrs,
})

fig = px.bar(df, x="carreras", y="alumnos", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application FRAMEWORK for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),


])

if __name__ == '__main__':
    app.run_server(debug=True)

    