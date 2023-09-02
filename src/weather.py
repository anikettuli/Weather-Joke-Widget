import requests


def get_ip():
    response = requests.get("https://api64.ipify.org?format=json").json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f"https://ipapi.co/{ip_address}/json/").json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
    }
    return location_data


location_data = get_location()

api_key = "BTr1dNstfwkjBSYXdIKDnmGPXRs2zh5y"


def get_forecast():
    location_data = get_location()
    response = requests.get(
        f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={location_data["city"]},{location_data["region"]},{location_data["country"]}&details=true'
    ).json()
    location_key = response[0]["Key"]
    response = requests.get(
        f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}?apikey={api_key}&details=true&metric=true"
    ).json()
    forecast_data = []
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


forecast = get_forecast()
for i in range(len(forecast)):
    print(
        "Time: ",
        forecast[i]["time"],
        "Temperature: ",
        forecast[i]["temp"],
        "Rain: ",
        forecast[i]["rain"],
    )
