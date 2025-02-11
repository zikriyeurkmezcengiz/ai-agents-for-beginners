import datetime
import time
import os
import json
import requests
from typing import Any, Callable, Set, Dict, List, Optional

def fetch_current_datetime(format: Optional[str] = None) -> str:
    """
    Get the current time as a formatted string.

    :param format: The format in which to return the current time. Defaults to None, which uses a standard format.
    :return: The current time as a formatted string.
    """
    current_time = datetime.datetime.now()
    time_format = format if format else "%Y-%m-%d %H:%M:%S"
    return current_time.strftime(time_format)


def convert_to_unix(date_str: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> int:
    """
    Convert a date string to a Unix timestamp.

    :param date_str: The date string.
    :param date_format: The format of the date string. Defaults to "%Y-%m-%d %H:%M:%S".
    :return: The Unix timestamp.
    """
    dt = datetime.datetime.strptime(date_str, date_format)
    return str(int(time.mktime(dt.timetuple())))


def get_airport_code_by_city(city_name: str) -> Optional[str]:
    """
    Search for the airport code by city name in the airports data.
    :param city_name: The name of the city to search for.
    :return: The airport code if found, otherwise None.
    """
    dirname = os.path.dirname(__file__)
    json_path = os.path.join(dirname, "airports.json")
    with open(json_path, 'r') as f:
        data = json.load(f)
    for airport in data:
        if airport.get("city", "").lower() == city_name.lower():
            return airport.get("code")
    return None


# Example usage:
if __name__ == "__main__":
    city = "Syracuse"
    code = get_airport_code_by_city(city)
    print(f"Airport code for {city} is: {code}")



def get_airport_traffic(city_name: str, date_str1: str, date_str2: str,
                        airports_data: Optional[List[Dict[str, str]]] = None) -> Any:
    """
    Lookup flight data for a given city and time period.
    :param city_name: The name of the city.
    :param date_str1: The start date string.
    :param date_str2: The end date string.
    :param airports_data: Optional JSON object representing airport data.
                          If None, it will be loaded from the local 'airports.json' file.
    :return: The flight data from the OpenSky Network API.
    """
    # If not provided, load airport data from file.
    if airports_data is None:
        dirname = os.path.dirname(__file__)
        json_path = os.path.join(dirname, "airports.json")
        with open(json_path, 'r') as f:
            airports_data = json.load(f)

    airport_code = get_airport_code_by_city(city_name)
    if not airport_code:
        return {"error": "Invalid city name"}

    unix_time1 = convert_to_unix(date_str1)
    unix_time2 = convert_to_unix(date_str2)

    # current_unix_time = int(time.time())
    # seven_days_ago_unix_time = current_unix_time - 7 * 24 * 60 * 60

    # if unix_time1 >= current_unix_time or unix_time2 >= current_unix_time:
    #     return {"error": "Dates must be in the past"}

    # if unix_time1 < seven_days_ago_unix_time or unix_time2 < seven_days_ago_unix_time:
    #     return {"error": "Dates must be within the last 7 days"}

    url = f"https://opensky-network.org/api/flights/arrival?airport={airport_code}&begin={unix_time1}&end={unix_time2}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch data from OpenSky Network"}

    # The API returns a list of flight objects. Each object should include a "callsign" field.
    return response.text


# Load airport data from JSON file
file_path = os.path.join(os.path.dirname(__file__), 'airports.json')
with open(file_path, 'r') as file:
    airports_data = json.load(file)

# Example usage
city_name = "Norresundby"
date_str1 = "2023-10-01 12:00:00"
date_str2 = "2023-10-02 12:00:00"
callsigns = get_airport_traffic(city_name, date_str1, date_str2, airports_data)


def fetch_flights(callsign: str):
    """
    Get details of a flight by its callsign.

    :param callsign: The callsign of the flight.
    :return: A dictionary with airline name, origin airport name, and destination airport name.
    """
    url = f"https://api.adsbdb.com/v0/callsign/{callsign}"
    response = requests.get(url)

    if response.status_code != 200:
        return json.dumps({"error": "Failed to fetch data from ADSBDB"})

    data = response.json()
    flight_route = data.get("response", {}).get("flightroute", {})

    airline_name = flight_route.get("airline", {}).get("name")
    origin_airport_name = flight_route.get("origin", {}).get("name")
    destination_airport_name = flight_route.get("destination", {}).get("name")

    return json.dumps({
        "airline_name": airline_name,
        "origin_airport_name": origin_airport_name,
        "destination_airport_name": destination_airport_name
    })


# if isinstance(callsigns, dict) and "error" in callsigns:
#     print(callsigns["error"])
# else:
#     for callsign in callsigns:
#         print(f"Callsign: {callsign}")
#         flight_details = fetch_flights(callsign)
#         print(flight_details)


user_functions: Set[Callable[..., Any]] = {
    fetch_current_datetime,
    convert_to_unix,
    get_airport_code_by_city,
    get_airport_traffic,
    fetch_flights
}