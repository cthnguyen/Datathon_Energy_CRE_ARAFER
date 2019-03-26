import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Heatmap(
        z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -30, 20]],
        x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        y=['Morning', 'Afternoon', 'Evening']
    )
]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Watt\'y'),

    html.Div(children='''
        Dash: A web application framework for our Watt\'y application f$
    '''),

    dcc.Graph( 
                id='example-graph',
        figure={
            'data': [
                {'x' :[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -30, 20]], 
                 'y' : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                 'type' : 'heatmap',
                 'name': 'Results'
                }],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)


# py.iplot(data, filename='labelled-heatmap')


# plotly.offline.plot(data, filename='labelled-heatmap')
