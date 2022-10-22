from dash import html
import plotly.express as px
import sys
from pathlib import Path


base_url = "/demo"

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H1('Fig3: Circular Network Graph'),
                                  html.P(
                                      "Objective 3: Research papers’ citation relationship."),
                                  html.P("Description: figure 3 is a circular network graph visualizing citation relationship between published papers in our dataset. All papers are categorized into their own model's field and legended with different colors. When users hover the mouse over the paper node it will be highlighted for a clear look. Souce paper would have the same color as its edge."),
                                  html.P("Tech approach: Python, PyeCharts."),
                                  html.P(
                                      "Discussion (Pros & Cons): Uses color to show different models & interactive filtering; quite dense."),
                                  html.P([html.Strong('Interactions'),
                                          html.Br(),
                                          '- Scroll to zoom in/out.',
                                         html.Br(),
                                         '- Hover over edges to see connection between researches.',
                                          html.Br(),
                                          '- Click on edges to see citation number of source paper.',
                                          html.Br(),
                                          '- Hover over nodes to see all connected nodes.',
                                          html.Br(),
                                          '- Check/Uncheck labels to select models.', ],
                                         style={'border-style': 'double'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             'Prev', id='button-prev', n_clicks=0)
                                                       ], href=base_url+'/TimeRiver', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                               'Next', id='button-next', n_clicks=0),
                                                       ], href=base_url+'/CiteSpace'),
                                                   ]
                                                   )
                                      ])
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.Div(style={'margin-top': '5rem'}),
                                  html.Iframe(src="./assets/citespace/citespace_cir.html", style={
                                      'height': '100%', 'width': '100%', 'margin-left': '5rem', "border-width": '0'}),
                              ])
                 ])
    ]
)
