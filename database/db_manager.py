import sqlite3
import pandas as pd
from datetime import datetime

DB_PATH = 'database/finance.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    date TEXT, 
                    category TEXT, 
                    description TEXT, 
                    amount REAL,
                    type TEXT
                )''')
    conn.commit()
    conn.close()

def add_transaction(category, description, amount, t_type):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    c.execute("INSERT INTO transactions (date, category, description, amount, type) VALUES (?, ?, ?, ?, ?)", 
              (date, category, description, amount, t_type))
    conn.commit()
    conn.close()

def get_all_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    return df