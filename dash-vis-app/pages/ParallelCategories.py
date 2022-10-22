from dash import dcc, html, Input, Output, callback
import plotly.graph_objects as go
import numpy as np
from pandas import read_csv

import sys
from pathlib import Path

#data_path = Path(sys.argv[0]).parent.joinpath('DataParallelCategories.csv')
df = read_csv('./data/DataParallelCategories.csv')
base_url = "/demo"

# Create dimensions
model_dim = go.parcats.Dimension(
    values=df['Model'],
    categoryorder='category ascending', label="Model"
)

year_dim = go.parcats.Dimension(
    values=df['Publication Year'],
    categoryorder='category ascending', label="Year"
)

area_dim = go.parcats.Dimension(
    values=df['Research Areas'],
    categoryorder='category ascending', label="Area"
)


# Create parcats trace
color = np.zeros(len(df), dtype='uint8')
colorscale = [[0, '#D885F2'], [1, '#73288A']]

fig = go.FigureWidget(
    data=go.Parcats(
        dimensions=[model_dim, year_dim, area_dim],
        line={'colorscale': colorscale, 'cmin': 0,
              'cmax': 1, 'color': color},
        hoveron='color',
        arrangement='freeform'))
fig.update_layout(
    template='plotly_dark', paper_bgcolor='rgba(0, 0, 0, 0)',
    height=800,
    dragmode='lasso', hovermode='closest',
    autosize=True,
    margin=dict(
        l=20,
        r=240,
        b=50,
        t=50,
        pad=4
    ),
    plot_bgcolor='rgba(0, 0, 0, 0)', width=float('inf'))

#app = Dash(__name__)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}


layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H1('Fig1: Parallel Categories Chart'),
                                  html.P(
                                      "Objective 1: Evolution of research area and keywords over time."),
                                  html.P("Description: figure 1 is a parallel categories graph connecting models,  publication year, and research area. Selecting the node gives it and its connected part a highlighted color to investigate the relationship in between."),
                                  html.P("Tech approach: Python, Plotly"),
                                  html.P(
                                      "Discussion (Pros & Cons): Click-highlight-interaction; density may be too high"),
                                  html.P([html.Strong('Interactions'),
                                          html.Br(),
                                          '- Hover over ribbons and lines to see number of researches on the category.',
                                         html.Br(),
                                         '- Drag to move ribbons around.',
                                          html.Br(),
                                          '- Click on a ribbon to highlight a category.'],
                                         style={'border-style': 'double'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             'Prev', id='button-prev', n_clicks=0)
                                                       ], href=base_url+'/', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              'Next', id='button-next', n_clicks=0),
                                                       ], href=base_url+'/TimeRiver'),
                                                   ]
                                                   )
                                      ])
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.Div(style={'margin-top': '5rem'}),
                                  dcc.Graph(id="graph", figure=fig),
                              ])
                 ])
    ]
)


@callback(
    Output("graph", "figure"),
    Input('graph', 'clickData'))
def update_figure(clickData):
    list_ = clickData['points']
    res = [item['pointNumber'] for item in list_]

    new_color = np.zeros(len(df), dtype='uint8')
    new_color[res] = 1
    fig.data[0].line.color = new_color
    return fig

#app.run_server(debug=True, use_reloader=False)
