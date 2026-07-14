import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

# Load global df so we don't reload on every function call
_DF = None

def get_df():
    global _DF
    if _DF is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(base_dir, 'dataset', 'clean_customer_churn.csv')
        _DF = pd.read_csv(csv_path)
    return _DF

# Common premium dark theme configuration for Plotly
theme_config = {
    'template': 'plotly_dark',
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'font': {'family': 'Inter', 'color': '#cbd5e1'}
}

def plot_customer_distribution():
    df = get_df()
    churn_counts = df['Churn Label'].value_counts().reset_index()
    churn_counts.columns = ['Churn Label', 'Count']
    
    fig = px.pie(churn_counts, values='Count', names='Churn Label', hole=0.7,
                 color='Churn Label', color_discrete_map={'Yes': '#EF4444', 'No': '#10B981'})
    
    fig.update_layout(**theme_config, 
                      annotations=[dict(text='Churn<br>Distribution', x=0.5, y=0.5, font_size=20, showarrow=False)],
                      margin=dict(t=30, b=0, l=0, r=0))
    return fig

def plot_contract_distribution():
    df = get_df()
    contract_churn = df.groupby(['Contract', 'Churn Label']).size().reset_index(name='Count')
    
    fig = px.bar(contract_churn, x='Contract', y='Count', color='Churn Label', barmode='group',
                 color_discrete_map={'Yes': '#EF4444', 'No': '#10B981'})
    fig.update_layout(**theme_config, xaxis_title="", yaxis_title="Number of Customers", margin=dict(t=10, b=0, l=0, r=0))
    return fig

def plot_monthly_charges():
    df = get_df()
    fig = px.histogram(df, x='Monthly Charges', color='Churn Label', nbins=40,
                       marginal='box', opacity=0.7, 
                       color_discrete_map={'Yes': '#EF4444', 'No': '#10B981'})
    fig.update_layout(**theme_config, barmode='overlay', margin=dict(t=10, b=0, l=0, r=0))
    return fig

def plot_tenure_analysis():
    df = get_df()
    fig = px.histogram(df, x='Tenure Months', color='Churn Label', nbins=40,
                       marginal='box', opacity=0.7, 
                       color_discrete_map={'Yes': '#EF4444', 'No': '#10B981'})
    fig.update_layout(**theme_config, barmode='overlay', margin=dict(t=10, b=0, l=0, r=0))
    return fig

def plot_feature_importance():
    df = get_df()
    
    if 'Churn Value' not in df.columns:
        df['Churn Value'] = df['Churn Label'].map({'Yes': 1, 'No': 0})
        
    numeric_df = df.select_dtypes(include=[int, float])
    corr = numeric_df.corr()['Churn Value'].sort_values(ascending=False).drop('Churn Value', errors='ignore')
    
    corr_df = corr.reset_index()
    corr_df.columns = ['Feature', 'Correlation']
    
    fig = px.bar(corr_df.head(10), x='Correlation', y='Feature', orientation='h',
                 color='Correlation', color_continuous_scale='RdBu_r')
    fig.update_layout(**theme_config, yaxis={'categoryorder':'total ascending'}, margin=dict(t=10, b=0, l=0, r=0))
    return fig

def plot_local_shap(shap_df):
    """
    Visualizes local SHAP feature contributions for a single prediction using Plotly.
    Takes the top 10 absolute features.
    """
    top_n = shap_df.head(10).copy()
    # Sort for bottom-up horizontal bar chart
    top_n = top_n.sort_values(by='Contribution', ascending=True)
    
    # Assign colors: Red for pushing towards churn (>0), Green for pushing towards retention (<0)
    top_n['Color'] = top_n['Contribution'].apply(lambda x: '#EF4444' if x > 0 else '#10B981')
    
    fig = go.Figure(go.Bar(
        x=top_n['Contribution'],
        y=top_n['Feature'],
        orientation='h',
        marker_color=top_n['Color']
    ))
    
    fig.update_layout(
        **theme_config,
        title="Key Features Influencing This Prediction (SHAP)",
        xaxis_title="Impact on Prediction (Log-Odds)",
        yaxis_title="",
        margin=dict(t=40, b=0, l=0, r=0),
        xaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor='rgba(255,255,255,0.2)')
    )
    
    return fig
