import dash
import dash_core_components as dcc  # deals with all the graphs and charts stuff
import dash_html_components as html #deals with all the html
from dash.dependencies import Input,Output
import pandas_datareader as web
import datetime

# start_time=datetime.datetime(2006,1,1)
# end_time=datetime.datetime.now()
#
# stock_symbol='TSLA'

#df=web.DataReader(stock_symbol,'yahoo',start_time,end_time)#to get data for that stock symbol, from the data_source"Google", for the time(start to end)
##google as a datasource not working for this version

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Stock graph'),#To show different html on the browser,H1 is the tag
    dcc.Input(value='',id='input',type='text'),
    html.Div(id='output_of_graph')

])


@app.callback(
Output(component_id='output_of_graph',component_property='children'),
[Input(component_property='value',component_id='input')])

def function(input_data):
    start_time=datetime.datetime(2006,1,1)
    end_time=datetime.datetime.now()

    stock_symbol=input_data## yahoo has been depreceated for real time updates

    df=web.DataReader(stock_symbol,'yahoo',start_time,end_time)



    return dcc.Graph(id='Example',                                                                                   #Every graph will need an id so that we can loacate it with html  #This is to basically to show graph
                    figure={
                                  'data':[{'x':df.index,'y':df.Close,'type':'line','name':stock_symbol}],
                                  'layout':{
                                      'title': stock_symbol

                                  }
                              }

                     )




if __name__=='__main__' :
    app.run_server(debug=True)
