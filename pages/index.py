from dash import html
import plotly.express as px

import sys
from pathlib import Path

path = Path(sys.argv[0]).parent.joinpath('/assets/citespace/citespace_index.html')

base_url = "/demo"
layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='ten columns div-user-controls',
                              children=[
                                  html.H1('Development of Models Used in Computer Vision',
                                          style={
                                              'background-color': '#693DE8', 'max-width': '40%'},
                                          className='index-title'),
                              ]
                              ),
                     html.Div(className='five columns div-user-controls index-description-container', children=[
                         html.P("In this project, we want to investigate how deep learning models used in the field of computer vision developed over time. We confined our subject of models to only GoogleNet, SeNet, VGG, AlexNet, LeNet, and ResNet. We crawled our data of published papers on these models from the Web of science, including information like article title, journal name, author(s), publication time, location, application areas, citation number, reference list and etc. We analyzed these data and investigated the geographic distribution, citation number trends, research area, and citation space properties in our dataset. We used python packages, including plotly, pyecharts, pyvis, and network, to visualize our work and combined all figures and descriptions in dash for a online interactive view.",
                                className='index-description')
                     ]),
                     html.Div(className='four columns div-user-controls index-author-container',
                              children=[
                                  html.P('Authors: ', className='index-author',
                                         style={'margin-bottom': '5px'}),
                                  html.P('Jiacheng Xie | Haowen Ji | Dunhan Jiang',
                                         className='index-author'),
                              ]
                              ),
                 ]),
        html.Div(className='two columns', children=[
            html.Div(
                children=[
                    html.Div(className='bottom-nav',
                             children=[
                                 html.A(id='', className='', children=[
                                     html.Button(
                                         'Start', id='button-next', n_clicks=0, style={'margin-left': '15rem'}),
                                 ], href=base_url+'/ParallelCategories'),
                             ]
                             )
                ]
            ),
        ]),
        html.Div(id='', className='', children=[
            html.Iframe(src=path,
                        className='poster-img', style={'height': '110%'}),
        ])
    ]
)
