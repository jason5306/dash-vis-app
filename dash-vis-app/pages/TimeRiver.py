from dash import html

base_url = "/demo"

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H1('Fig2: Time River'),
                                  html.P(
                                      "Objective 2: Main models’ regional research popularities."),
                                  html.P("Description: figure 2 is a river plot demonstrating the timelines of the citation number of selected published paper. One can choose a specific time period at the bottom bar section to zoom into the graph to have a closer look at that section."),
                                  html.P("Tech approach: Python, Plotly."),
                                  html.P(
                                      "Discussion (Pros & Cons): Clear trends; few papers before 2014."),
                                  html.P([html.Strong('Interactions'),
                                          html.Br(),
                                          '- Hover over to see cited times data.',
                                         html.Br(),
                                         '- Click and drag to zoom in / Double-click to zoom back out.',
                                          html.Br(),
                                          '- Drag scale bar to specify range of investigation.',
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
                                                       ], href=base_url+'/ParallelCategories', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              'Next', id='button-next', n_clicks=0),
                                                       ], href=base_url+'/CiteSpaceCir'),
                                                   ]
                                                   )
                                      ])
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.Div(style={'margin-top': '5rem'}),
                                  html.Iframe(src="./assets/TimeRiver.html",
                                              style={'height': '100%', 'width': '100%'}),
                              ])
                 ])
    ]
)
