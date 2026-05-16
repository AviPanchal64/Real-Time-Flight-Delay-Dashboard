import plotly.express as px
import streamlit as st


def render_status_chart(df):
    st.subheader("Flight Status Breakdown")

    if df.empty or "flight_status" not in df.columns:
        st.info("No flight status data available.")
        return

    counts = df["flight_status"].fillna("unknown").value_counts().reset_index()
    counts.columns = ["Status", "Count"]

    fig = px.pie(
        counts,
        names="Status",
        values="Count",
        title="Live Flight Status Distribution"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)


def render_delay_chart(df):
    st.subheader("Top Delayed Flights")

    if df.empty or "departure_delay" not in df.columns:
        st.info("No delay data available.")
        return

    delayed = df.sort_values("departure_delay", ascending=False).head(10)

    fig = px.bar(
        delayed,
        x="flight_number",
        y="departure_delay",
        color="departure_delay",
        title="Top 10 Departure Delays",
        labels={
            "flight_number": "Flight",
            "departure_delay": "Delay (minutes)"
        }
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.4)"
    )

    st.plotly_chart(fig, use_container_width=True)


def render_airline_delay_chart(df):
    st.subheader("Average Delay by Airline")

    if df.empty or "airline" not in df.columns:
        st.info("No airline data available.")
        return

    airline_delay = (
        df.groupby("airline", dropna=True)["departure_delay"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        airline_delay,
        x="airline",
        y="departure_delay",
        title="Average Departure Delay by Airline",
        labels={
            "airline": "Airline",
            "departure_delay": "Average Delay (minutes)"
        }
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,23,42,0.4)"
    )

    st.plotly_chart(fig, use_container_width=True)