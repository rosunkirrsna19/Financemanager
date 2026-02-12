import streamlit as st
import plotly.express as px
from database.db_manager import get_all_data

def render_dashboard():
    st.title("📊 Financial Overview")
    df = get_all_data()

    if df.empty:
        st.warning("No data found. Go to 'Add Transaction' to start!")
        return

    income = df[df['type'] == 'Income']['amount'].sum()
    expense = df[df['type'] == 'Expense']['amount'].sum()
    balance = income - expense

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Income", f"₹{income:,.2f}")
    m2.metric("Total Expense", f"₹{expense:,.2f}", delta=f"-{expense:,.2f}", delta_color="inverse")
    m3.metric("Net Balance", f"₹{balance:,.2f}")

    st.subheader("Expense Breakdown")
    exp_df = df[df['type'] == 'Expense']
    if not exp_df.empty:
        fig = px.pie(exp_df, values='amount', names='category', hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Add some expenses to see the chart!")