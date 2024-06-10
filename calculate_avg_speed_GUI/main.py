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

        button = QPushButton("Calculate")
        button.clicked.connect(self.calculate)
        self.output = QLabel("")

        # Adding widgets
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(metric_label, 0, 2)
        grid.addWidget(self.metric_button, 1, 2)
        grid.addWidget(button, 2, 0, 1, 2)
        grid.addWidget(self.output, 3, 0, 1, 3)

        self.setLayout(grid)

    def calculate(self):
        if self.metric_button.currentText() == "Km":
            output = int(self.distance_line_edit.text()) / int(self.time_line_edit.text())
            self.output.setText(f"You were traveling at {str(round(output, 2))} Km per hour")

        else:
            output = int(self.distance_line_edit.text()) / int(self.time_line_edit.text())
            self.output.setText(f"You were traveling at {str(round(output, 2))} miles per hour")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
