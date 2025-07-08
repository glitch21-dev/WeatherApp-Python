import emoji
from PyQt5.QtGui import QIcon
from emoji import emojize
import sys
import requests
from PyQt5.QtWidgets import(QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temparature_label = QLabel("29° C", self)
        self.emoji_label = QLabel(emojize(":sun:"))
        self.description_label = QLabel("Sunny")

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setWindowIcon(QIcon(r"C:\Users\Pirila\Downloads\pyqt1.jpg"))

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        se



if __name__== "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())