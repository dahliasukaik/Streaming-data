import sqlite3
import pandas as pd

# Create/connect to an SQLite database
conn = sqlite3.connect("streaming.db")
cursor = conn.cursor()

# Create tables (if they don't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS dimUser(
    user_id INTEGER PRIMARY KEY,
    subscription_type TEXT,
    region TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS dimContent(
    content_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    content_type TEXT,
    release_year INTEGER
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS factEngagement(
    user_id INTEGER,
    content_id INTEGER,
    view_date TEXT,
    minutes_watched INTEGER,
    device_type TEXT,
    was_completed INTEGER
)''')

# Load data from CSV into DataFrames
users_df = pd.read_csv("users.csv")
content_df = pd.read_csv("content.csv")
engagement_df = pd.read_csv("engagement.csv")

# Write data to tables
users_df.to_sql('dimUser', conn, if_exists='append', index=False)
content_df.to_sql('dimContent', conn, if_exists='append', index=False)
engagement_df.to_sql('factEngagement', conn, if_exists='append', index=False)

conn.commit()
conn.close()
