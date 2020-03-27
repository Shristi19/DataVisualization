import dash
import dash_renderer
import dash_core_components as dcc  # deals with all the graphs and charts stuff
import dash_html_components as html #deals with all the html
import pandas
import pandas_datareader as web
import datetime

start_time=datetime.datetime(2006,1,1)
end_time=datetime.datetime.now()

stock_symbol='TSLA'

df=web.DataReader(stock_symbol,'yahoo',start_time,end_time)#to get data for that stock symbol, from the data_source"Google", for the time(start to end)
##google as a datasource not working for this version






app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Stock graph'),#To show different html on the browser,H1 is the tag
    dcc.Graph(id='Example',                                                                                   #Every graph will need an id so that we can loacate it with html  #This is to basically to show graph
              figure={
                  'data':[{'x':df.index,'y':df.Close,'type':'line','name':stock_symbol}],
                  'layout':{
                      'title': 'Basic'

                  }
              }

              )

])

if __name__=='__main__' :
    app.run_server(debug=True)

