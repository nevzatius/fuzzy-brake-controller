#!/usr/bin/env python3
"""
qt_gui.py

PyQt5 tabanlı basit GUI uygulaması. Fuzzy Brake Controller hesaplamalarını bu arayüze entegre edebilirsiniz.
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QSlider, QPushButton
)
from PyQt5.QtCore import Qt
from fuzzy_brake_controller import create_brake_controller

class BrakeControllerGUI(QWidget):
    def __init__(self):
        super().__init__()
        # Bulanık kontrol simülatörü oluştur
        self.sim = create_brake_controller()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Fuzzy Brake Controller (Qt5)')
        layout = QVBoxLayout()

        # Parametre tanımları: name: (min, max, default, label_text)
        self.params = {
            'speed': (0, 200, 60, 'Hız (km/h)'),
            'brake_pressure': (0, 100, 50, 'Fren Basıncı (%)'),
            'road_grip': (0, 100, 70, 'Yol Tutuş (%)'),
            'slope': (-10, 10, 0, 'Eğim (°)'),
            'tire_temp': (0, 120, 50, 'Lastik Sıcaklığı (°C)')
        }
        self.sliders = {}
        self.labels = {}

        # Girdi slider'ları ve etiketler
        for name, (mn, mx, default, text) in self.params.items():
            lbl = QLabel(f"{text}: {default}")
            slider = QSlider(Qt.Horizontal)
            slider.setRange(mn, mx)
            slider.setValue(default)
            slider.valueChanged.connect(lambda val, n=name: self.on_value_change(n, val))
            layout.addWidget(lbl)
            layout.addWidget(slider)
            self.labels[name] = lbl
            self.sliders[name] = slider

        # Hesapla butonu
        btn = QPushButton('Hesapla')
        btn.clicked.connect(self.compute)
        layout.addWidget(btn)

        # Çıktı etiketleri
        self.result_front = QLabel('Ön Fren Dağılımı: –')
        self.result_rear  = QLabel('Arka Fren Dağılımı: –')
        layout.addWidget(self.result_front)
        layout.addWidget(self.result_rear)

        self.setLayout(layout)

    def on_value_change(self, name, val):
        # Slider hareket ettiğinde etiketi güncelle
        text = self.params[name][3]
        self.labels[name].setText(f"{text}: {val}")
        # Anlık hesaplama
        self.compute()

    def compute(self):
        # Tüm girdileri simülatöre ayarla ve hesapla
        for name, slider in self.sliders.items():
            self.sim.input[name] = slider.value()
        self.sim.compute()
        front = self.sim.output.get('front_bias', 0)
        rear  = self.sim.output.get('rear_bias', 0)
        self.result_front.setText(f"Ön Fren Dağılımı: {front:.1f}%")
        self.result_rear.setText(f"Arka Fren Dağılımı: {rear:.1f}%")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = BrakeControllerGUI()
    gui.show()
    sys.exit(app.exec_())