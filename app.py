import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout =  html.Div(style={'backgroundColor':'#7FDBFF', 'columnCount': 1}, 
                       children=[html.Div(),                                     
                                          #Temperature
                                          html.Label('Temperature (C)'),
                                          html.Div(className='gap'),
                                          dcc.Input(id='T',value=25.0),
                                 
                                          #CoC
                                          html.Label('Cycles of Concentration'),
                                          html.Div(className='gap'),  
                                          dcc.Input(id='CoC',value=1),

                                          #Malk
                                          html.Label('M Alkalinity (mg/l as CaCO3)'),
                                          html.Div(className='gap'),  
                                          dcc.Input(id='Malk',value=30),  
                                          html.Div(className='gap'),
                                          html.Br(),   
                                          
                                          #Ca
                                          html.Label('Ca ion'),
                                          html.Div(className='gap'),  
                                          dcc.Input(id='Ca',value=10),

                                          #Mg
                                          html.Label('Mg ion'),
                                          html.Div(className='gap'),  
                                          dcc.Input(id='Mg',value=0),

                                          #Zn
                                          html.Label('Zn ion'),
                                          html.Div(className='gap'),  
                                          dcc.Input(id='Zn',value=0),

                                          #Na
                                          html.Label('Na ion'),
                                          html.Div(className='gap'),  
                                          dcc.Input(id='Na',value=0),

                                          html.Div(className='gap'), 
                                          html.Br(),

                                          #Cl
                                          html.Label('Cl ion'),
                                          html.Div(className='gap'),  
                                          dcc.Input(id='Cl',value=0),

                                          #SO4
                                          html.Label('SO4 ion'),
                                          html.Div(className='gap'),  
                                          dcc.Input(id='SO4',value=5),

                                          #PO4
                                          html.Label('PO4 ion'),
                                          html.Div(className='gap'),  
                                          dcc.Input(id='PO4',value=1),

                                          html.Div(className='gap'), 
                                          html.Br(),
                                 
                                          #Plotting Choice
                                          html.Label(["Plotting Choice",
                                                      dcc.Dropdown(id='forplots', style={'marginBottom': '1.5em','width': '50%'}, 
                                                                   clearable=False, value=2, 
                                                                   options=[{'label': 'CoC Plots', 'value': 2},
                                                                            {'label': 'Alkalinity Plots', 'value': 3},  
                                                                            {'label': 'Temperature Plots', 'value': 4}])
                                                      ]),  

                                          html.Button('Submit', id='button'),
                                          html.Br(),
                                          html.Div(id='output-container-button', children='Enter a value and press submit')
                                    ])

if __name__ == '__main__':
    app.run_server()
