
import sqlite3
import pandas as pd
from config import DATABASE_NAME

def connect():
    return sqlite3.connect(DATABASE_NAME)


def create_table():

    conn = connect()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT NOT NULL,

        description TEXT,

        priority TEXT NOT NULL,

        due_date TEXT NOT NULL,

        status TEXT DEFAULT 'Pending'

    )
    """)

    conn.commit()

    conn.close()

    
def execute_query(query, values=()):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(query, values)

    conn.commit()

    conn.close()


def fetch_query(query, values=()):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(query, values)

    rows = cursor.fetchall()

    conn.close()

    return rows  

def fetch_dataframe(query, values=()):

    import pandas as pd

    conn = connect()

    df = pd.read_sql_query(
        query,
        conn,
        params=values
    )

    conn.close()

    return df
  
def fetch_one(query, values=()):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(query, values)

    row = cursor.fetchone()

    conn.close()

    return row

def fetch_value(query, values=()):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(query, values)

    value = cursor.fetchone()[0]

    conn.close()

    return value