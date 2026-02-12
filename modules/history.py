import streamlit as st
from database.db_manager import get_all_data

def render_history():
    st.title("📜 Transaction History")
    df = get_all_data()

    if df.empty:
        st.info("No records yet.")
        return

    st.dataframe(df.sort_values(by="date", ascending=False), use_container_width=True, hide_index=True)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Export to CSV", data=csv, file_name='finance_history.csv', mime='text/csv')