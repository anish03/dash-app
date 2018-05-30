import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash()

# include CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

df = pd.read_csv('perf_met1.csv')

available_selectors = df.columns.unique()

def generate_table(dataframe):
    return html.Table(
        #headers
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        #body
        [html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(0,len(dataframe))
        ],
        style={'margin-left':'30%'}
    )


app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='attrib1',
                options=[{'label':i,'value':i} for i in available_selectors if i!='Date' and i!='Unnamed: 0']
            ),
        ],
        style={'width':'48%','display':'inline-block'}),
        html.Div(id='output-div')
        # html.Div([
        #     dcc.Dropdown(
        #         id='attrib2',
        #         options=[{'label':i,'value':i} for i in available_selectors]
        #     )
        # ],
        # style={'width':'48%','display':'inline-block'})
    ]),

    dcc.Graph(id='main-graph'),
    html.Div([
        html.H4('Device Sensor Data'),
        generate_table(df)
    ])
])

@app.callback(
    Output('main-graph','figure'),
    [Input('attrib1','value')]
)
def update_graph(attrib):

    return {
        'data':[go.Scatter(
            x = df['Date'],
            y = df[attrib],
            mode = 'markers',
            marker = {
                'size' : 15,
                'opacity' : 0.5,
                'line' : {'width':0.5,'color':'white'}
            }
        )],
        'layout':go.Layout(
            xaxis = {
                'title' : 'Date'
            },
            yaxis = {
                'title' : attrib
            },
            margin = {
                'l' : 40, 'b' : 40, 't' : 10, 'r' : 0
            },
            hovermode = 'closest'
        )
    }

@app.callback(
    Output('output-div','children'),
    [Input('main-graph','hoverData')]
)
def update_table(date):
    return '{}'.format(date['points'][0]['x'])


if __name__ == '__main__':
    app.run_server(debug=True)
