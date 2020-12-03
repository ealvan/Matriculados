# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "carreras": ["Medicina", "Sistemas", "Industrial", "Medicina", "Sistemas", "Industrial"],
    "alumnos": [4, 1, 2, 2, 4, 5],
    "ciudad": ["Arequipa", "Arequipa", "Arequipa", "Lima", "Lima", "Lima"]
})

fig = px.bar(df, x="carreras", y="alumnos", color="ciudad", barmode="group")

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

    