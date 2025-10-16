# Banking Analytics Dashboard

This repository contains two powerful analytics solutions for banking data analysis: a Streamlit dashboard and a Power BI dashboard.

## Streamlit Dashboard

The Streamlit dashboard is built with Python and provides interactive visualizations for exploring banking customer data.

### Features:
- Multi-page application with Home and Data Explorer pages
- Interactive filters for occupation, nationality, and loyalty classification
- Real-time data visualization updates
- Export functionality for filtered data
- Responsive design for different screen sizes

### Requirements:
- Python 3.7+
- Streamlit
- Pandas
- Plotly

### How to Run Locally:
```bash
streamlit run banking_dashboard.py
```

### Deployment Instructions:
1. Create a `requirements.txt` file with all dependencies
2. Push the code to GitHub
3. Connect your GitHub repository to Streamlit Cloud
4. Streamlit Cloud will automatically install dependencies from requirements.txt

## Power BI Dashboard

The Power BI dashboard consists of 4 comprehensive pages designed to provide deep insights into customer demographics, financial assets, lending patterns, and predictive analytics.

### Dashboard Structure (4 Pages Total)

---

### PAGE 1 — Customer Demographics & Overview

**Objective**: Understand customer distribution by age, gender, nationality, and loyalty.

| Visualization | Description | Columns Used |
|---------------|-------------|--------------|
| 🧑‍🤝‍🧑 Pie Chart | Gender distribution | GenderId (1 = Male, 2 = Female) |
| 🎂 Histogram / Column Chart | Age distribution | Age |
| 🌍 Stacked Bar Chart | Customers by nationality | Nationality |
| 💎 Donut Chart | Loyalty classification distribution | Loyalty Classification |
| 💰 Card Visuals | Average income, average deposits, total customers | Estimated Income, Bank Deposits |
| 📆 Line Chart | Customer join trend over time | Joined Bank |

**Slicers / Filters**: Nationality, Occupation, Fee Structure

---

### PAGE 2 — Financial Assets & Performance

**Objective**: Visualize customers' financial holdings and relationships across different accounts.

| Visualization | Description | Columns Used |
|---------------|-------------|--------------|
| 📈 Bar Chart | Average deposits, savings, checking by loyalty class | Bank Deposits, Saving Accounts, Checking Accounts, Loyalty Classification |
| 🏦 Clustered Column Chart | Distribution of account types by fee structure | Fee Structure, Saving Accounts, Checking Accounts |
| 💳 Column Chart | Avg. number of credit cards by income range | Estimated Income, Amount of Credit Cards |
| 🪙 Stacked Area Chart | Total balances vs. bank loans | Bank Deposits, Bank Loans |
| 🧾 Gauge Chart | Avg. Credit Card Balance | Credit Card Balance |

**KPI Cards**:
- Total deposits = SUM(Bank Deposits)
- Avg. savings = AVERAGE(Saving Accounts)
- Total business lending = SUM(Business Lending)

---

### PAGE 3 — Loan, Lending & Risk Analysis

**Objective**: Evaluate customer loan behavior, property ownership, and risk weighting.

| Visualization | Description | Columns Used |
|---------------|-------------|--------------|
| 🏘️ Bar Chart | Properties owned by loyalty tier | Properties Owned, Loyalty Classification |
| 🧮 Box Plot | Risk weighting distribution across occupations | Risk Weighting, Occupation |
| 🏦 Line Chart | Business lending vs. savings trend | Business Lending, Saving Accounts |
| 💼 Stacked Column Chart | Average loan vs. income | Bank Loans, Estimated Income |
| ⚠️ Gauge or KPI | Avg. risk score per customer | Risk Weighting |

**Slicers**: Occupation, Fee Structure, Risk Weighting

---

### PAGE 4 — Predictive & Strategic Insights (Bonus for Final-Year)

**Objective**: Show ML-driven or derived metrics for decision-making.

| Visualization | Description | Columns Used |
|---------------|-------------|--------------|
| 📊 Scatter Plot | Income vs. Loan amount (color-coded by risk) | Estimated Income, Bank Loans, Risk Weighting |
| 🧠 Card Visuals | Predicted high-risk customers (if ML model used) | Predicted column from Python model |
| 📈 Line Chart | Yearly customer growth by loyalty class | Joined Bank, Loyalty Classification |
| 🧭 Table / Matrix | Top 10 high-value customers (income + deposits) | Name, Estimated Income, Bank Deposits, Risk Weighting |
| 🧩 Word Cloud (Optional) | Common occupations | Occupation |

---

## Data Source

The dashboard is built using the `Banking.csv.xlsx` file which contains customer information including demographics, financial assets, and banking behaviors.

## Setup Instructions

1. Ensure you have Python installed
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit dashboard:
   ```
   streamlit run banking_dashboard.py
   ```

For Power BI dashboard:
1. Open Power BI Desktop
2. Import the `Banking.csv.xlsx` file
3. Use the data model to create visualizations as described above