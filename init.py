#10: 06!!!
import dash
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go
import random
colors = {
    'text':'#0000ff',#blue
    'plot': '#00ff00',#
    'paper': '#ff0000',#red
}
l1 = []
l2 = []
for i in range(0,55):
    l1.append(random.randint(0,i+1))
    l2.append(random.randint(0,i+2))

app = dash.Dash()
app.layout = html.Div([
    html.H1 (children ="hELLo world"    ,
        style={
            'color' : colors['text'],
        }
    ),
    html.Div(children ='Dash aplication',
        style={
            'color' : colors['text'],
        }
    ),
    dcc.Graph(
        id = 'SampleChart',
        figure = {
            'data' : [
                {'x':[1,2,3],'y':[1,2,3],'type':'bar','name':'My first Graphic'},
                {'x':[1,2,3],'y':[2,4,6],'type':'bar','name':'Second Graphic'},
                
            ],
            'layout' : {
                'title' : 'Mi primer graphico!!',
                'plot_bgcolor' :colors['plot'], # second background
                'paper_bgcolor': colors['paper'],# background general 
                'font':{
                    'color':colors['text'],
                }
            }
        }
    ),
    dcc.Graph(
        id = 'scatter_chart',
        figure= {
            'data':[go.Scatter(
                x = l1,
                y= l2,
                mode = 'markers',
            )],
            'layout': go.Layout(
                title = 'Scatter random graph',
                xaxis ={'title': 'random x values'},
                yaxis ={'title': 'random x values'}, 
            )
        }
    )

])

app.run_server(port=4050)
