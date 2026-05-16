import pandas as pd


def flatten_flight_data(flights):
    rows = []

    for item in flights:
        departure = item.get("departure") or {}
        arrival = item.get("arrival") or {}
        airline = item.get("airline") or {}
        flight = item.get("flight") or {}
        aircraft = item.get("aircraft") or {}

        rows.append({
            "airline": airline.get("name"),
            "flight_number": flight.get("iata"),
            "flight_status": item.get("flight_status"),
            "departure_airport": departure.get("airport"),
            "departure_iata": departure.get("iata"),
            "departure_scheduled": departure.get("scheduled"),
            "departure_actual": departure.get("actual"),
            "departure_delay": departure.get("delay"),
            "arrival_airport": arrival.get("airport"),
            "arrival_iata": arrival.get("iata"),
            "arrival_scheduled": arrival.get("scheduled"),
            "arrival_actual": arrival.get("actual"),
            "arrival_delay": arrival.get("delay"),
            "aircraft_registration": aircraft.get("registration"),
        })

    df = pd.DataFrame(rows)

    if df.empty:
        return df

    delay_cols = ["departure_delay", "arrival_delay"]

    for col in delay_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    return df