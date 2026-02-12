import sqlite3
from datetime import datetime

# Connect to your existing finance database
conn = sqlite3.connect('database/finance.db')
c = conn.cursor()

# Sample data to insert
samples = [
    ('2026-02-01', 'Salary', 'Monthly Stipend', 15000.0, 'Income'),
    ('2026-02-02', 'Rent', 'Room Rent', 5000.0, 'Expense'),
    ('2026-02-05', 'Food', 'Weekend Dinner', 1200.0, 'Expense'),
    ('2026-02-07', 'Tech', 'Keyboard Upgrade', 2500.0, 'Expense'),
    ('2026-02-10', 'Freelance', 'Bug Fix Project', 3000.0, 'Income'),
    ('2026-02-11', 'Transport', 'Fuel', 400.0, 'Expense')
]

# Insert into the database
c.executemany("INSERT INTO transactions (date, category, description, amount, type) VALUES (?, ?, ?, ?, ?)", samples)

conn.commit()
conn.close()
print("✅ Sample data added successfully! Refresh your Streamlit app.")