import dash
import dash_renderer
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Trying out dash'),
    dcc.Graph(id='Example',
              figure={
                  'data':[{'x':[1,2,3,4,5,6,7,8],'y':[1,4,9,16,25,36,49,64],'type':'line','name':'Xars'},
                          {'x':[1,2,3,4,5,6,7,8],'y':[1,3,8,15,24,35,48,63],'type':'bar','name':'Mars'}],
                  'layout': {
                      'title': 'Basic'

                  }
              }

              )

])

if __name__=='__main__' :
    app.run_server(debug=True)

