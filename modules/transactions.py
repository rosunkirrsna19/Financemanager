import streamlit as st
from database.db_manager import add_transaction

def render_transactions():
    st.title("➕ Add Transaction")
    
    with st.form("finance_form", clear_on_submit=True):
        t_type = st.radio("Type", ["Expense", "Income"], horizontal=True)
        amount = st.number_input("Amount (₹)", min_value=0.0, step=50.0)
        
        if t_type == "Expense":
            cat_options = ["Food", "Transport", "Rent", "Shopping", "Tech", "Other"]
        else:
            cat_options = ["Salary", "Freelance", "Gift", "Other"]
            
        category = st.selectbox("Category", cat_options)
        description = st.text_input("Description (Optional)")
        
        submit = st.form_submit_button("Save Transaction")
        
    if submit:
        if amount > 0:
            add_transaction(category, description, amount, t_type)
            st.success(f"Recorded {t_type} of ₹{amount}")
            st.balloons()
        else:
            st.error("Please enter a valid amount.")