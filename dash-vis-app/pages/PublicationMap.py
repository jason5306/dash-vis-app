from dash import html
import plotly.express as px


base_url = "/demo"

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H1('Fig6: Publication Heat Map'),
                                  html.P(
                                      "Objective 6: Main models’ regional research popularities."),
                                  html.P("Description: This figure shows the reginal distribution of the number of papers published. Different colors from darker to lighter in the world map represent the total publication number in that area from large to small in the heatmap."),
                                  html.P("Tech approach: Python, PyeCharts."),
                                  html.P(
                                      "Discussion (Pros & Cons): Clear distribution, details need zooming in to see."),
                                  html.P([html.Strong('Interactions'),
                                         html.Br(),
                                         '- Scroll to zoom in/out.',
                                        html.Br(),
                                        '- Click and drag to move around.',
                                         html.Br(),
                                         '- Hover over points to see city names.',
                                         html.Br(),
                                         '- Drag frequency bar to filter results.',
                                         html.Br(),
                                         '- Change views between "Effect Scatter“ and "HeatMap".'],
                                        style={'border-style': 'double'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             'Prev', id='button-prev', n_clicks=0)
                                                       ], href=base_url+'/WordCloud', style={'margin-right': '2rem'}),
                                                   ]
                                                   )
                                      ])
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.Div(style={'margin-top': '13rem'}),
                                  html.Iframe(src="./assets/PublicationMap.html", style={
                                      'height': '100%', 'width': '100%', 'margin-left': '5rem'}),
                              ])
                 ])
    ]
)
