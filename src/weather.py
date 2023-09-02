import requests


# Function to get the public IP address using the ipify.org API
def get_ip():
    response = requests.get("https://api64.ipify.org?format=json").json()
    return response["ip"]


# Function to get location information based on the public IP address
def get_location():
    ip_address = get_ip()
    response = requests.get(f"https://ipapi.co/{ip_address}/json/").json()

    # Create a dictionary containing location data
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
    }
    return location_data


# Get location information
location_data = get_location()

# AccuWeather API key
api_key = "BTr1dNstfwkjBSYXdIKDnmGPXRs2zh5y"


# Function to get the weather forecast
def get_forecast():
    location_data = get_location()

    # Send a request to AccuWeather API to search for the location key
    response = requests.get(
        f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={location_data["city"]},{location_data["region"]},{location_data["country"]}&details=true'
    ).json()

    # Extract the location key
    location_key = response[0]["Key"]

    # Send a request to AccuWeather API to get hourly weather forecast
    response = requests.get(
        f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}?apikey={api_key}&details=true&metric=true"
    ).json()

    forecast_data = []

    # Extract relevant data from the response and store it in a list
    for forecast in response:
        forecast_data.append(
            {
                "time": forecast["DateTime"],
                "temp": forecast["Temperature"]["Value"],
                "rain": forecast["PrecipitationProbability"],
                "icon": forecast["WeatherIcon"],
            }
        )
    return forecast_data


# Main function
def main():
    forecast = get_forecast()

    # Loop through the forecast data and print it
    for i in range(len(forecast)):
        print(
            "Time: ",
            forecast[i]["time"],
            "Temperature: ",
            forecast[i]["temp"],
            "Rain: ",
            forecast[i]["rain"],
        )


# Entry point of the script
if __name__ == "__main__":
    main()
