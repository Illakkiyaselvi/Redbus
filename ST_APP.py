import streamlit as st
import pandas as pd
import psycopg2
#import re

#from datetime import datetime

# Function to fetch bus details from PostgreSQL
def fetch_bus_details():
    conn = psycopg2.connect(
        host="localhost",
        database="projectdb",
        user="postgres",
        password="qwertyuiop"
    )
    query = "SELECT * FROM red_bus"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def convert_to_time(time_str):
    if pd.isnull(time_str):
        return None
    try:
        time_str = time_str.strip()
        return pd.to_datetime(time_str, format='%H:%M').time()  # Handles "HH:MM" format
    except ValueError:
        return None


# Main Streamlit application
def main():
    st.title("Bus Routes from RedBus")
    st.image("logo.png",width=1000)

    st.markdown("<h1 style='text-align: center;'>State Road Transport Corporation (SRTC) of India</h1>", unsafe_allow_html=True)

    # Fetching bus details
    df = fetch_bus_details()

    df['departing_time'] = df['departing_time'].apply(lambda x: convert_to_time(x))

   

    # Display the data
    st.subheader("Available Bus Routes")
    st.write("Here are the available bus routes:")
    
    # Filters
    st.sidebar.header("Filters")

    if 'state' in df.columns:
        state = df['state'].unique().tolist()
        selected_state = st.sidebar.selectbox("Select State", state)
    else:
        st.warning("State column is missing in the data.")

  

    route_names  = df[df['state'] == selected_state]['route_name'].unique()
    selected_route = st.sidebar.selectbox("Select Route", route_names  )


  

    # Filter 3: Star Rating Filter
    if 'star_rating' in df.columns:
        min_rating = float(df['star_rating'].min())
        max_rating = float(df['star_rating'].max())
        rating_range = st.sidebar.slider("Select Star Rating", min_value=min_rating, max_value=max_rating, step=0.1, value=(min_rating, max_rating))
        df = df[(df['star_rating'] >= rating_range[0]) & (df['star_rating'] <= rating_range[1])]


        min_price = None
        max_price = None
   
    if 'price' in df.columns:
        min_price = float(df['price'].min())
        max_price = float(df['price'].max())
        price_range = st.slider("Select Price Range", min_value=min_price, max_value=max_price, value=(min_price, max_price))
        df = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]

   



    min_departure_time = st.sidebar.time_input("Min Departure Time", value=pd.to_datetime("00:00").time())
    max_departure_time = st.sidebar.time_input("Max Departure Time", value=pd.to_datetime("23:59").time())

    availability_options = ['Available', 'Not Available']
    selected_availability = st.sidebar.selectbox("Seat Availability", availability_options)

    

    # Applying filters
    filtered_df = df[
        (df['state'] == selected_state)&
        (df['route_name'] == selected_route) &
        (df['price'] >= min_price) &
        (df['price'] <= max_price) &
        (df['star_rating'] >= min_rating) &
        (df['departing_time'] >= min_departure_time) &
        (df['departing_time'] <= max_departure_time) &
        ((df['seat_availability'] >= 0) if selected_availability == 'Available' 
             else (df['seat_availability'] == 0))
    ]

    if filtered_df.empty:
        st.write("No results found based on the selected filters.")
    else:
        st.dataframe(filtered_df)

        # Allow downloading the filtered results
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='filtered_bus_details.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
