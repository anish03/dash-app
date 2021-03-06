import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
    dcc.Input(id='my-id',value='initial value',type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div',component_property='children'),
    [Input(component_id='my-id',component_property='value')]
)

def update_output(input_val):
    return 'You entered {}'.format(input_val)

if __name__ == '__main__':
    app.run_server(debug=True)
