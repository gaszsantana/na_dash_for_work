# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:29:45 2019

@author: Ricardo Gomez
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import os
from flask import send_from_directory
import dash_bootstrap_components as dbc
from figures import *
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go


#app = dash.Dash()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])#, title='Nucleo Analitico',requests_pathname_prefix='/app1/')

# default values
#app.config.assets_folder = 'assets'     # The path to the assets folder.
#app.config.include_asset_files = True   # Include the files in the asset folder
#app.config.assets_external_path = "http://code.jquery.com/jquery-3.3.1.min.js"    # The external prefix if serve_locally == False
#app.config.assets_url_path = '/assets'  # the local url prefix ie `/assets/*.js`
#app.css.config.serve_locally = True
#app.scripts.config.serve_locally = True
#app.scripts.config.serve_locally = False

app.title = 'Nucleo Analitico'


    
app.layout = html.Div([
    #Header
    html.Header(children=[ 
            html.Meta(charSet="utf-8"),
            html.Meta(name="author", content="Ricardo Gómez"),
            html.Link(rel="stylesheet", href="https://fonts.googleapis.com/css?family=Nunito+Sans:200,300,400,600,700"),
            
               
            ]),

    #NavBar
    html.Div(id="page-container", className="sidebar-l sidebar-o side-scroll header-navbar-fixed",
             children=[
            #<!-- Sidebar -->
            html.Nav(id="sidebar", children=[
                    html.Div(id="sidebar-scroll", children=[
                            html.Div(className="sidebar-content", children=[
                                    #<!-- Side Header -->
                                    html.Div(className="menuLeft__logo", children=[
                                        html.Div(className="menuLeft__logoContainer ", children=[
                                                html.Div(className="logo_na")
                                                #html.Img(src="assets\img\logos\logo-inverse.png")
                                                ])
                                        #<!-- END Side Header -->
                                        ]),
                                    #<!-- Side Content -->
                                    html.Div(className="side-content", children=[
                                            html.Ul(children=[
                                                html.A( children=[ 
                                                         dbc.Nav([dbc.NavItem(dbc.NavLink("Dashboard", id="dash-button", className="navlink_1 ico_dashb", href="#", ), style={"width": "100%"}, ),
                                                                  
                                                                  #---- Twitter ------#
                                                                  dbc.NavItem(dbc.NavLink("Twitter ", id="collapse-button", className="navlink_1 ico_twitter", href="#" ),style={"width": "100%"},),
                                                                  dbc.NavItem(dbc.Collapse(dbc.Nav([
                                                                            dbc.NavItem(dbc.NavLink("Sentiments",  href="#", className="navlink_2 ico_sen",),style={"width": "100%"},),
                                                                            dbc.NavItem(dbc.NavLink("Clusters", id="collapse-button-1", href="#", className="navlink_2 ico_clu ico_arr_1",),style={"width": "100%"},),
                                                                            dbc.NavItem(dbc.Collapse(dbc.Nav([
                                                                                    dbc.NavItem(dbc.NavLink("Profiles",  href="#", className="navlink_3 ico_pro",),),
                                                                                    dbc.NavItem(dbc.NavLink("Lexicon",  href="#", className="navlink_3 ico_spe",),),
                                                                                                            ],vertical="sm",  style={"text-indent": "44px"},), style={"background-color":"#000000", "width": "100%"}, id="collapse-1",),style={"width": "100%"},),
                                                                            dbc.NavItem(dbc.NavLink("Words Relationship",  href="#", className="navlink_2 ico_wor",),),
                                                                            dbc.NavItem(dbc.NavLink("Scope",  href="#", className="navlink_2 ico_sco",),),
                                                                                                    ], vertical="sm", style={"text-indent": "22px", "width": "100%"}, ),style={"background-color":"#000C17", "width": "100%"},id="collapse",)),
                                                                  
                                                                  #--- Facebook ---#
                                                                  dbc.NavItem(dbc.NavLink("Facebook", id="collapse-button-f", className="navlink_1 ico_facebook", href="#" ),style={"width": "100%"},),
                                                                  dbc.NavItem(dbc.Collapse(dbc.Nav([
                                                                            dbc.NavItem(dbc.NavLink("Sentiments",  href="#", className="navlink_2 ico_sen",),style={"width": "100%"},),
                                                                            dbc.NavItem(dbc.NavLink("Clusters", id="collapse-button-2", href="#", className="navlink_2 ico_clu ico_arr_1",),style={"width": "100%"},),
                                                                            dbc.NavItem(dbc.Collapse(dbc.Nav([
                                                                                    dbc.NavItem(dbc.NavLink("Profiles",  href="#", className="navlink_3 ico_pro",),),
                                                                                    dbc.NavItem(dbc.NavLink("Lexicon",  href="#", className="navlink_3 ico_spe",),),
                                                                                                            ],vertical="sm",  style={"text-indent": "44px"},), style={"background-color":"#000000", "width": "100%"}, id="collapse-2",),style={"width": "100%"},),
                                                                            dbc.NavItem(dbc.NavLink("Words Relationship",  href="#", className="navlink_2 ico_wor",),),
                                                                            dbc.NavItem(dbc.NavLink("Scope",  href="#", className="navlink_2 ico_sco",),),
                                                                                                    ], vertical="sm", style={"text-indent": "22px", "width": "100%"}, ),style={"background-color":"#000C17", "width": "100%"},id="collapse-f",)),
                                                                  
                                                                  #--- Instagram ---#
                                                                  dbc.NavItem(dbc.NavLink("Instagram", id="collapse-button-i", className="navlink_1 ico_instagram", href="#" ),style={"width": "100%"},),
                                                                  dbc.NavItem(dbc.Collapse(dbc.Nav([
                                                                            dbc.NavItem(dbc.NavLink("Sentiments",  href="#", className="navlink_2 ico_sen",),style={"width": "100%"},),
                                                                            dbc.NavItem(dbc.NavLink("Clusters", id="collapse-button-3", href="#", className="navlink_2 ico_clu ico_arr_1",),style={"width": "100%"},),
                                                                            dbc.NavItem(dbc.Collapse(dbc.Nav([
                                                                                    dbc.NavItem(dbc.NavLink("Profiles",  href="#", className="navlink_3 ico_pro",),),
                                                                                    dbc.NavItem(dbc.NavLink("Lexicon",  href="#", className="navlink_3 ico_spe",),),
                                                                                                            ],vertical="sm",  style={"text-indent": "44px"},), style={"background-color":"#000000", "width": "100%"}, id="collapse-3",),style={"width": "100%"},),
                                                                            dbc.NavItem(dbc.NavLink("Words Relationship",  href="#", className="navlink_2 ico_wor",),),
                                                                            dbc.NavItem(dbc.NavLink("Scope",  href="#", className="navlink_2 ico_sco",),),
                                                                                                    ], vertical="sm", style={"text-indent": "22px", "width": "100%"}, ),style={"background-color":"#000C17", "width": "100%"},id="collapse-i",)),
                                                                  
                                                                  
                                                                ],
                                                                vertical="md",  className='ant-menu menuLeft__navigation ant-menu-dark ant-menu-root ant-menu-inline',),

                                                            ]),
                                                            
                                                    ])

                                            ])
                                    ])
                            ])
                    ])
        
            ]),

    #Contenido
    html.Div([
            
            
        #sentiments IG
        dbc.Row([
            dbc.Col(
                html.H3(["Sentiment - User: X ",
                dcc.Graph(id='Sentiment-interactions',
                    figure= fig_t1,
                                          
                        ), ]),width=12, className='card', style={"width": "100%"},
                    ),
                                                          

            ], justify="between", no_gutters=False, align="end", style={"width": "100%"},),



        dbc.Row([
            dbc.Col(
                html.H3(["Interactions - User: X ",
                dcc.Graph(id='interactions',
                    figure={
                        'data': [go.Bar(
                                        x=['post_x','post_x1','post_x2','post_x3','post_x4', 'post_x5'],
                                        y=[320, 440, 540, 425, 427, 256],
                                        name='Comentarios',
                                        marker = dict(color = '#1F6B9C',),
                                        text = [320, 440, 540, 425, 427, 256],
                                        textposition = 'auto',
                                    ),
                                go.Bar(
                                        x=['post_x','post_x1','post_x2','post_x3','post_x4', 'post_x5'],
                                        y=[340, 800, 740, 625, 227, 156],
                                        name='Likes',
                                        marker = dict(color = '#38A399',),
                                        text = [340, 800, 740, 625, 227, 156],
                                        textposition = 'auto',
                                        
                                        
                                    ),                                
                                                            
                                ],
                        'layout':go.Layout(
                                legend=go.layout.Legend(
                                        x=0,
                                        y=1.0),
                                annotations=[
                                        dict(xref='x', 
                                             yref='y',
                                             text='TOTAL + FECHA',
                                             x=0,
                                             y=340 + 320,
                                             )],
                                
                                barmode='stack',
                                xaxis=dict(
                                      showgrid=False,
                                      showline=False,
                                      
                                      zeroline=True,
                                      tickangle=55
                                     
                                      ),
                                yaxis=dict(
                                      showgrid=False,
                                      showline=False,
                                      showticklabels=False,
                                      zeroline=False,
                                      


                                      ),
                                
                                )                       
                            },
                                          
                        ), ]),width=12, className='card', style={"width": "100%"},
                    ),
                                                          

            ], justify="between", no_gutters=False, align="end", style={"width": "100%"},),

        dbc.Row([
            dbc.Col(
                html.H3(["Palabras  Negativas del User X",
                    dcc.Graph(id='bar_pos_2',
                        figure={
                                'data': [go.Bar(x=[21, 57, 141, 202, 393, 454, 512], 
                                         y=['Mal', 'Odio', 'Vete', 'Nunca', 'HDP', 'CDTM', 'RATA'],
                                         orientation='h',
                                         text=[21, 57, 141, 202, 393, 454, 512], #cuando se le este agragando datos colocar porcentajes tambien
                                         textposition = 'auto',
                                         marker = dict(
                                                    color = '#363860',)
                                         )],
                                'layout':go.Layout(
                                        xaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=False,
                                                zeroline=False,
                                                domain=[0.15, 1]
                                            ),
                                            yaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=True,
                                                zeroline=False,
                                            ),
                                       margin=go.layout.Margin(l=10, r=50, t=10, b=10)
                                        )
                                }                  
                            )
                        ]),
                
                width=4, className='card',  style={"width": "31%"},                  
                ),

            dbc.Col(
                html.H3(["Palabras Neutras del User X",
                    dcc.Graph(id='bar_neu_2',
                        figure={
                                'data': [go.Bar(x=[21, 57, 141, 202, 393, 454, 512], 
                                         y=['Normal', 'Pido', 'Agua', 'Seguridad', 'Ayuda', 'olvidar', 'cuando'],
                                         orientation='h',
                                         text=[21, 57, 141, 202, 393, 454, 512], #cuando se le este agragando datos colocar porcentajes tambien
                                         textposition = 'auto',
                                         marker = dict(
                                                    color = '#F2F2F2',
                                                    line = dict(
                                                            color = '#C1C1C1',
                                                            width = 1))
                                                    
                                         )],
                                'layout':go.Layout(
                                        xaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=False,
                                                zeroline=False,
                                                domain=[0.15, 1]
                                            ),
                                            yaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=True,
                                                zeroline=False,
                                            ),
                                        margin=go.layout.Margin(l=10, r=50, t=10, b=10)
                                        )
                                }                  
                        ), ]),width=4, className='card', style={"width": "31%"},
                ),

            
            dbc.Col(
                html.H3(["Palabras Positivas del User X",
                    dcc.Graph(id='bar_neg_2',
                        figure={
                                'data': [go.Bar(x=[21, 57, 141, 202, 393, 454, 512], 
                                         y=['Dios', 'Bendiga', 'Amor', 'Bien', 'Amo', 'Palante', '100'],
                                         orientation='h',
                                         text=[21, 57, 141, 202, 393, 454, 512], #cuando se le este agragando datos colocar porcentajes tambien
                                         textposition = 'auto',
                                         marker = dict(
                                                    color = '#0767A0',)
                                         )],
                                'layout':go.Layout(
                                        xaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=False,
                                                zeroline=False,
                                                domain=[0.15, 1]
                                            ),
                                            yaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=True,
                                                zeroline=False,
                                            ),
                                        margin=go.layout.Margin(l=10, r=50, t=10, b=10)
                                        )
                                }                  
                        ), ]),width=4, className='card', style={"width": "31%"},
                    ),
                                                         
            ], justify="between", no_gutters=False, align="center", style={"width": "100%"},),        
        
        dbc.Row([
            dbc.Col(
                html.H3(["Post_x",
                          html.Img(
                            src='https://media.wired.com/photos/598e35fb99d76447c4eb1f28/master/pass/phonepicutres-TA.jpg',
                            style={
                                'height' : '80%',
                                'width' : '80%',
                                 'display' : 'block',
                                 'margin-left': 'auto',
                                 'margin-right': 'auto',
#                                'float' : 'right',
#                                'position' : 'relative',
#                                'padding-top' : 0,
#                                'padding-right' : 0
                            },
                            ),
                
                          html.H4(["Username: "]),
                          html.H5(["Text contenido del mensaje"]),
                         ], ),
                
                width=6, className='card',  style={"width": "48%"},                  
                ),
            
            dbc.Col(
                html.H3(["Sentimento post_x",
                    dcc.Graph(id='crossfilter-indicator-scatter_1',
                        figure={
                            'data': [
                                go.Pie(labels=['Positivo','Neutral','Negativo'], hoverinfo='label', textinfo='value+percent', 
                                values=[1500,753,990],
                                
                                marker=dict(colors= [ '#0767A0', '#F2F2F2', '#363860']))],
                            'layout':go.Layout(
                                    #title='Sentiment',
                                    showlegend=True,
                                    legend=go.layout.Legend(
                                        x=0,
                                        y=1.0),
                                    margin=go.layout.Margin(l=10, r=10, t=10, b=10)
                                    
                                    )                       
                                }                  
                        ), ]),width=6, className='card', style={"width": "48%"},
                    ),
                                                         
            ], justify="between", no_gutters=False, align="center", style={"width": "100%"},),

        dbc.Row([
            dbc.Col(
                html.H3(["Palabras Negativas del Post X",
                    dcc.Graph(id='bar_pos_1',
                        figure={
                                'data': [go.Bar(x=[21, 57, 141, 202, 393, 454, 512], 
                                         y=['Mal', 'Odio', 'Vete', 'Nunca', 'HDP', 'CDTM', 'RATA'],
                                         orientation='h',
                                         text=[21, 57, 141, 202, 393, 454, 512], #cuando se le este agragando datos colocar porcentajes tambien
                                         textposition = 'auto',
                                         marker = dict(
                                                    color = '#363860',)
                                         )],
                                'layout':go.Layout(
                                        xaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=False,
                                                zeroline=False,
                                                domain=[0.15, 1]
                                            ),
                                        yaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=True,
                                                zeroline=False,
                                            ),
                                        margin=go.layout.Margin(l=10, r=10, t=10, b=10)
                                        )
                                }                  
                            )
                        ]),
                
                width=4, className='card',  style={"width": "31%"},                  
                ),

            dbc.Col(
                html.H3(["Palabras Neutras del Post X",
                    dcc.Graph(id='bar_neu_1',
                        figure={
                                'data': [go.Bar(x=[21, 57, 141, 202, 393, 454, 512], 
                                         y=['Normal', 'Pido', 'Agua', 'Seguridad', 'Ayuda', 'olvidar', 'cuando'],
                                         orientation='h',
                                         text=[21, 57, 141, 202, 393, 454, 512], #cuando se le este agragando datos colocar porcentajes tambien
                                         textposition = 'auto',
                                         marker = dict(
                                                    color = '#F2F2F2',
                                                    line = dict(
                                                            color = '#C1C1C1',
                                                            width = 1))
                                                    
                                         )],
                                'layout':go.Layout(
                                        xaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=False,
                                                zeroline=False,
                                                domain=[0.15, 1]
                                            ),
                                        yaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=True,
                                                zeroline=False,
                                            ),
                                        margin=go.layout.Margin(l=10, r=10, t=10, b=10)
                                        )
                                }                  
                        ), ]),width=4, className='card', style={"width": "31%"},
                ),

            
            dbc.Col(
                html.H3(["Palabras Positivas del Post X",
                    dcc.Graph(id='bar_neg_1',
                        figure={
                                'data': [go.Bar(x=[21, 22, 57, 59, 141, 155, 202, 264, 393, 420, 454, 500, 512, 600], 
                                         y=['Dios', 'Dios2', 'Bendiga', 'Bendiga2', 'Amor', 'Amor2', 'Bien',  'Bien2', 'Amo',  'Amo2', 'Palante', 'Palante2', '100', '100%'],
                                         orientation='h',
                                         text=[21, 22, 57, 59, 141, 155, 202, 264, 393, 420, 454, 500, 512, 600], #cuando se le este agragando datos colocar porcentajes tambien
                                         textposition = 'auto',
                                         marker = dict(
                                                    color = '#0767A0',)
                                         )],
                                'layout':go.Layout(
                                        xaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=False,
                                                zeroline=False,
                                                domain=[0.15, 1]
                                            ),
                                        yaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=True,
                                                zeroline=False,
                                            ),
                                       margin=go.layout.Margin(l=10, r=50, t=10, b=10)
                                        )
                                }                  
                        ), ]),width=4, className='card', style={"width": "31%"},
                    ),
                                                         
            ], justify="between", no_gutters=False, align="center", style={"width": "100%"},),





        #Sentiment tw
        dbc.Row([
            dbc.Col(
                html.H3(["Sentiment Keyword_X",
                dcc.Graph(id='crossfilter-indicator-scatter',
                    figure={
                        'data': [
                            go.Pie(labels=['Positivo','Neutral','Negativo'], hoverinfo='label', textinfo='value+percent', 
                            values=[4500,2500,1053],
                            
                            marker=dict(colors= [ '#0767A0', '#F2F2F2', '#363860']))],
                        'layout':go.Layout(
                                #title='Sentiment',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0),
                                margin=go.layout.Margin(l=10, r=10, t=10, b=10)
                                
                                )                       
                            }                  
                        ), ]),width=12, className='card', style={"width": "100%"},
                    ),
                                                         
            ], justify="between", no_gutters=False, align="end", style={"width": "100%"},),

        dbc.Row([
            dbc.Col(
                html.H3(["Palabras mas usadas en mensajes Negativos del Keyword X",
                    dcc.Graph(id='bar_pos_3',
                        figure={
                                'data': [go.Bar(x=[21, 57, 141, 202, 393, 454, 512], 
                                         y=['Mal', 'Odio', 'Vete', 'Nunca', 'HDP', 'CDTM', 'RATA'],
                                         orientation='h',
                                         text=[21, 57, 141, 202, 393, 454, 512], #cuando se le este agragando datos colocar porcentajes tambien
                                         textposition = 'auto',
                                         marker = dict(
                                                    color = '#363860',)
                                         )],
                                'layout':go.Layout(
                                        xaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=False,
                                                zeroline=False,
                                                domain=[0.15, 1]
                                            ),
                                        yaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=True,
                                                zeroline=False,
                                            ),
                                        margin=go.layout.Margin(l=10, r=10, t=10, b=10)
                                        )
                                }                  
                            )
                        ]),
                
                width=4, className='card',  style={"width": "31%"},                  
                ),

            dbc.Col(
                html.H3(["Palabras mas usadas en mensajes Neutros del Keyword X",
                    dcc.Graph(id='bar_neu_3',
                        figure={
                                'data': [go.Bar(x=[21, 57, 141, 202, 393, 454, 512], 
                                         y=['Normal', 'Pido', 'Agua', 'Seguridad', 'Ayuda', 'olvidar', 'cuando'],
                                         orientation='h',
                                         text=[21, 57, 141, 202, 393, 454, 512], #cuando se le este agragando datos colocar porcentajes tambien
                                         textposition = 'auto',
                                         marker = dict(
                                                    color = '#F2F2F2',
                                                    line = dict(
                                                            color = '#C1C1C1',
                                                            width = 1))
                                                    
                                         )],
                                'layout':go.Layout(
                                        xaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=False,
                                                zeroline=False,
                                                domain=[0.15, 1]
                                            ),
                                        yaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=True,
                                                zeroline=False,
                                            ),
                                        margin=go.layout.Margin(l=10, r=10, t=10, b=10)
                                        )
                                }                  
                        ), ]),width=4, className='card', style={"width": "31%"},
                ),

            
            dbc.Col(
                html.H3(["Palabras mas usadas en mensajes positivos del Keyword X",
                    dcc.Graph(id='bar_neg_3',
                        figure={
                                'data': [go.Bar(x=[21, 22, 57, 59, 141, 155, 202, 264, 393, 420, 454, 500, 512, 600], 
                                         y=['Dios', 'Dios2', 'Bendiga', 'Bendiga2', 'Amor', 'Amor2', 'Bien',  'Bien2', 'Amo',  'Amo2', 'Palante', 'Palante2', '100', '100%'],
                                         orientation='h',
                                         text=[21, 22, 57, 59, 141, 155, 202, 264, 393, 420, 454, 500, 512, 600], #cuando se le este agragando datos colocar porcentajes tambien
                                         textposition = 'auto',
                                         marker = dict(
                                                    color = '#0767A0',)
                                         )],
                                'layout':go.Layout(
                                        xaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=False,
                                                zeroline=False,
                                                domain=[0.15, 1]
                                            ),
                                        yaxis=dict(
                                                showgrid=False,
                                                showline=False,
                                                showticklabels=True,
                                                zeroline=False,
                                            ),
                                       margin=go.layout.Margin(l=10, r=50, t=10, b=10)
                                        )
                                }                  
                        ), ]),width=4, className='card', style={"width": "31%"},
                    ),
                                                         
            ], justify="between", no_gutters=False, align="center", style={"width": "100%"},),
    
    ], className='contenido',)
    
])

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse-1", "is_open"),
    [Input("collapse-button-1", "n_clicks")],
    [State("collapse-1", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse-f", "is_open"),
    [Input("collapse-button-f", "n_clicks")],
    [State("collapse-f", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse-2", "is_open"),
    [Input("collapse-button-2", "n_clicks")],
    [State("collapse-2", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse-i", "is_open"),
    [Input("collapse-button-i", "n_clicks")],
    [State("collapse-i", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse-3", "is_open"),
    [Input("collapse-button-3", "n_clicks")],
    [State("collapse-3", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
