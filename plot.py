import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import QSizePolicy
import serial
from datetime import datetime

ser = serial.Serial('COM3', 9600)

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.timestamps = []
        self.dB_values = []

    def update_plot(self):
        try:
            line = ser.readline().decode('utf-8').strip()
            if line.startswith("Loudness: "):
                db_value = int(line.split(" ")[1][:-2])
                self.timestamps.append(datetime.now())
                self.dB_values.append(db_value)

                self.timestamps = self.timestamps[-100:]
                self.dB_values = self.dB_values[-100:]

                self.ax.clear()
                self.ax.plot(self.timestamps, self.dB_values, 'r-')
                self.ax.set_xlabel('Time')
                self.ax.set_ylabel('Loudness [dB]')
                self.ax.set_title('Real-time Loudness Data')
                self.fig.autofmt_xdate()
                self.draw()

        except:
            pass

    def get_min_value(self):
        if self.dB_values:
            return min(self.dB_values)
        else:
            None

    def get_max_value(self):
        if self.dB_values:
            return max(self.dB_values)
        else:
            return None

    def get_avg_value(self):
        if self.dB_values:
            return sum(self.dB_values) / len(self.dB_values)
        else:
            None
