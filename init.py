
import dash
import dash_core_components as dcc 
import dash_html_components as html 
 
colors = {
    'text':'#0000ff',#blue
    'plot': '#00ff00',#
    'paper': '#ff0000',#red
}
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
    )

])



app.run_server(port=4050)
