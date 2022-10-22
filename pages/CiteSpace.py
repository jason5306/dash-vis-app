from dash import html
import plotly.express as px

base_url = "/demo"

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H1('Fig4: Linked Network Graph'),
                                  html.P(
                                      "Objective 4: Research papers’ citation relationship"),
                                  html.P("Description: figure 4 is a linked network graph visualizing citation relationship between published papers in our dataset. Users can use the filter function ontop to select specific paper (node) or citation relationship (edge) to see only part of the sophisticated network. One can also click or drag the node to investigate the cite space interacgively."),
                                  html.P(
                                      "Tech approach: Python, Pyvis and Networkx"),
                                  html.P(
                                      "Discussion (Pros & Cons): Interactive in filtering and selection; too dense"),
                                  html.P([html.Strong('Interactions'),
                                          html.Br(),
                                          '- Scroll to zoom in/out.',
                                         html.Br(),
                                         '- Click and drag to move around.',
                                          html.Br(),
                                          '- Hover over nodes to see citation information.',
                                          html.Br(),
                                          '- Click on nodes to highlight connected nodes and edges.',
                                          html.Br(),
                                          '- Use the search bar to conduct advanced filtering.'],
                                         style={'border-style': 'double'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             'Prev', id='button-prev', n_clicks=0)
                                                       ], href=base_url+'/CiteSpaceCir', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              'Next', id='button-next', n_clicks=0),
                                                       ], href=base_url+'/WordCloud'),
                                                   ]
                                                   )
                                      ])
                              ]
                              ),
                     html.Div(className='',
                              children=[
                                  html.Iframe(src="./assets/citespace/citespace.html", style={
                                      'height': '100%', "border-width": '0'}, className='cite-space'),
                              ])
                 ])
    ]
)
