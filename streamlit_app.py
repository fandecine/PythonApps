import time
import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim

# Set page layout to wide
st.set_page_config(layout="wide")

# Title and Description
st.title('Streamlit Map with Country Highlight and Population Data')
st.write(
    'This app demonstrates how to load a CSV file containing country names and population data, geocode the countries, and display them on a map.')

# File Uploader
uploaded_file = st.file_uploader("Upload a CSV file with country names and population data", type=["csv"])
if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Show the uploaded data for debugging
    st.write("Uploaded Data:")
    st.write(df.head())  # Show only the first few rows for preview

    # Geocoding the Countries
    geolocator = Nominatim(user_agent="streamlit_geocoder", timeout=10)  # Increased timeout to 10 seconds


    # Function to get latitude and longitude from country name
    def geocode_country(country_name):
        try:
            # Geocode with a delay to avoid rate-limiting errors
            time.sleep(1)  # Adding a 1-second delay between requests
            location = geolocator.geocode(country_name)
            if location:
                return location.latitude, location.longitude
            else:
                st.write(f"Geocoding failed for {country_name}: No location found.")
                return None, None
        except Exception as e:
            st.write(f"Error geocoding {country_name}: {e}")
            return None, None


    # Get distinct countries from the 'Entity' column
    distinct_countries = df['Entity'].unique()

    # Create a dictionary to store the latitude and longitude of each country
    country_coords = {}

    # Geocode only the distinct countries
    for country in distinct_countries:
        if country not in country_coords:  # Check if the country has already been geocoded
            lat, lon = geocode_country(country)
            if lat and lon:
                country_coords[country] = (lat, lon)
            else:
                st.write(f"Skipping geocoding for {country} as no coordinates were found.")

    # Debugging output: Show the country_coords dictionary
    st.write("Geocoding results (latitude, longitude):")
    st.write(country_coords)

    # Map the latitude and longitude back to the original dataset
    df['latitude'], df['longitude'] = zip(*df['Entity'].map(country_coords).fillna((None, None)))

    # Debugging: Show Data with Latitude and Longitude
    st.write("Data with Latitude and Longitude:")
    st.write(df[['Entity', 'latitude', 'longitude']])

    # Filter out rows with missing latitudes/longitudes (in case geocoding fails)
    df = df.dropna(subset=['latitude', 'longitude'])

    # Debugging: Check how many valid rows are left after filtering
    st.write(f"Number of valid rows after filtering: {len(df)}")

    # If there are valid rows, display the map
    if len(df) > 0:
        # --- 3. Display Map ---
        st.subheader('Map of Countries with Population Data')
        st.map(df[['latitude', 'longitude']])  # Plotting the coordinates on the map
    else:
        st.write("No valid country names found or no coordinates found for the countries.")

    # Show population data for specific year (optional)
    st.subheader("Population Data for Year 1950 (Example)")
    df_1950 = df[df['Year'] == 1950]
    st.write(df_1950[['Entity', 'Population - Sex: all - Age: all - Variant: estimates']])

# Additional Information
st.write("""
This app uses the Geopy library to convert country names into latitude and longitude coordinates, 
which are then used to highlight those countries on a map.
""")
