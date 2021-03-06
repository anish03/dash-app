import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

app = dash.Dash()

heading = {
    'padding' : '10px'
}

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    html.H1(style={'padding':heading['padding']},children='Sensor Data'),

    html.Div(style={'padding':heading['padding']},children='''
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
