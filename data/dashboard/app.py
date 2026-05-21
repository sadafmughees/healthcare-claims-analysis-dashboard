import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load Dataset
df = pd.read_csv("../data/claims_demo.csv")

# Create Dash App
app = Dash(__name__)

# Chart 1 - Claim Status
status_data = df['Status'].value_counts().reset_index()

status_data.columns = ['Status', 'Count']

status_chart = px.bar(
    status_data,
    x='Status',
    y='Count',
    title='Claim Approval Status'
)

# Chart 2 - Amount by Country
country_data = df.groupby(
    'Country'
)['Amount'].mean().reset_index()

country_chart = px.bar(
    country_data,
    x='Country',
    y='Amount',
    title='Average Claim Amount by Country'
)

# Fraud Demo Trend
df['Fraud_Rate'] = df['Amount'] > 8000

fraud_data = df.groupby(
    'Date'
)['Fraud_Rate'].mean().reset_index()

fraud_chart = px.line(
    fraud_data,
    x='Date',
    y='Fraud_Rate',
    title='Fraud Rate Trend'
)

# Dashboard Layout
app.layout = html.Div([

    html.H1(
        "UK Claims Analytics Dashboard",
        style={'textAlign': 'center'}
    ),

    dcc.Graph(figure=status_chart),

    dcc.Graph(figure=country_chart),

    dcc.Graph(figure=fraud_chart)

])

# Run App
if __name__ == '__main__':
    app.run(debug=True)