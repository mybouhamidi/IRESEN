import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

#lecture et initialisation des données
df = pd.read_csv('data.csv', delimiter=',', names=['year','temperature','moisture','humidity'])

def render_gauge(name, parameter, unit):
    return daq.Gauge(
      className= 'gauge',
      label = name,
      value = df.loc[len(df)-1, parameter],
      max = 100,
      min = 0,
      showCurrentValue = True,
      units = unit,
      color = {"gradient":True,"ranges":{"green":[0,60],"yellow":[60,80],"red":[80,100]}},
      scale = {'start':0, 'interval': 5},
      )

def render_graph(yvalue, label):
    return dcc.Graph(
      config={'displaylogo': False},
      figure ={ 'data': [{'x': df['year'], 'y': df[yvalue], 'type': 'bar'}],
                'layout' : {
                'title' : label + ' VS Temps',
                'xaxis' : dict(
                              title= 'Temps',
                              titlefont=dict(
                                            family = 'Arial',
                                            size = 20,
                                            color = '#7FDBFF'
                                        )
                          ),
                'yaxis' : dict(
                              title= label,
                              titlefont=dict(
                                            family = 'Arial',
                                            size = 20,
                                            color = '#7FDBFF'
                                        )
                          ),
                'plot_bgcolor': '#1d242e',
                'paper_bgcolor': '#1d242e',
                'font': {'color': '#7FDBFF'}                                                       
                }
              }
          )

#styles des onglets utilisés
tab_style = {
    'border': '1px solid #111111',
    'background':'#111111',
    'color':'#7FDBFF',
    'padding': '3px'
}
tab_selected_style = {
    'borderBottom': '2px solid #7FDBFF',
    'borderRight': '1px solid #111111',
    'borderLeft' : '1px solid #111111',
    'borderTop': '1px solid #111111',
    'backgroundColor': '#272a2e',
    'color': '#7FDBFF',
    'padding': '3px',
    'fontWeight':'bold'
}
main_tab_style = {
    'border': '1px solid #111111',
    'background':'#111111',
    'color':'#f5f6f7',
    'padding': '3px',
}
main_tab_selected = {
    'borderBottom': '2px solid white',
    'borderRight': '1px solid #111111',
    'borderLeft' : '1px solid #111111',
    'borderTop': '1px solid #111111',
    'backgroundColor': '#272a2e',
    'color': '#f5f6f7',
    'padding': '3px',
    'fontWeight':'bold'
}

          
#initialisation de la page dash
app = dash.Dash(__name__, 
             meta_tags=[{"name":"description","content":"my UI app"},{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app.title = "UI pour IRESEN"
server = app.server 


#visualisation de la page
app.layout =html.Div(
    [	
        html.Header(className="flex-display row", children=[
            html.Img(src=app.get_asset_url('domaines.webp'), className='icon', alt='icone des domaines'),
            html.Div(className='seven columns', children=[
                html.H1('Interface graphique pour serre intelligente', style={'textAlign': 'center', 'margin-top':'30px'}),
                html.Br(),
                html.H6('Visualisation des paramètres avec un serveur local', style={'textAlign': 'center', 'padding': 5}),
            ]),
            html.Img(src=app.get_asset_url("Iresen.webp"), className='icon_iresen', alt='icone IRESEN'),
        ]),
        html.Main([
            dcc.Tabs(value='tab_1', children=[
                dcc.Tab(label='Vue générale', value='tab_1', style= main_tab_style, selected_style= main_tab_selected, children=[
                    html.Div(className='six columns', children=[
                        html.H2(children='Image de la serre', className='twelve columns', style={'textAlign':'center'}),
                        html.Img(src=app.get_asset_url('serre.webp'), className='serre', alt='image de la serre'),
                    ]),
                    html.Div(className='six columns', children=[
                        html.H2(children='Valeur des capteurs', className='twelve columns', style={'textAlign':'center'}),
                        html.Div([
                        render_gauge('Humidité du sol', 'moisture', '%'),
                        render_gauge('Température du sol', 'temperature', '°C'),
                        render_gauge('Température ambiante', 'temperature', '°C'),
                        render_gauge('Ensoleillement','moisture', '%'),
                        render_gauge('CO2', 'humidity','mg/L'),
                        render_gauge('Humidité relative', 'humidity', '%'),
                        ])
                    ]),
                ]),
                dcc.Tab(label='Humidité du sol', style=tab_style, selected_style=tab_selected_style, children=[
                    html.Div(className= 'three columns', children=[
                        html.H4(children='Emplacement des capteurs',className='twelve columns', style={'margin-left':20,'textAlign': 'center'}),
                        html.Img(src=app.get_asset_url('serre moist.webp'), className='img_sensor', alt='image de la serre'),
                    ]),
                    html.Div(className='six columns', children=[
                        html.H4(children='Humidité du sol', style={'textAlign': 'center'}),
                        html.Div(className='offset-by-four columns',children=[
                            render_gauge('', 'moisture', '%')
                        ])
                    ]),
                    html.Div(className='three columns', children=[
                        html.H4(children='Image du capteur'),
                        html.Img(src=app.get_asset_url('moisture.webp'), className='img_capt', alt='image du capteur'),
                    ]),
                    html.Div(className='twelve columns', children=[
                            render_graph('moisture','Humidité du sol')
                    ])
                ]),
                dcc.Tab(label='Température du sol', style=tab_style, selected_style=tab_selected_style, children=[
                    html.Div(className= 'three columns', children=[
                        html.H4(children='Emplacement des capteurs', style={'textAlign': 'center', 'margin-left':20}),
                        html.Img(src=app.get_asset_url('serre temp.webp'), className='img_sensor', alt='image de la serre'),
                    ]),
                    html.Div(className='six columns', children=[
                        html.H4(children='Température du sol', style={'textAlign': 'center'}),
                        html.Div(className='offset-by-four columns',children=[
                            render_gauge('','temperature','°C')
                        ])
                    ]),
                    html.Div(className='three columns', children=[
                        html.H4(children='Image du capteur'),
                        html.Img(src=app.get_asset_url('temp.webp'), className='img_capt', alt='image du capteur'),
                    ]),
                    html.Div(className='twelve columns', children=[
                        render_graph('temperature','Température du sol')              
                    ])
                ]),
                dcc.Tab(label='Température ambiante', style=tab_style, selected_style=tab_selected_style, children=[
                    html.Div(className= 'three columns', children=[
                        html.H4(children='Emplacement des capteurs', style={'textAlign': 'center', 'margin-left':20}),
                        html.Img(src=app.get_asset_url('serre both.webp'), className='img_sensor', alt='image de la serre'),
                    ]),
                    html.Div(className='six columns', children=[
                        html.H4(children='Température ambiante', style={'textAlign': 'center'}),
                        html.Div(className='offset-by-four columns',children=[
                            render_gauge('','temperature','°C')
                        ])
                    ]),
                    html.Div(className='three columns', children=[
                        html.H4(children='Image du capteur'),
                        html.Img(src=app.get_asset_url('temp and humidity.webp'), className='img_capt', alt='image du capteur'),
                    ]),
                    html.Div(className='twelve columns', children=[
                        render_graph('temperature','Température ambiante')
                    ])
                ]),
                dcc.Tab(label='Ensoleillement', style=tab_style, selected_style=tab_selected_style, children=[
                    html.Div(className= 'three columns', children=[
                        html.H4(children='Emplacement des capteurs', style={'textAlign': 'center', 'margin-left':20}),
                        html.Img(src=app.get_asset_url('serre enso.webp'), className='img_sensor', alt='image de la serre'),
                    ]),
                    html.Div(className='six columns', children=[
                        html.H4(children='Ensoleillement', style={'textAlign': 'center'}),
                        html.Div(className='offset-by-four columns',children=[
                            render_gauge('','temperature','%')
                        ])
                    ]),
                    html.Div(className='three columns', children=[
                        html.H4(children='Image du capteur'),
                        html.Img(src=app.get_asset_url('ensoleillement.webp'), className='img_capt', alt='image du capteur'),
                    ]),
                    html.Div(className='twelve columns', children=[
                        render_graph('humidity','Ensoleillement')
                    ])
                ]),
                dcc.Tab(label='CO2', style=tab_style, selected_style=tab_selected_style, children=[
                    html.Div(className= 'three columns', children=[
                        html.H4(children='Emplacement des capteurs', style={'textAlign': 'center', 'margin-left':20}),
                        html.Img(src=app.get_asset_url('serre co.webp'), className='img_sensor', alt='image de la serre'),
                    ]),
                    html.Div(className='six columns', children=[
                        html.H4(children='CO2', style={'textAlign': 'center'}),
                        html.Div(className='offset-by-four columns',children=[
                            render_gauge('','moisture','%')
                        ])
                    ]),
                    html.Div(className='three columns', children=[
                        html.H4(children='Image du capteur'),
                        html.Img(src=app.get_asset_url('CO2.webp'), className='img_capt', alt='image du capteur'),
                    ]),
                    html.Div(className='twelve columns', children=[
                        render_graph('moisture','CO2')
                    ])
                ]),      
                dcc.Tab(label='Humidité relative', style=tab_style, selected_style=tab_selected_style, children=[
                    html.Div(className= 'three columns', children=[
                        html.H4(children='Emplacement des capteurs', style={'textAlign': 'center', 'margin-left':20}),
                        html.Img(src=app.get_asset_url('serre both.webp'), className='img_sensor', alt='image de la serre'),
                    ]),
                    html.Div(className='six columns', children=[
                        html.H4(children='Humidité relative', style={'textAlign': 'center'}),
                        html.Div(className='offset-by-four columns',children=[
                            render_gauge('','humidity','%')
                        ])
                    ]),
                    html.Div(className='three columns', children=[
                        html.H4(children='Image du capteur'),
                        html.Img(src=app.get_asset_url('temp and humidity.webp'), className='img_capt', alt='image du capteur'),
                    ]),
                    html.Div(className='twelve columns', children=[
                        render_graph('humidity','Humidité relative')
                    ])
                ]),        
        ])
    ])
])


if __name__ == '__main__':
    app.run_server(debug=False)