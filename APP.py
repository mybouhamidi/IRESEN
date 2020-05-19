# -*- coding: utf-8 -*-
import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
import base64
import pandas as pd
from pandas import *

#définition des images à afficher
#image iresen
image_filename = 'Iresen.png'
encoded_image = base64.b64encode(open(image_filename,'rb').read())

#image capteur de temp
temp = 'temp.png'
encoded_image3 = base64.b64encode(open(temp,'rb').read())

#image capteur d'humidité du sol
moist = 'moisture.png'
encoded_image4 = base64.b64encode(open(moist,'rb').read())

#image capteur CO2
co2 = 'CO2.png'
encoded_image5 = base64.b64encode(open(co2,'rb').read())

#image capteur Ensoleillement
light = 'ensoleillement.png'
encoded_image6 = base64.b64encode(open(light,'rb').read())

#image capteur température et humidité de l'air
both = 'temp and humidity.png'
encoded_image7 = base64.b64encode(open(both,'rb').read())

#image des domaines
imaege_fil = 'domaines.png'
encoded_image1 = base64.b64encode(open(imaege_fil,'rb').read())

#image logo
imaege_fil1 = 'logo.png'
encoded_image2 = base64.b64encode(open(imaege_fil1,'rb').read())

#image de la serre
serre = 'serre.png'
encoded_image8 = base64.b64encode(open(serre,'rb').read())

#image emplacement des capteurs de temp dans la serre
temps = 'serre temp.png'
encoded_image9 = base64.b64encode(open(temps,'rb').read())

#image emplacement des capteurs d'humidité du sol dans la serre
moists = 'serre moist.png'
encoded_image10 = base64.b64encode(open(moists,'rb').read())

#image emplacement des capteurs d'humidité et température de l'air dans la serre
boths = 'serre both.png'
encoded_image11 = base64.b64encode(open(boths,'rb').read())

#image emplacement des capteurs de CO2 dans la serre
cos = 'serre co.png'
encoded_image12 = base64.b64encode(open(cos,'rb').read())

#image emplacement des capteurs d'ensoleillement dans la serre
ensos = 'serre enso.png'
encoded_image13 = base64.b64encode(open(ensos,'rb').read())

#lecture et initialisation des données
df = pd.read_csv('data.csv', delimiter=',', names=['year','temperature','moisture','humidity','state'])
df = DataFrame(df, columns=['year','temperature','moisture','humidity','state'])
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#styles des onglets utilisés
tab_style = {
    'border': '1px solid #111111',
    'background':'#111111',
    'color':'#7FDBFF',
    'margin-left': 20,
    'margin-right': 20,
    'padding': '6px'
}
tab_selected_style = {
    'borderBottom': '2px solid #7FDBFF',
    'borderRight': '1px solid #111111',
    'margin-left': 20,
    'margin-right': 20,
    'borderLeft' : '1px solid #111111',
    'borderTop': '1px solid #111111',
    'backgroundColor': '#272a2e',
    'color': '#7FDBFF',
    'padding': '6px',
    'fontWeight':'bold'
}
tab_style1 = {
    'border': '1px solid #111111',
    'background':'#111111',
    'margin-left': 20,
    'margin-right': 20,
    'color':'#f5f6f7',
    'padding': '6px',
    'fontWeight':'bold'
}
tab_selected_style1 = {
    'borderBottom': '2px solid white',
    'borderRight': '1px solid #111111',
    'borderLeft' : '1px solid #111111',
    'borderTop': '1px solid #111111',
    'margin-left': 20,
    'margin-right': 20,
    'backgroundColor': '#272a2e',
    'color': '#f5f6f7',
    'padding': '6px',
    'fontWeight':'bold'
}

#initialisation de la page dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {'background' : '#1d242e',
          'text': '#7FDBFF'}

#visualisation de la page
app.layout = html.Div(
      style={'backgroundColor': colors['background']},
      children=[
          html.Div([
              html.Div([
                  html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()),
                           className='three columns',
                           style={
                               'height': '10%',
                               'width': '10%',
                               'float': 'left',
                               'position': 'relative',
                               'backgroundColor': colors['background'],
                               'margin-top': 20,
                               'margin-left': 20,
                           },
                           ),
                  html.H1(children='Interface graphique pour serre intelligente',
                          className='six columns',
                          style={
                               'textAlign': 'center',
                               'color': colors['text'],
                              }),
                  html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                           className='three columns',
                           style={
                                 'height':'10%',
                                 'width':'10%',
                                 'float':'right',
                                 'position':'relative',
                                 'backgroundColor': colors['background'],
                                 'margin-top':50,
                                 'margin-right':20,
                                 },
                           ),
                  html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()),
                           className='three columns',
                           style={
                               'height': '10%',
                               'width': '10%',
                               'float': 'right',
                               'position': 'relative',
                               'margin-top':20,
                               'margin_right':20,
                               'backgroundColor': colors['background'],
                           },
                           ),
                  html.H6(children='Visualisation des paramètres avec un serveur local',
                          className='six columns',
                          style={
                               'textAlign': 'center',
                               'color': colors['text'],
                              }),
                  ],className='row flex-display'
              ), ]),
          html.Div([
              html.Div([
                  dcc.Tabs(id='tabs', value='tab_1', children=[
                      dcc.Tab(label='Vue générale',value= 'tab_1', style=tab_style1, selected_style=tab_selected_style1, children=[
                              html.Div([
                                  html.H2(children='''
                                            Image de la serre 
                                             ''',
                                          className='six columns',
                                          style={
                                              'textAlign': 'center',
                                              'color': colors['text']
                                          }),
                                  html.H2(children='''
                                        Valeur des capteurs 
                                            ''',
                                          className='six columns',
                                          style={
                                              'textAlign': 'center',
                                              'color': colors['text']
                                          }),
                              ],className=' flex-display'),
                              html.Div([
                                  html.Img(src='data:image/png;base64,{}'.format(encoded_image8.decode()),
                                           className='six columns',
                                           style={
                                               'height': '240%',
                                               'width': '90%',
                                               'float': 'left',
                                               'position': 'relative',
                                               'margin-top':60,
                                               'margin-left':0,
                                               'backgroundColor': colors['background'],
                                           },
                                           ),
                              ], className='six columns'),
                              html.Div([
                                  html.Div([
                                      daq.Gauge(
                                      id='ex1',
                                      label='Humidité du sol',
                                      value = df.loc[191,'moisture'],
                                      max = 100,
                                      min = 0,
                                      style={'textAlign': 'center',
                                             'color': colors['text']},
                                      showCurrentValue=True,
                                      units='%',
                                      color='#0774e0',
                                      size = 200,
                                      scale={'start':0, 'interval': 5}),
                                  ], className='two columns'),
                                  html.Div([
                                      daq.Gauge(
                                      id='ex3',
                                      label='Température du sol',
                                      value = df.loc[191,'temperature'],
                                      max = 100,
                                      min = 0,
                                      style={'textAlign': 'center',
                                             'color': colors['text']},
                                      showCurrentValue=True,
                                      units='°C',
                                      color='#ff5714',
                                      size = 200,
                                      scale={'start':0, 'interval': 5}),
                              ], className='two columns'),
                                  html.Div([
                                  daq.Gauge(
                                      id='ex2',
                                      label='Température ambiante',
                                      style={'textAlign': 'center',
                                             'color': colors['text'],
                                             'margin-right':40},
                                      value=df.loc[191, 'temperature'],
                                      max=100,
                                      min=0,
                                      showCurrentValue=True,
                                      units='°C',
                                      color='#ed3700',
                                      size=200,
                                      scale={'start': 0, 'interval': 5}
                                    ),
                              ],className= 'two columns'),]),
                              html.Div([
                                  html.Div([
                                  daq.Gauge(
                                      id='ex4',
                                      label='Ensoleillement',
                                      value=80,
                                      max=100,
                                      min=0,
                                      style={'textAlign': 'center',
                                             'color': colors['text']},
                                      showCurrentValue=True,
                                      units='%',
                                      color='#ffb619',
                                      size=200,
                                      scale={'start': 0, 'interval': 5}),
                              ], className='two columns'),
                                  html.Div([
                                  daq.Gauge(
                                      id='ex5',
                                      label='CO2',
                                      value=10,
                                      max=100,
                                      min=0,
                                      style={'textAlign': 'center',
                                             'color': colors['text']},
                                      showCurrentValue=True,
                                      units='mg/L',
                                      color='#706f6e',
                                      size=200,
                                      scale={'start': 0, 'interval': 5}),
                                  ], className='two columns'), ]),
                                  html.Div([
                                  daq.Gauge(
                                      id='ex6',
                                      label='Humidité relative',
                                      style={'textAlign': 'center',
                                             'color': colors['text'],
                                             'margin-right':40},
                                      value=df.loc[191, 'humidity'],
                                      max=100,
                                      min=0,
                                      showCurrentValue=True,
                                      units='%',
                                      color='#02ebe3',
                                      size=200,
                                      scale={'start': 0, 'interval': 5}
                                  ),
                              ], className='two columns'
                                  )],className='row flex-display'),
                      dcc.Tab(label='Humidité du sol', style=tab_style, selected_style=tab_selected_style, children=[
                          html.Div(
                              [
                                  html.Div(
                                      [
                                          html.Div([
                                              html.H4(children='''
                                              Emplacement des capteurs
                                              ''',
                                              className='three columns',
                                              style={
                                                 'textAlign': 'right',
                                                 'color': colors['text']
                                      }),
                                              html.H4(children='''
                                              Humidité du sol
                                              ''',
                                              className='six columns',
                                              style={
                                                  'textAlign' : 'center',
                                                  'color': colors['text']
                                      }),
                                              html.H4(children='''
                                              Image du capteur 
                                                ''',
                                                      className='three columns',
                                                      style={
                                                          'color': colors['text']
                                                      }),
                                          ],)]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image10.decode()),
                                                       className='three columns',
                                                       style={
                                                           'height':'150%',
                                                           'width':'125%',
                                                           'float':'left',
                                                           'position':'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top':20,
                                                           'margin-left':20,
                                                       },
                                                       ),
                                         ], className='three columns'),]),
                                  html.Div(
                                      [
                                          html.Div([
                                              daq.Gauge(
                                                 id='ex7',
                                                 value = df.loc[191,'moisture'],
                                                 max = 100,
                                                 min = 0,
                                                 style={'textAlign': 'center',
                                                        'color': colors['text']},
                                                 showCurrentValue=True,
                                                 units='%',
                                                 color='#0774e0',
                                                 size = 200,
                                                 scale={'start':0, 'interval': 5}),
                                         ], className='seven columns'),]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode()),
                                                       className='two columns',
                                                       style={
                                                           'height':'100%',
                                                           'width':'100%',
                                                           'float':'right',
                                                           'position':'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top':20,
                                                           'margin-right':20,
                                                       },
                                                       ),
                                         ], className='two columns'),]),
                                          html.Div([
                                              dcc.Graph(id='graph1',
                                                     figure ={
                                                       'data': [
                                                        {'x': df['year'], 'y': df['moisture'], 'type': 'bar'},
                                                    ],
                                                       'layout' : {
                                                           'title' : 'Humidité du sol VS Temps',
                                                           'xaxis' : dict(
                                                              title= 'Temps',
                                                              titlefont=dict(
                                                              family = 'Arial',
                                                              size = 20,
                                                              color = '#7FDBFF'
                                                           )),
                                                           'yaxis' : dict(
                                                              title= 'Humidité du sol',
                                                              titlefont=dict(
                                                              family = 'Arial',
                                                              size = 20,
                                                              color = '#7FDBFF'
                                                           )),
                                                           'plot_bgcolor': colors['background'],
                                                           'paper_bgcolor': colors['background'],
                                                           'font': {
                                                            'color': colors['text']
                                                            }
                                    }
                        }
                        )],className= 'twelve columns'),]),]),
                      dcc.Tab(label='Température du sol', style=tab_style, selected_style=tab_selected_style, children=[
                          html.Div(
                              [
                                  html.Div(
                                      [
                                          html.Div([
                                              html.H4(children='''
                                                      Emplacement des capteurs
                                                                         ''',
                                                      className='three columns',
                                                      style={
                                                          'textAlign': 'right',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      Température du sol
                                                      ''',
                                                      className='six columns',
                                                      style={
                                                          'textAlign': 'center',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      Image du capteur 
                                                       ''',
                                                      className='three columns',
                                                      style={
                                                          'color': colors['text']
                                                      }),
                                 ], className='twelve columns')]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image9.decode()),
                                                       className='three columns',
                                                       style={
                                                           'height':'150%',
                                                           'width':'125%',
                                                           'float':'left',
                                                           'position':'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top':20,
                                                           'margin-left':20,
                                                       },
                                                       ),
                                          ], className='three columns'), ]),
                                  html.Div(
                                      [
                                          html.Div([
                                              daq.Thermometer(
                                                 id='ex8',
                                                 style={'textAlign': 'center',
                                                        'color': colors['text']},
                                                 value= df.loc[191, 'temperature'],
                                                 max=100,
                                                 min=0,
                                                 showCurrentValue=True,
                                                 units='°C',
                                                 color='#ff5714',
                                                 size=200,
                                                 scale={'start': 0, 'interval': 5}),
                                          ], className='seven columns'), ]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode()),
                                                       className='two columns',
                                                       style={
                                                           'height':'100%',
                                                           'width':'100%',
                                                           'float':'right',
                                                           'position':'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top':20,
                                                           'margin-right': 20,
                                                       },
                                                       ),
                                         ], className='two columns'),]),
                                          html.Div([
                                              dcc.Graph(id='graph2',
                                                        figure={'data':
                                                            [
                                                                {'x': df['year'], 'y': df['temperature'],
                                                                 'type': 'bar'},
                                                            ],
                                                            'layout': {
                                                                'title': 'Température du sol vs Temps',
                                                                'xaxis': dict(
                                                                    title='Temps',
                                                                    titlefont=dict(
                                                                        family='Arial',
                                                                        size=20,
                                                                        color='#7FDBFF'
                                                                    )),
                                                                'yaxis': dict(
                                                                    title='Température du sol',
                                                                    titlefont=dict(
                                                                        family='Arial',
                                                                        size=20,
                                                                        color='#7FDBFF'
                                                                    )),
                                                                'plot_bgcolor': colors['background'],
                                                                'paper_bgcolor': colors['background'],
                                                                'font': {
                                                                    'color': colors['text']
                                                                }
                                                            }
                                                        }
                        )],className= 'twelve columns'),]),]),
                      dcc.Tab(label='Température ambiante', style=tab_style, selected_style=tab_selected_style, children=[
                          html.Div(
                              [
                                  html.Div(
                                      [
                                          html.Div([
                                              html.H4(children='''
                                                      Emplacement des capteurs
                                                                         ''',
                                                      className='three columns',
                                                      style={
                                                          'textAlign': 'right',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      Température ambiante
                                                      ''',
                                                      className='six columns',
                                                      style={
                                                          'textAlign': 'center',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      Image du capteur 
                                                       ''',
                                                      className='three columns',
                                                      style={
                                                          'color': colors['text']
                                                      }),
                                 ], className='twelve columns')]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image11.decode()),
                                                       className='three columns',
                                                       style={
                                                           'height':'150%',
                                                           'width':'125%',
                                                           'float':'left',
                                                           'position':'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top':20,
                                                           'margin-left':20,
                                                       },
                                                       ),
                                          ], className='three columns'), ]),
                                  html.Div(
                                      [
                                          html.Div([
                                              daq.Thermometer(
                                                 id='ex9',
                                                  value=df.loc[191, 'temperature'],
                                                  max=100,
                                                  min=0,
                                                  style={'textAlign': 'center',
                                                         'color': colors['text']},
                                                  showCurrentValue=True,
                                                  units='°C',
                                                  color='#ed3700',
                                                  size=200,
                                                  scale={'start': 0, 'interval': 5}),
                                          ], className='seven columns'), ]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image7.decode()),
                                                       className='two columns',
                                                       style={
                                                           'height':'100%',
                                                           'width':'100%',
                                                           'float':'right',
                                                           'position':'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top':20,
                                                           'margin-right':20,
                                                       },
                                                       ),
                                         ], className='two columns'),]),
                                          html.Div([
                                              dcc.Graph(id='graph3',
                                                        figure={'data':
                                                            [
                                                                {'x': df['year'], 'y': df['temperature'],
                                                                 'type': 'bar'},
                                                            ],
                                                            'layout': {
                                                                'title': 'Température ambiante vs Temps',
                                                                'xaxis': dict(
                                                                    title='Temps',
                                                                    titlefont=dict(
                                                                        family='Arial',
                                                                        size=20,
                                                                        color='#7FDBFF'
                                                                    )),
                                                                'yaxis': dict(
                                                                    title='Température ambiante',
                                                                    titlefont=dict(
                                                                        family='Arial',
                                                                        size=20,
                                                                        color='#7FDBFF'
                                                                    )),
                                                                'plot_bgcolor': colors['background'],
                                                                'paper_bgcolor': colors['background'],
                                                                'font': {
                                                                    'color': colors['text']
                                                                }
                                                            }
                                                        }
                        )],className= 'twelve columns'),]),]),
                      dcc.Tab(label='Ensoleillement', style=tab_style, selected_style=tab_selected_style, children=[
                          html.Div(
                              [
                                  html.Div(
                                      [
                                          html.Div([
                                              html.H4(children='''
                                                      Emplacement des capteurs
                                                      ''',
                                                      className='three columns',
                                                      style={
                                                          'textAlign': 'right',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      Ensoleillement
                                                       ''',
                                                      className='six columns',
                                                      style={
                                                          'textAlign': 'center',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      Image du capteur 
                                                        ''',
                                                      className='three columns',
                                                      style={
                                                          'color': colors['text']
                                                      }),
                                 ], className='twelve columns')]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image13.decode()),
                                                       className='three columns',
                                                       style={
                                                           'height': '150%',
                                                           'width': '125%',
                                                           'float': 'left',
                                                           'position': 'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top': 20,
                                                           'margin-left': 20,
                                                       },
                                                       ),
                                          ], className='three columns'), ]),
                                  html.Div(
                                      [
                                          html.Div([
                                              daq.Gauge(
                                                  id='ex10',
                                                  value=80,
                                                  max=100,
                                                  min=0,
                                                  style={'textAlign': 'center',
                                                         'color': colors['text']},
                                                  showCurrentValue=True,
                                                  units='%',
                                                  color='#ffb619',
                                                  size=200,
                                                  scale={'start': 0, 'interval': 5}),
                                          ], className='seven columns'), ]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image6.decode()),
                                                       className='two columns',
                                                       style={
                                                           'height':'100%',
                                                           'width':'100%',
                                                           'float':'right',
                                                           'position':'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top':20,
                                                           'margin-right':20,
                                                       },
                                                       ),
                                         ], className='two columns'),]),
                                  html.Div([
                                      dcc.Graph(id='graph4',
                                                figure={'data':
                                                    [
                                                        {'x': df['year'], 'y': df['temperature'],
                                                         'type': 'bar'},
                                                    ],
                                                    'layout': {
                                                        'title': 'Ensoleillement vs Temps',
                                                        'xaxis': dict(
                                                            title='Temps',
                                                            titlefont=dict(
                                                                family='Arial',
                                                                size=20,
                                                                color='#7FDBFF'
                                                            )),
                                                        'yaxis': dict(
                                                            title='Ensoleillement',
                                                            titlefont=dict(
                                                                family='Arial',
                                                                size=20,
                                                                color='#7FDBFF'
                                                            )),
                                                        'plot_bgcolor': colors['background'],
                                                        'paper_bgcolor': colors['background'],
                                                        'font': {
                                                            'color': colors['text']
                                                        }
                                                    }
                                                }
                                                )], className='twelve columns'), ]), ]),
                      dcc.Tab(label='CO2', style=tab_style, selected_style=tab_selected_style, children=[
                          html.Div(
                              [
                                  html.Div(
                                      [
                                          html.Div([
                                              html.H4(children='''
                                                      Emplacement des capteurs
                                                       ''',
                                                      className='three columns',
                                                      style={
                                                          'textAlign': 'right',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      CO2
                                                      ''',
                                                      className='six columns',
                                                      style={
                                                          'textAlign': 'center',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      Image du capteur 
                                                       ''',
                                                      className='three columns',
                                                      style={
                                                          'color': colors['text']
                                                      }),
                                 ], className='twelve columns')]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image12.decode()),
                                                       className='three columns',
                                                       style={
                                                           'height': '150%',
                                                           'width': '125%',
                                                           'float': 'left',
                                                           'position': 'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top': 20,
                                                           'margin-left': 20,
                                                       },
                                                       ),
                                          ], className='three columns'), ]),
                                  html.Div(
                                      [
                                          html.Div([
                                              daq.Gauge(
                                                 id='ex13',
                                                 value = 10,
                                                 max = 100,
                                                 min = 0,
                                                 style={'textAlign': 'center',
                                                        'color': colors['text']},
                                                 showCurrentValue=True,
                                                 units='mg/L',
                                                 color='#706f6e',
                                                 size = 200,
                                                 scale={'start':0, 'interval': 5}),
                                         ], className='seven columns'),]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode()),
                                                       className='two columns',
                                                       style={
                                                           'height':'100%',
                                                           'width':'100%',
                                                           'float':'right',
                                                           'position':'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top':20,
                                                           'margin-right':20,
                                                       },
                                                       ),
                                         ], className='two columns'),]),
                                          html.Div([
                                              dcc.Graph(id='graph6',
                                                     figure ={
                                                       'data': [
                                                        {'x': df['year'], 'y': df['moisture'], 'type': 'bar'},
                                                    ],
                                                       'layout' : {
                                                           'title' : 'CO2 VS Temps',
                                                           'xaxis' : dict(
                                                              title= 'Temps',
                                                              titlefont=dict(
                                                              family = 'Arial',
                                                              size = 20,
                                                              color = '#7FDBFF'
                                                           )),
                                                           'yaxis' : dict(
                                                              title= 'CO2',
                                                              titlefont=dict(
                                                              family = 'Arial',
                                                              size = 20,
                                                              color = '#7FDBFF'
                                                           )),
                                                           'plot_bgcolor': colors['background'],
                                                           'paper_bgcolor': colors['background'],
                                                           'font': {
                                                            'color': colors['text']
                                                            }
                                    }
                        }
                        )],className= 'twelve columns'),]),]),
                      dcc.Tab(label='Humidité relative', style=tab_style, selected_style=tab_selected_style, children=[
                          html.Div(
                              [
                                  html.Div(
                                      [
                                          html.Div([
                                              html.H4(children='''
                                                      Emplacement des capteurs
                                                       ''',
                                                      className='three columns',
                                                      style={
                                                          'textAlign': 'right',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      Humidité relative
                                                      ''',
                                                      className='six columns',
                                                      style={
                                                          'textAlign': 'center',
                                                          'color': colors['text']
                                                      }),
                                              html.H4(children='''
                                                      Image du capteur 
                                                      ''',
                                                      className='three columns',
                                                      style={
                                                          'color': colors['text']
                                                      }),
                                 ], className='twelve columns')]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image11.decode()),
                                                       className='three columns',
                                                       style={
                                                           'height': '150%',
                                                           'width': '125%',
                                                           'float': 'left',
                                                           'position': 'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top': 20,
                                                           'margin-left': 20,
                                                       },
                                                       ),
                                          ], className='three columns'), ]),
                                  html.Div(
                                      [
                                          html.Div([
                                              daq.Gauge(
                                                  id='ex12',
                                                  style={'textAlign': 'center',
                                                         'color': colors['text']},
                                                  value=df.loc[191, 'humidity'],
                                                  max=100,
                                                  min=0,
                                                  showCurrentValue=True,
                                                  units='%',
                                                  color='#02ebe3',
                                                  size=200,
                                                  scale={'start': 0, 'interval': 5}
                                              ),
                                          ], className='seven columns')]),
                                  html.Div(
                                      [
                                          html.Div([
                                              html.Img(src='data:image/png;base64,{}'.format(encoded_image7.decode()),
                                                       className='two columns',
                                                       style={
                                                           'height':'100%',
                                                           'width':'100%',
                                                           'float':'right',
                                                           'position':'relative',
                                                           'backgroundColor': colors['background'],
                                                           'margin-top':20,
                                                           'margin-right':20,
                                                       },
                                                       ),
                                         ], className='two columns'),]),
                                  html.Div([
                                      dcc.Graph(id='graph5',
                                                figure={'data':
                                                    [
                                                        {'x': df['year'], 'y': df['humidity'],
                                                         'type': 'bar'},
                                                    ],
                                                    'layout': {
                                                        'title': 'Humidité relative VS Temps',
                                                        'xaxis': dict(
                                                            title='Temps',
                                                            titlefont=dict(
                                                                family='Arial',
                                                                size=20,
                                                                color='#7FDBFF'
                                                            )),
                                                        'yaxis': dict(
                                                            title='Humidité relative',
                                                            titlefont=dict(
                                                                family='Arial',
                                                                size=20,
                                                                color='#7FDBFF'
                                                            )),
                                                        'plot_bgcolor': colors['background'],
                                                        'paper_bgcolor': colors['background'],
                                                        'font': {
                                                            'color': colors['text']
                                                        }
                                                    }
                                                }
                                                )], className='twelve columns'), ]), ]),
                                  ])
                          ])
                      ])
      ])

if __name__ == '__main__':
    app.run_server(debug=True)