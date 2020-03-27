import dash
import dash_renderer
import dash_core_components as dcc  # deals with all the graphs and charts stuff
import dash_html_components as html #deals with all the html
from dash.dependencies import Input,Output

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(id='input',value="xcx",type='text'),#####Basically a text i/p field for you to inpt text data into
    html.Div(id='output')###shows the o/p on the browser

])


#Wrapper/Decorator we need to output(the dependencies function) the into the output tag
#input id is the same but what we need for the input to print or intake wil be the value entered
@app.callback(
    Output(component_id='output',component_property='children'),
    [Input(component_id='input', component_property='value')])
#simple funtion to print the same thing as user entered
def actual_function(input_data):
    return "Input: {}".format(input_data)

if __name__=='__main__' :
    app.run_server(debug=True)

