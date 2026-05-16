import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
BASE_URL = "http://api.aviationstack.com/v1/flights"


def fetch_flights(
    dep_iata=None,
    arr_iata=None,
    flight_status=None,
    limit=50
):
    params = {
        "access_key": API_KEY,
        "limit": limit,
    }

    if dep_iata:
        params["dep_iata"] = dep_iata.upper()

    if arr_iata:
        params["arr_iata"] = arr_iata.upper()

    if flight_status and flight_status != "All":
        params["flight_status"] = flight_status.lower()

    response = requests.get(BASE_URL, params=params, timeout=20)
    response.raise_for_status()

    return response.json().get("data", [])