
import requests

# Define the API endpoint
API_ENDPOINT = "https://samples.openweathermap.org/data/2.5/forecast/hourly"


# Function to get temperature for a given date and time
def get_temperature(date_time):
    params = {"q": "London,us", "appid": "b6907d289e10d714a6e88b30761fae22"}
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()

    # Find the relevant temperature data based on the date_time provided
    for forecast in data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['main']['temp']

    return None


# Function to get wind speed for a given date and time
def get_wind_speed(date_time):
    params = {"q": "London,us", "appid": "b6907d289e10d714a6e88b30761fae22"}
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()

    # Find the relevant wind speed data based on the date_time provided
    for forecast in data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['wind']['speed']

    return None


# Function to get pressure for a given date and time
def get_pressure(date_time):
    params = {"q": "London,us", "appid": "b6907d289e10d714a6e88b30761fae22"}
    response = requests.get(API_ENDPOINT, params=params)
    data = response.json()

    # Find the relevant pressure data based on the date_time provided
    for forecast in data['list']:
        if forecast['dt_txt'] == date_time:
            return forecast['main']['pressure']

    return None


# Main program loop
while True:
    print("Options:")
    print("1. Get Temperature")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date_time = input("Enter date with time (e.g., yyyy/mm/dd , 2023-09-26 14:30:00): ")
        temperature = get_temperature(date_time)
        if temperature is not None:
            print(f"Temperature at {date_time}: {temperature}°C")
        else:
            print("Temperature data not found for the provided date and time.")

    elif choice == "2":
        date_time = input("Enter date with time (e.g., 2019-03-27 18:00:00): As the api report is of 2019 , pls enter the date from the yeaR 2019 ")
        wind_speed = get_wind_speed(date_time)
        if wind_speed is not None:
            print(f"Wind Speed at {date_time}: {wind_speed} m/s")
        else:
            print("Wind speed data not found for the provided date and time.")

    elif choice == "3":
        date_time = input("Enter date with time (e.g., 2023-09-26 14:30:00): ")
        pressure = get_pressure(date_time)
        if pressure is not None:
            print(f"Pressure at {date_time}: {pressure} hPa")
        else:
            print("Pressure data not found for the provided date and time.")

    elif choice == "0":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")


