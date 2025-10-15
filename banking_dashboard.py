import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Set page config
st.set_page_config(
    page_title="Banking Analytics Dashboard",
    page_icon="🏦",
    layout="wide"
)

# Create multi-page app
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Explorer"])

# Load data
@st.cache_data
def load_data():
    df = pd.read_excel('Banking.csv.xlsx')
    # Convert datetime column
    df['Joined Bank'] = pd.to_datetime(df['Joined Bank'])
    # Extract year for analysis
    df['Join_Year'] = df['Joined Bank'].dt.year
    return df

# Load the data
df = load_data()

if page == "Home":
    # Dashboard title
    st.title("🏦 Banking Analytics Dashboard")
    st.markdown("---")
    
    # Key metrics
    st.header("Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Customers", f"{len(df):,}")
        
    with col2:
        avg_age = df['Age'].mean()
        st.metric("Average Age", f"{avg_age:.1f} years")
        
    with col3:
        avg_income = df['Estimated Income'].mean()
        st.metric("Average Income", f"${avg_income:,.0f}")
        
    with col4:
        avg_credit_balance = df['Credit Card Balance'].mean()
        st.metric("Avg. Credit Card Balance", f"${avg_credit_balance:,.0f}")
    
    st.markdown("---")
    
    # Customer Demographics Section
    st.header("Customer Demographics")
    
    # Age distribution
    fig_age = px.histogram(
        df, 
        x="Age", 
        nbins=30, 
        title="Age Distribution of Customers",
        color_discrete_sequence=['#636EFA']
    )
    fig_age.update_layout(bargap=0.1)
    
    # Nationality distribution
    nationality_counts = df['Nationality'].value_counts()
    fig_nationality = px.pie(
        values=nationality_counts.values, 
        names=nationality_counts.index, 
        title="Customer Nationality Distribution"
    )
    
    # Create columns for charts
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_age, use_container_width=True)
        
    with col2:
        st.plotly_chart(fig_nationality, use_container_width=True)
    
    # Occupation distribution
    occupation_counts = df['Occupation'].value_counts().head(10)
    fig_occupation = px.bar(
        x=occupation_counts.index,
        y=occupation_counts.values,
        title="Top 10 Occupations",
        labels={'y': 'Number of Customers', 'x': 'Occupation'},
        color_discrete_sequence=['#EF553B']
    )
    st.plotly_chart(fig_occupation, use_container_width=True)
    
    st.markdown("---")
    
    # Financial Insights Section
    st.header("Financial Insights")
    
    # Create subplots for financial metrics
    fig_financial = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            'Income Distribution', 
            'Credit Card Balance Distribution',
            'Bank Deposits vs Income',
            'Loan Distribution'
        )
    )
    
    # Income distribution
    fig_financial.add_trace(
        go.Histogram(x=df['Estimated Income'], name="Income", showlegend=False),
        row=1, col=1
    )
    
    # Credit card balance distribution
    fig_financial.add_trace(
        go.Histogram(x=df['Credit Card Balance'], name="Credit Card Balance", showlegend=False),
        row=1, col=2
    )
    
    # Bank deposits vs income scatter
    fig_financial.add_trace(
        go.Scatter(
            x=df['Estimated Income'], 
            y=df['Bank Deposits'],
            mode='markers',
            marker=dict(color='#00CC96', size=5),
            showlegend=False,
            hovertemplate='<b>Income:</b> $%{x:,.0f}<br><b>Deposits:</b> $%{y:,.0f}<extra></extra>'
        ),
        row=2, col=1
    )
    
    # Loan distribution
    fig_financial.add_trace(
        go.Histogram(x=df['Bank Loans'], name="Loans", showlegend=False),
        row=2, col=2
    )
    
    fig_financial.update_layout(height=700, title_text="Financial Metrics Analysis")
    st.plotly_chart(fig_financial, use_container_width=True)
    
    st.markdown("---")
    
    # Loyalty and Risk Analysis
    st.header("Loyalty & Risk Analysis")
    
    # Loyalty classification distribution
    loyalty_counts = df['Loyalty Classification'].value_counts()
    fig_loyalty = px.bar(
        x=loyalty_counts.index,
        y=loyalty_counts.values,
        title="Loyalty Classification Distribution",
        labels={'x': 'Loyalty Level', 'y': 'Number of Customers'},
        color=loyalty_counts.index,
        color_discrete_sequence=px.colors.sequential.Viridis
    )
    st.plotly_chart(fig_loyalty, use_container_width=True)
    
    # Risk weighting analysis
    fig_risk = px.box(
        df, 
        x="Loyalty Classification", 
        y="Risk Weighting",
        title="Risk Weighting by Loyalty Classification",
        color="Loyalty Classification",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig_risk, use_container_width=True)
    
    st.markdown("---")
    
    # Banking Products Analysis
    st.header("Banking Products Analysis")
    
    # Create subplots for banking products
    fig_products = make_subplots(
        rows=2, cols=3,
        subplot_titles=(
            'Credit Cards', 
            'Checking Accounts',
            'Saving Accounts',
            'Foreign Currency Accounts',
            'Business Lending',
            'Properties Owned'
        )
    )
    
    # Credit cards
    fig_products.add_trace(
        go.Histogram(x=df['Amount of Credit Cards'], name="Credit Cards", showlegend=False),
        row=1, col=1
    )
    
    # Checking accounts
    fig_products.add_trace(
        go.Histogram(x=df['Checking Accounts'], name="Checking Accounts", showlegend=False),
        row=1, col=2
    )
    
    # Saving accounts
    fig_products.add_trace(
        go.Histogram(x=df['Saving Accounts'], name="Saving Accounts", showlegend=False),
        row=1, col=3
    )
    
    # Foreign currency accounts
    fig_products.add_trace(
        go.Histogram(x=df['Foreign Currency Account'], name="Foreign Currency", showlegend=False),
        row=2, col=1
    )
    
    # Business lending
    fig_products.add_trace(
        go.Histogram(x=df['Business Lending'], name="Business Lending", showlegend=False),
        row=2, col=2
    )
    
    # Properties owned
    fig_products.add_trace(
        go.Histogram(x=df['Properties Owned'], name="Properties", showlegend=False),
        row=2, col=3
    )
    
    fig_products.update_layout(height=700, title_text="Banking Products Usage")
    st.plotly_chart(fig_products, use_container_width=True)
    
    st.markdown("---")
    
    # Time Series Analysis
    st.header("Time Series Analysis")
    
    # Customers joined over time
    join_counts = df['Join_Year'].value_counts().sort_index()
    fig_join = px.line(
        x=list(join_counts.index),
        y=list(join_counts.values),
        title="Customer Acquisition Over Time",
        markers=True
    )
    fig_join.update_layout(
        xaxis_title="Year",
        yaxis_title="Number of Customers"
    )
    st.plotly_chart(fig_join, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("🏦 Banking Analytics Dashboard | Data Insights for Better Decision Making")

elif page == "Data Explorer":
    # Dashboard title
    st.title("🔍 Data Explorer")
    st.markdown("---")
    
    # Sidebar filters
    st.sidebar.header("Filters")
    selected_occupations = st.sidebar.multiselect(
        "Select Occupation(s):",
        options=df['Occupation'].unique(),
        default=df['Occupation'].unique()[:3]
    )
    
    selected_nationalities = st.sidebar.multiselect(
        "Select Nationality:",
        options=df['Nationality'].unique(),
        default=df['Nationality'].unique()
    )
    
    selected_loyalty = st.sidebar.multiselect(
        "Select Loyalty Classification:",
        options=df['Loyalty Classification'].unique(),
        default=df['Loyalty Classification'].unique()
    )
    
    # Apply filters
    filtered_df = df[
        (df['Occupation'].isin(selected_occupations)) &
        (df['Nationality'].isin(selected_nationalities)) &
        (df['Loyalty Classification'].isin(selected_loyalty))
    ]
    
    # Key metrics for filtered data
    st.header("Key Metrics (Filtered Data)")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Customers", f"{len(filtered_df):,}")
        
    with col2:
        avg_age = filtered_df['Age'].mean()
        st.metric("Average Age", f"{avg_age:.1f} years")
        
    with col3:
        avg_income = filtered_df['Estimated Income'].mean()
        st.metric("Average Income", f"${avg_income:,.0f}")
        
    with col4:
        avg_credit_balance = filtered_df['Credit Card Balance'].mean()
        st.metric("Avg. Credit Card Balance", f"${avg_credit_balance:,.0f}")
    
    st.markdown("---")
    
    # Show filtered data
    st.header("Filtered Data")
    st.dataframe(filtered_df)
    
    # Download button for filtered data
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_banking_data.csv",
        mime="text/csv"
    )
    
    st.markdown("---")
    
    # Filtered visualizations
    st.header("Filtered Data Visualizations")
    
    # Age distribution for filtered data
    fig_age_filtered = px.histogram(
        filtered_df, 
        x="Age", 
        nbins=30, 
        title="Age Distribution (Filtered Data)",
        color_discrete_sequence=['#636EFA']
    )
    fig_age_filtered.update_layout(bargap=0.1)
    st.plotly_chart(fig_age_filtered, use_container_width=True)
    
    # Nationality distribution for filtered data
    # Use groupby and count instead of value_counts to avoid type issues
    nationality_counts_filtered = filtered_df.groupby('Nationality').size()
    values_list = list(nationality_counts_filtered)
    names_list = list(nationality_counts_filtered.index)
    fig_nationality_filtered = px.pie(
        values=values_list, 
        names=names_list, 
        title="Customer Nationality Distribution (Filtered Data)"
    )
    st.plotly_chart(fig_nationality_filtered, use_container_width=True)