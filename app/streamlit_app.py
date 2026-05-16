import sys
from pathlib import Path

import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from api.flight_api import fetch_flights
from components.charts import (
    render_airline_delay_chart,
    render_delay_chart,
    render_status_chart,
)
from components.layout import apply_css, render_footer, render_header
from src.data_processing import flatten_flight_data


st.set_page_config(
    page_title="Flight Delay Analytics Dashboard",
    page_icon="✈️",
    layout="wide"
)

apply_css()
render_header()

# Refresh every 60 seconds
st_autorefresh(interval=60 * 1000, key="flight_refresh")

st.sidebar.title("Flight Search Controls")
st.sidebar.write("Data refreshes automatically every 60 seconds.")

dep_iata = st.sidebar.text_input("Departure airport IATA code", value="LHR")
arr_iata = st.sidebar.text_input("Arrival airport IATA code", value="")
flight_status = st.sidebar.selectbox(
    "Flight status",
    ["All", "scheduled", "active", "landed", "cancelled", "incident", "diverted"]
)
limit = st.sidebar.slider("Number of flights", 10, 100, 50)

try:
    flights = fetch_flights(
        dep_iata=dep_iata,
        arr_iata=arr_iata,
        flight_status=flight_status,
        limit=limit
    )

    df = flatten_flight_data(flights)

except Exception as e:
    st.error("Could not fetch live flight data. Check your API key or request limit.")
    st.write(e)
    st.stop()


if df.empty:
    st.warning("No flight data found for the selected filters.")
    st.stop()


total_flights = len(df)
delayed_flights = int((df["departure_delay"] > 0).sum())
avg_delay = df["departure_delay"].mean()
max_delay = df["departure_delay"].max()

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Flights Tracked", f"{total_flights}")

with m2:
    st.metric("Delayed Flights", f"{delayed_flights}")

with m3:
    st.metric("Average Delay", f"{avg_delay:.1f} min")

with m4:
    st.metric("Max Delay", f"{max_delay:.0f} min")


if avg_delay >= 30:
    st.error("High average delay detected for the selected airport/filter.")
elif avg_delay >= 10:
    st.warning("Moderate delay conditions detected.")
else:
    st.success("Low delay conditions currently detected.")


st.subheader("Live Flight Board")

display_cols = [
    "flight_number",
    "airline",
    "flight_status",
    "departure_iata",
    "arrival_iata",
    "departure_scheduled",
    "departure_actual",
    "departure_delay",
    "arrival_delay",
]

available_cols = [col for col in display_cols if col in df.columns]
st.dataframe(df[available_cols], use_container_width=True)


left, right = st.columns(2)

with left:
    render_status_chart(df)
    render_delay_chart(df)

with right:
    render_airline_delay_chart(df)


with st.expander("View Raw Processed Flight Data"):
    st.dataframe(df, use_container_width=True)

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download flight data as CSV",
    data=csv,
    file_name="flight_delay_data.csv",
    mime="text/csv"
)

render_footer()