#Basic weather app based on a youtube tutorial
import emoji
import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QCompleter
)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.api_key = "b5566d53013dd300e50f81fdfde51b89"

        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("29° C", self)
        self.emoji_label = QLabel(emoji.emojize(":sun:"))
        self.description_label = QLabel("Sunny")

        self.initUI()
        self.get_weather_button.clicked.connect(self.get_weather)

    def initUI(self):
        self.setWindowTitle("Weather App")
       # self.setWindowIcon(QIcon("C://Users\Pirila\Downloads\pyqt1.jpg"))  # Optional

        # Tried basic autocomplete hope it works.
        city_list = ["London", "Lusaka", "Paris", "New York", "Tokyo", "Nairobi", "Cairo"]
        completer = QCompleter(city_list, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.city_input.setCompleter(completer)

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        for w in [self.city_label, self.city_input, self.temperature_label,
                  self.emoji_label, self.description_label]:
            w.setAlignment(Qt.AlignCenter)

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
                font-size: 16px;
            }
            QLineEdit {
                font-family: Calibri;
                font-size: 14px;
            }
        """)

    def get_weather(self):
        city = self.city_input.text().strip()
        if not city:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                QMessageBox.critical(self, "Error", f"City not found: {city}")
                return

            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            main = data["weather"][0]["main"]

            emoji_icon = self.get_emoji(main)
            self.temperature_label.setText(f"{temp:.1f}° C")
            self.description_label.setText(description.capitalize())
            self.emoji_label.setText(emoji_icon)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to retrieve weather data:\n{e}")

    def get_emoji(self, weather):
        weather = weather.lower()
        if "cloud" in weather:
            return emoji.emojize(":cloud:")
        elif "sun" in weather or "clear" in weather:
            return emoji.emojize(":sun:")
        elif "rain" in weather:
            return emoji.emojize(":cloud_with_rain:")
        elif "snow" in weather:
            return emoji.emojize(":snowflake:")
        elif "storm" in weather or "thunder" in weather:
            return emoji.emojize(":cloud_with_lightning:")
        elif "fog" in weather or "mist" in weather:
            return emoji.emojize(":fog:")
        else:
            return emoji.emojize(":earth_africa:")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
