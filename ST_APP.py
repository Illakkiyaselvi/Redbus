import streamlit as st
import pandas as pd
import psycopg2

# Function to fetch bus details from PostgreSQL
def fetch_bus_details():
    conn = psycopg2.connect(
        host="localhost",
        database="projectdb",
        user="postgres",
        password="qwertyuiop"
    )
    query = "SELECT * FROM bus_routes1"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Main Streamlit application
def main():
    st.title("Bus Routes from RedBus")
    st.image("logo.png",width=200)

    st.markdown("<h1 style='text-align: center;'>State Road Transport Corporation (SRTC) of India</h1>", unsafe_allow_html=True)

    # Fetching bus details
    df = fetch_bus_details()

    # Display the data
    st.subheader("Available Bus Routes")
    st.write("Here are the available bus routes:")
    
    # Filters
    st.sidebar.header("Filters")
    route_names = df['route_name'].unique().tolist()
    selected_route = st.sidebar.selectbox("Select Bus Route", route_names)
    min_price = st.sidebar.slider("Minimum Price", 00.0, float(df['price'].max()), 00.0)
    max_price = st.sidebar.number_input("Maximum Price", 0.0, float(df['price'].max()), float(df['price'].max()))
    min_rating = st.sidebar.slider("Minimum Star Rating", 0.0, 5.0, 0.0)
    bus_types = df['bus_type'].unique().tolist()
    selected_bus_type = st.sidebar.multiselect("Bus Type", bus_types, default=bus_types)

    # Applying filters
    filtered_df = df[
        (df['route_name'] == selected_route) &
        (df['price'] >= min_price) &
        (df['price'] <= max_price) &
        (df['star_rating'] >= min_rating) &
        (df['bus_type'].isin(selected_bus_type))
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
