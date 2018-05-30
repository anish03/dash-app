import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Sensor Data'),

    html.Div(children='''
        A web Dash App.
    '''),

    dcc.Graph(
        id='op-graph',
        figure={
            'data':[
                {'x':[x for x in range(0,10)],'y':np.random.randint(10,size=10),'type':'bar'}
            ],
            'layout':{
                'title':'Dash viz'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
