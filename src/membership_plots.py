#!/usr/bin/env python3
"""
membership_plots.py

Bu script, örnek olarak 'speed' değişkeni için tanımlanan üçgen üyelik fonksiyonlarını çizer
ve ekranda gösterir. Diğer değişkenler için de benzer şekilde grafik oluşturabilirsiniz.
"""
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

def plot_speed_mfs():
    # 'Speed' değişkeni için evren
    x_speed = np.arange(0, 201, 1)
    # Üyelik fonksiyonları
    speed_low    = fuzz.trimf(x_speed, [0,   0,  80])
    speed_medium = fuzz.trimf(x_speed, [60, 100, 140])
    speed_high   = fuzz.trimf(x_speed, [120, 200, 200])

    plt.figure()
    plt.plot(x_speed, speed_low,    label='Low')
    plt.plot(x_speed, speed_medium, label='Medium')
    plt.plot(x_speed, speed_high,   label='High')
    plt.title('Speed Membership Functions')
    plt.xlabel('Speed (km/h)')
    plt.ylabel('Membership Degree')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    plot_speed_mfs()
