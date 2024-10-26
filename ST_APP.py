#connect sql
import psycopg2
import pandas as pd
import numpy as np

#psycopg2: Used to connect and interact with a PostgreSQL database.
#pandas: For data manipulation and analysis.
#numpy: For numerical operations, including handling missing values (`NaN`).

# Load the existing CSV into DataFrames
df1 = pd.read_csv("Rajasthan.csv")
df2 = pd.read_csv("Telungana.csv")
df3 = pd.read_csv("Kadamba.csv")
df4 = pd.read_csv("West_Bengal.csv")  
df5 = pd.read_csv("Uttar_Pradesh.csv")

df6=pd.read_csv('Chandigarh.csv')
df6['State_Name']='Chandigarh'
df6.to_csv('Chandigarh.csv',index=False)

df7 = pd.read_csv("Bihar.csv")

df8 = pd.read_csv("Andra.csv")
df8['State_Name']='Andra pradesh'
df8.to_csv('Andra.csv',index=False)

df9 = pd.read_csv("Assam.csv")
df9['State_Name']='Assam'
df9.to_csv('Assam.csv',index=False)

df10 = pd.read_csv("Kerala.csv")
df11 = pd.read_csv("Haryana.csv")

# Concatenate all DataFrames
df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], ignore_index=True)

# Clean up the Price column
df["Price"] = df["Price"].str.replace("INR", "")# Remove "INR" from Price column
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")# Convert Price to numeric
df["Price"].fillna(0, inplace=False)  #  Fill missing Price values with 0

# Clean up the Star Rating column (if necessary)
df["Star_Rating"] = pd.to_numeric(df["Star_Rating"], errors="coerce")# to numeric
df["Star_Rating"].fillna(0, inplace=False)  #  Fill missing Price values with 0

# Replacing NaN values with None (for PostgreSQL compatibility)
df = df.replace({np.nan: None})

# Save the cleaned DataFrame to CSV
df.to_csv("Busdetails.csv", index=False)

# Database setup for PostgreSQL
def conn_dbsetup():
    conn = psycopg2.connect(
        host="localhost",
        database="projectdb",
        user="postgres",
        password="qwertyuiop"
    )
    cursor = conn.cursor()

    # Create table for bus details if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS red_bus (
            id SERIAL PRIMARY KEY,
            state TEXT,
            route_name TEXT,
            route_link TEXT,
            bus_name TEXT,
            bus_type TEXT,
            departing_time VARCHAR(100),
            duration TEXT,
            reaching_time VARCHAR(100),
            star_rating FLOAT,
            price FLOAT,
            seat_availability INT
        )
    ''')

    conn.commit()
    return conn, cursor

# Insert DataFrame data into the PostgreSQL database
def insertingtodb(conn, cursor, df):
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO red_bus
            (state,route_name, route_link, bus_name, bus_type, departing_time, duration, reaching_time, star_rating, price, seat_availability)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (
            row['State_Name'],
            row['Route_Name'],
            row['Route_Link'],
            row['Bus_Name'],
            row['Bus_Type'],
            row['Departure'],
            row['Duration'],
            row['Arrival'],
            row['Star_Rating'],  
            row['Price'], 
            int(row['Seat_Availability']) if str(row['Seat_Availability']).isdigit() else 0
        ))#`Seat_Availability` is converted to an integer or `0` if it's not a valid number.

    conn.commit()

# Example of calling the functions
def sqlcsv():
    # Set up the PostgreSQL database
    conn, cursor =conn_dbsetup()

    # Insert the data from DataFrame into the PostgreSQL database
    insertingtodb(conn, cursor, df)

    # Close the connection
    cursor.close()
    conn.close()

# Run the function to load data into PostgreSQL
sqlcsv()
