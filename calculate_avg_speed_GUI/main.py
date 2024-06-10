import sys
from PyQt6.QtWidgets import QLabel, QApplication, QPushButton, QGridLayout, QWidget, QLineEdit, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()

        # Creating widgets
        distance_label = QLabel("Enter total distance:")
        self.distance_line_edit = QLineEdit()
        time_label = QLabel("Enter total hours taken:")
        self.time_line_edit = QLineEdit()
        metric_label = QLabel("Choose metric")
        self.metric_button = QComboBox()
        self.metric_button.addItem("Km")
        self.metric_button.addItem("Miles")
