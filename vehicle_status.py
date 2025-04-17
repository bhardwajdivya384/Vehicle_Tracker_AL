import streamlit as st
import requests
import pandas as pd
import json
from datetime import datetime

# Configuration
st.set_page_config(
    page_title="Vehicle Tracking Dashboard",
    page_icon="🚚",
    layout="wide"
)

# Sheet2API credentials and configuration
SHEET2API_ENDPOINT = "https://sheet2api.com/v1/gCKi83JGQMST/vehicle_status"  # Replace with your actual endpoint
# API_KEY = "YOUR_API_KEY"  # Replace with your actual API key if needed

def get_all_records():
    """Fetch all records from the spreadsheet"""
    try:
        response = requests.get(SHEET2API_ENDPOINT)
        if response.status_code == 200: # success
            return response.json()
        else:
            st.error(f"Error fetching data: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error connecting to sheet2api: {e}")
        return []

def main():
    data_json = get_all_records()
    data = pd.DataFrame(data_json)
    st.title("Vehicle Tracker")
    vehicle_number = st.text_input("Vehicle Number")
    result = data[data["Vehicle Number"]==vehicle_number]
    result = result.reset_index(drop=True)

    if vehicle_number:

        if not result.empty:
            result = result.T
            result.columns=['']
            st.subheader("Vehicle Status")
            st.dataframe(result)  # Transposed display
        else:
            st.warning("No matching vehicle found.")

    

main()
