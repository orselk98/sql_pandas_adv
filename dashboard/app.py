#imports 

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#import dataframes from analysis files

from analysis.territory_profit import df as territory_df
from analysis.customer_spending import df as customer_df
from analysis.product_performance import df as product_df
from analysis.top_sellers import df as sellers_df


#init app
app =dash.Dash(__name__)

#layout

app.layout =html.Div([
    html.H1("AdventureWorks Sales Dashboard"),
    html.H2("Territory Profit Margin"),
dcc.Graph(
    id='territory-profit-chart',
    figure=px.bar(
        territory_df,
        x='Name',
        y='ProfitPercentage',
        title='Profit Margin by Territory'
    )
),
    html.H2("Product Performace by Year"),
    dcc.Graph(
        id='product-performance-chart',
        figure=px.bar(
                product_df,
                x='orderyear',
                y='totalrevenue',
                color='Name',
                barmode='group',
                title='Product Revenue by Category and Year'
    )
),
    html.H2("Top customers by Territory"),
    dcc.Dropdown(
        id='territory-dropdown',
        options=[{'label': t, 'value': t} for t in customer_df['Name'].unique()],
        value='Australia'
    ),
    dcc.Graph(
        id='customer-spending-chart'
    
),
    html.H2("Top Sellers by Sales Revenue"),
    dcc.Graph(
        id='top-sellers-chart',
        figure=px.bar(
            sellers_df,
            x='LastName',
            y='TotalSales',
            title='Top Sellers by Sales Revenue'
        )
    )

    #section 1 - territory profit chart
    #section 2 - customer spending with dropdown
    #section 3 - product performace chart
    #section 4 - top sellers chart
])

#callbacks for interactive charts
@app.callback(
    Output('customer-spending-chart','figure'),
    Input('territory-dropdown','value')
)
def update_customer_chart(selected_territory):
    filtered_df = customer_df[customer_df['Name']==selected_territory]
    fig=px.bar(
        filtered_df,
        x='LastName',
        y='TotalSpending',
        title=f'Top Customers in{selected_territory}'
    )
    return fig
#runn app

if __name__ == '__main__':
    app.run(debug=True)