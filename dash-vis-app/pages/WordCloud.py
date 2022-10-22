from dash import html
import plotly.express as px


base_url = "/demo"

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H1('Fig5: Keywords Cloud'),
                                  html.P(
                                      "Objective 5: Changes in models’ application area"),
                                  html.P("Description: figure 5 is a word cloud concatenating keywords in different model's application area. All keywords are selected from our published papers dataset as they apear most frequently. The world cloud also changes dynamically as time goes from 2000 to 2022 years."),
                                  html.P("Tech approach: Python, PyeCharts."),
                                  html.P(
                                      "Discussion (Pros & Cons): Abundant Choices of models and Years; need  interpretation."),
                                  html.P([html.Strong('Interactions'),
                                          html.Br(),
                                          '- Click ">" button to autoplay.',
                                         html.Br(),
                                         '- Hover over words to see frequencies.',
                                          html.Br(),
                                          '- Select years to filter words by year',
                                          html.Br(),
                                          '- Check models tab to filter words by models.',
                                          html.Br(),
                                          '- Check/Uncheck labels to filter words by frequency.', ],
                                         style={'border-style': 'double'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             'Prev', id='button-prev', n_clicks=0)
                                                       ], href=base_url+'/CiteSpace', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              'Next', id='button-next', n_clicks=0),
                                                       ], href=base_url+'/PublicationMap'),
                                                   ]
                                                   )
                                      ])
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  html.Div(style={'margin-top': '13rem'}),
                                  html.Iframe(src="./assets/WordCloud.html", style={
                                      'height': '100%', 'width': '100%', 'margin-left': '5rem'}),
                              ])
                 ])
    ]
)
