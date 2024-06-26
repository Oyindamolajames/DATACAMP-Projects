import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'

app = dash.Dash(__name__)

app.layout = html.Div([
  html.Img(src=logo_link,style={'margin':'30px 0px 0px 0px' }),
  html.H1('Sales breakdowns'),
  html.Div(
    children=[
    html.Div(
        children=[
        html.H2('Controls'),
        html.Br(),
        html.H3('Country Select'),
        dcc.Dropdown(id='country_dd',
        options=[
            {'label':'UK', 'value':'United Kingdom'},
            {'label':'GM', 'value':'Germany'},
            {'label':'FR', 'value':'France'},
            {'label':'AUS', 'value':'Australia'},
            {'label':'HK', 'value':'Hong Kong'}],
            style={'width':'200px', 'margin':'0 auto'})
        ],
        style={'width':'350px', 'height':'350px', 'display':'inline-block', 'vertical-align':'top', 'border':'1px solid black', 'padding':'20px'}),
    html.Div(children=[
            dcc.Graph(id='major_cat'),
            html.H2('Major Category', 
            style={ 'border':'2px solid black', 'width':'200px', 'margin':'0 auto'})
            ],
             style={'width':'700px','display':'inline-block'}
             ),
    ])], 
  style={'text-align':'center', 'display':'inline-block', 'width':'100%'}
  )
@app.callback(
    Output(component_id='major_cat', component_property='figure'),
    Input(component_id='country_dd', component_property='value')
)

def update_plot(input_country):
    # Set a default value
    country_filter = 'All Countries'
    # Ensure the DataFrame is not overwritten
    sales = ecom_sales.copy(deep=True)
    # Create a conditional to filter the DataFrame if the input exists
    if input_country:
        country_filter = input_country
        sales = sales[sales['Country'] == country_filter]
    ecom_bar_major_cat = sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
    bar_fig_major_cat = px.bar(
        title=f'Sales in {country_filter}', data_frame=ecom_bar_major_cat, x='Total Sales ($)', y='Major Category', color='Major Category',
                 color_discrete_map={'Clothes':'blue','Kitchen':'red','Garden':'green','Household':'yellow'})
   	# Return the figure
    return bar_fig_major_cat


if __name__ == '__main__':
    app.run_server(debug=True)


    import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from datetime import datetime, date
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_sales['InvoiceDate'] = pd.to_datetime(ecom_sales['InvoiceDate'])

app = dash.Dash(__name__)

def make_break(num_breaks):
    br_list = [html.Br()] * num_breaks
    return br_list

def add_logo():
    corp_logo = html.Img(
        src=logo_link, 
        style={'margin':'20px 20px 5px 5px',
              'border':'1px dashed lightblue',
              'display':'inline-block'})
    return corp_logo

# Create a function to add corporate styling
def style_c():
    layout_style={'display':'inline-block','margin':'0 auto','padding':'20px'}
    return layout_style

app.layout = html.Div([
  add_logo(),
  # Insert two HTML breaks
  *make_break(2),
  html.H1('Sales breakdowns'),
  # Insert three HTML breaks
  *make_break(3),
  html.Div(
    children=[
    html.Div(
        children=[
        add_logo(),
        # Style using the styling function
        html.H2('Controls', style=style_c()),
        add_logo(),
        html.H3('Sale Date Select'),
        # Insert two HTML breaks
        *make_break(2),
        dcc.DatePickerSingle(
            id='sale_date',
            min_date_allowed=ecom_sales.InvoiceDate.min(),
            max_date_allowed=ecom_sales.InvoiceDate.max(),
            initial_visible_month=date(2011,4,1),
            date=date(2011,4,11),
          	# Add styling using the styling function
            style={'width':'200px'}.update(style_c())),
        ],
        style={'width':'550px', 'height':'350px', 'vertical-align':'top', 'border':'1px solid black',
        'display':'inline-block', 'margin':'0px 40px'}),
    html.Div(children=[
            dcc.Graph(id='sales_cat'),
            html.H2('Daily Sales by Major Category', 
            style={ 'border':'2px solid black', 'width':'400px', 'margin':'0 auto'})
            ],
             style={'width':'700px','display':'inline-block'}
             ),
    ]),
    add_logo(),
    ], 
  style={'text-align':'center', 'display':'inline-block', 'width':'100%'}
  )

@app.callback(
    Output(component_id='sales_cat', component_property='figure'),
    Input(component_id='sale_date', component_property='date')
)
def update_plot(input_date):
    
    sales = ecom_sales.copy(deep=True)

    if input_date:
        sales = sales[sales['InvoiceDate'] == input_date]

    ecom_bar_major_cat = sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')

    bar_fig_major_cat = px.bar(
        title=f'Sales on: {input_date}',data_frame=ecom_bar_major_cat, orientation='h', 
        x='Total Sales ($)', y='Major Category')

    return bar_fig_major_cat


if __name__ == '__main__':
    app.run_server(debug=True)