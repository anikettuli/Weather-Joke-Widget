# Joke and Weather App

This Python application fetches and displays a random joke using the JokeAPI and provides the weather forecast based on your current location using the AccuWeather API.

## Prerequisites

- Python 3.x
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/anikettuli/Weather-Joke-Widget.git
   cd Weather-Joke-Widget
   ```

2. Install the required dependencies:

   The app self installs any additional modules on its first run. 

## Usage

### Joke Module

Run the `joke.py` script to get a random joke:

```bash
python joke.py
```

### Weather Module

1. Obtain an AccuWeather API key from [AccuWeather Developer Portal](https://developer.accuweather.com/).

2. Replace `api_key` in the `weather.py` script with your AccuWeather API key.

3. Run the `weather.py` script to get the hourly temperature forecast for your location:

   ```bash
   python weather.py
   ```

## How it Works

- `joke.py` uses the JokeAPI to fetch and display a random joke.
- `weather.py` retrieves your current IP address and uses it to determine your location. It then fetches the weather forecast using the AccuWeather API for that location.

## License
I will license this soon.
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
