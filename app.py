import streamlit as st
import os
from database.db_manager import init_db
from modules.dashboard import render_dashboard
from modules.transactions import render_transactions
from modules.history import render_history

st.set_page_config(page_title="FinanceFlow", page_icon="💰", layout="wide")

def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Important: Load styles and init DB
local_css("assets/styles.css")
init_db()

st.sidebar.title("💰 FinanceFlow")
choice = st.sidebar.selectbox("Menu", ["Dashboard", "Add Transaction", "History"])

if choice == "Dashboard":
    render_dashboard()
elif choice == "Add Transaction":
    render_transactions()
elif choice == "History":
    render_history()