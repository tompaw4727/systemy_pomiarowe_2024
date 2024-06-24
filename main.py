import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer
from ui_main import Ui_MainWindow
from plot import MplCanvas
from plot import ser
import os
import datetime
from ui_info_widget import Ui_Form

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Ustawianie wykresu na widgecie
        self.canvas = MplCanvas(self.plot_widget, width=5, height=4, dpi=100)
        layout = QVBoxLayout(self.plot_widget)
        layout.addWidget(self.canvas)

        # Timer dla aktualizacji wykresow
        self.timer = QTimer()
        self.timer.setInterval(200)  # Update every 200 ms
        self.timer.timeout.connect(self.canvas.update_plot)

        # Timer dla aktualizowania textBoxow
        self.value_update_timer = QTimer()
        self.value_update_timer.setInterval(1000)  # Update every 1000 ms (1 second)
        self.value_update_timer.timeout.connect(self.update_values)


        self.start_button.clicked.connect(self.toggle_measurement)
        self.clean_button.clicked.connect(self.clear_plot_and_texts)
        self.save_button.clicked.connect(self.save_mesaurement)
        self.info_button.clicked.connect(self.show_info_widget)

    def toggle_measurement(self):
        if self.timer.isActive():
            self.timer.stop()
            self.value_update_timer.stop()
            self.start_button.setText("Start")
        else:
            self.timer.start()
            self.value_update_timer.start()
            self.start_button.setText("Stop")

    def clear_plot_and_texts(self):
        self.timer.stop()
        self.value_update_timer.stop()
        self.start_button.setText("Start")

        self.canvas.timestamps.clear()
        self.canvas.dB_values.clear()
        self.canvas.ax.clear()
        self.canvas.ax.set_xlabel('Time')
        self.canvas.ax.set_ylabel('Loudness [dB]')
        self.canvas.ax.set_title('Real-time Loudness Data')
        self.canvas.draw()

        self.min_text_browser.clear()
        self.max_text_browser.clear()
        self.avg_text_browser.clear()
        self.scale_text_browser.celar()

    def save_mesaurement(self):
        self.timer.stop()
        self.value_update_timer.stop()
        self.start_button.setText("Start")

        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(desktop_path, "loudness_" + str(current_time) + "_.txt")

        with open(file_path, 'w') as file:
            for timestamp, db_value in zip(self.canvas.timestamps, self.canvas.dB_values):
                file.write(f"{timestamp} - {db_value}\n")

    def update_plot(self):
        self.canvas.update_plot()

    def update_values(self):
        self.update_min_text_browser()
        self.update_max_text_browser()
        self.update_avg_text_browser()
        self.update_scale_text_browser()

    def update_min_text_browser(self):
        min_value = self.canvas.get_min_value()
        if min_value is not None:
            self.min_text_browser.setText(f"{min_value} [dB]")

    def update_max_text_browser(self):
        max_value = self.canvas.get_max_value()
        if max_value is not None:
            self.max_text_browser.setText(f"{max_value} [dB]")

    def update_avg_text_browser(self):
        avg_value = self.canvas.get_avg_value()
        if avg_value is not None:
            self.avg_text_browser.setText(f"{round(avg_value, 2)} [dB]")

    def update_scale_text_browser(self):
        if self.canvas.dB_values:
            current_value = self.canvas.dB_values[-1]
            if current_value < 10:
                scale = "Very quiet"
                color = "blue"
            elif 10 <= current_value < 20:
                scale = "Quiet sounds"
                color = "blue"
            elif 20 <= current_value < 30:
                scale = "Whisper"
                color = "blue"
            elif 30 <= current_value < 40:
                scale = "Quiet office"
                color = "blue"
            elif 40 <= current_value < 50:
                scale = "Moderate rainfall"
                color = "blue"
            elif 50 <= current_value < 60:
                scale = "Normal conversation"
                color = "green"
            elif 60 <= current_value < 70:
                scale = "Vacuum cleaner"
                color = "green"
            elif 70 <= current_value < 80:
                scale = "Restaurant"
                color = "yellow"
            elif 80 <= current_value < 90:
                scale = "Hair dryer"
                color = "yellow"
            elif 90 <= current_value < 100:
                scale = "Motorcycle"
                color = "orange"
            elif 100 <= current_value < 110:
                scale = "Nightclub"
                color = "orange"
            elif 110 <= current_value < 120:
                scale = "Concert"
                color = "red"
            elif 120 <= current_value < 130:
                scale = "Jackhammer"
                color = "red"
            elif current_value >= 130:
                scale = "Fireworks"
                color = "red"

            self.scale_text_browser.setText(scale)
            self.scale_text_browser.setStyleSheet(f"color: {color}; border: 2px solid #555; border-style: outset;")

    def show_info_widget(self):
        self.info_widget = QWidget()
        self.ui_info_widget = Ui_Form()
        self.ui_info_widget.setupUi(self.info_widget)
        self.info_widget.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

ser.close()