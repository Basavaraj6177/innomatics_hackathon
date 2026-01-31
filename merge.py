import pandas as pd
import sqlite3
import os


print("Loading Orders...")
orders = pd.read_csv('orders.csv')


print("Loading Users...")
users = pd.read_json('users.json')


print("Loading Restaurants...")
conn = sqlite3.connect(':memory:')
with open('restaurants.sql', 'r') as f:
    sql_script = f.read()
conn.executescript(sql_script)

restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)


print("Merging datasets...")

merged_data = pd.merge(orders, users, on='user_id', how='left')


final_df = pd.merge(merged_data, restaurants, on='restaurant_id', how='left')
final_df.to_csv('final_food_delivery_dataset.csv', index=False)
print("Success! 'final_food_delivery_dataset.csv' has been created.")