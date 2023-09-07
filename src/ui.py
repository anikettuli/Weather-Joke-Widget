import sys
import asyncio


# Import PyQt6 libraries
try:
    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
    from PyQt6.QtCore import QTimer  # Import QTimer for auto-closing
except ImportError:
    # If PyQt5 is not installed, attempt to install it
    import os

    os.system("pip install PyQt6")

    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
    from PyQt6.QtCore import QTimer  # Import QTimer for auto-closing

# Import functions from external modules
from weather import (
    get_forecast,
    get_location,
)  # Import the get_forecast function from weather.py
from joke import get_joke  # Import the get_joke function from joke.py


# Create a PyQt6 widget for displaying weather and jokes
class WeatherJokeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.update_data()

    def initUI(self):
        self.setWindowTitle("Weather and Joke Widget")
        self.setGeometry(100, 100, 400, 200)

        self.weather_label = QLabel(f"Weather: N/A", self)
        self.joke_label = QLabel("Joke: N/A", self)

        self.update_button = QPushButton("Update", self)
        self.update_button.clicked.connect(self.update_data)

        layout = QVBoxLayout()
        layout.addWidget(self.weather_label)
        layout.addWidget(self.joke_label)
        layout.addWidget(self.update_button)

        self.setLayout(layout)

    def update_data(self):
        # Get weather data using get_forecast from weather.py
        forecast = get_forecast()
        weather_data = "\n".join(
            [
                f"Time: {item['time'].strftime('%I %p')}, Temperature: {item['temp']}°C, Rain: {item['rain']}%"
                for item in forecast
            ]
        )

        # Get a joke using get_joke from joke.py, await it
        loop = asyncio.get_event_loop()
        joke_data = loop.run_until_complete(get_joke())

        self.weather_label.setText(
            f"12 Hour Weather Forecast in {get_location()['city']}:\n{weather_data}"
        )
        self.joke_label.setText(f"Joke:\n{joke_data}")

        # Automatically close the window after 20 seconds
        QTimer.singleShot(20000, self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherJokeWidget()
    window.show()
    sys.exit(app.exec())
