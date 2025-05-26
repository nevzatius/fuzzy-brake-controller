#!/usr/bin/env python3
"""
fuzzy_brake_controller.py

Python ile otomotiv için fren basıncı dağılımını bulanık mantıkla kontrol eden tek dosyalık uygulama.
Girdiler: hız, fren_basıncı, yol_tutuş, eğim, lastik_sıcaklığı
Çıktılar: ön_fren_dağılımı, arka_fren_dağılımı
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Bulanık Mantık Kontrolcüsü Tanımı ---
def create_brake_controller():
    speed = ctrl.Antecedent(np.arange(0, 201, 1), 'speed')            # km/h
    brake_pressure = ctrl.Antecedent(np.arange(0, 101, 1), 'brake_pressure')  # % pedala basma
    road_grip = ctrl.Antecedent(np.arange(0, 101, 1), 'road_grip')       # yol tutuş katsayısı %
    slope = ctrl.Antecedent(np.arange(-10, 11, 1), 'slope')           # eğim derece
    tire_temp = ctrl.Antecedent(np.arange(0, 121, 1), 'tire_temp')       # lastik sıcaklığı °C

    front_bias = ctrl.Consequent(np.arange(0, 101, 1), 'front_bias')      # ön fren %
    rear_bias = ctrl.Consequent(np.arange(0, 101, 1), 'rear_bias')       # arka fren %

    # Üyelik fonksiyonları
    speed['low']    = fuzz.trimf(speed.universe, [0, 0, 80])
    speed['medium'] = fuzz.trimf(speed.universe, [60, 100, 140])
    speed['high']   = fuzz.trimf(speed.universe, [120, 200, 200])

    brake_pressure['light'] = fuzz.trimf(brake_pressure.universe, [0, 0, 40])
    brake_pressure['medium'] = fuzz.trimf(brake_pressure.universe, [30, 60, 90])
    brake_pressure['heavy'] = fuzz.trimf(brake_pressure.universe, [80,100,100])

    road_grip['low']    = fuzz.trimf(road_grip.universe, [0, 0, 40])
    road_grip['medium'] = fuzz.trimf(road_grip.universe, [30, 50, 70])
    road_grip['high']   = fuzz.trimf(road_grip.universe, [60,100,100])

    slope['down']  = fuzz.trimf(slope.universe, [-10,-10,0])
    slope['flat']  = fuzz.trimf(slope.universe, [-2,0,2])
    slope['up']    = fuzz.trimf(slope.universe, [0,10,10])

    tire_temp['cold']   = fuzz.trimf(tire_temp.universe, [0, 0, 40])
    tire_temp['normal'] = fuzz.trimf(tire_temp.universe, [30,60,90])
    tire_temp['hot']    = fuzz.trimf(tire_temp.universe, [80,120,120])

    front_bias['low']    = fuzz.trimf(front_bias.universe, [0,0,40])
    front_bias['medium'] = fuzz.trimf(front_bias.universe, [30,50,70])
    front_bias['high']   = fuzz.trimf(front_bias.universe, [60,100,100])

    rear_bias['low']     = fuzz.trimf(rear_bias.universe, [0,0,40])
    rear_bias['medium']  = fuzz.trimf(rear_bias.universe, [30,50,70])
    rear_bias['high']    = fuzz.trimf(rear_bias.universe, [60,100,100])

    # Kural tabanı: kombinasyon ve fallback kuralları
    rules = []
    rules += [
        ctrl.Rule(brake_pressure['light'] & speed['high'], front_bias['medium']),
        ctrl.Rule(brake_pressure['heavy'] & road_grip['low'], rear_bias['medium']),
        ctrl.Rule(slope['down'] & brake_pressure['heavy'], rear_bias['high']),
        ctrl.Rule(slope['up'] & brake_pressure['heavy'], front_bias['high']),
        ctrl.Rule(tire_temp['cold'] & brake_pressure['heavy'], rear_bias['medium']),
        ctrl.Rule(tire_temp['hot']  & brake_pressure['light'], front_bias['low']),
    ]
    rules += [
        ctrl.Rule(speed['low'], front_bias['low']),
        ctrl.Rule(speed['medium'], front_bias['medium']),
        ctrl.Rule(speed['high'], front_bias['high']),
        ctrl.Rule(brake_pressure['light'], front_bias['low']),
        ctrl.Rule(brake_pressure['medium'], front_bias['medium']),
        ctrl.Rule(brake_pressure['heavy'], front_bias['high']),
        ctrl.Rule(brake_pressure['light'], rear_bias['low']),
        ctrl.Rule(brake_pressure['medium'], rear_bias['medium']),
        ctrl.Rule(brake_pressure['heavy'], rear_bias['high']),
        ctrl.Rule(road_grip['low'], rear_bias['high']),
        ctrl.Rule(road_grip['medium'], rear_bias['medium']),
        ctrl.Rule(road_grip['high'], rear_bias['low']),
        ctrl.Rule(slope['down'], rear_bias['medium']),
        ctrl.Rule(slope['up'], front_bias['medium']),
        ctrl.Rule(tire_temp['cold'], rear_bias['low']),
        ctrl.Rule(tire_temp['hot'], front_bias['medium']),
    ]

    system = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(system)

# --- Basit Tkinter GUI ---
def launch_gui(ctrl_sim):
    root = tk.Tk()
    root.title("Otomotiv Fren Dağılım Kontrolü")
    root.geometry("450x550")

    vars_def = {
        'speed': ('Hız (km/h)', 0, 200, 60),
        'brake_pressure': ('Fren Basıncı (%)', 0, 100, 50),
        'road_grip': ('Yol Tutuş (%)', 0, 100, 70),
        'slope': ('Eğim (°)', -10, 10, 0),
        'tire_temp': ('Lastik Sıcaklığı (°C)', 0, 120, 50)
    }

    sliders = {}
    labels = {}

    def update_and_compute(var_name, val):
        labels[var_name].config(text=f"{float(val):.0f}")
        for vn, var in sliders.items():
            ctrl_sim.input[vn] = var.get()
        ctrl_sim.compute()
        front = ctrl_sim.output.get('front_bias', 0)
        rear = ctrl_sim.output.get('rear_bias', 0)
        lbl_front.config(text=f"Ön Fren Dağılımı: {front:.1f}%")
        lbl_rear.config(text=f"Arka Fren Dağılımı: {rear:.1f}%")

    lbl_front = ttk.Label(root, text="Ön Fren Dağılımı: –", font=('Arial', 11, 'bold'))
    lbl_front.pack(pady=(10,5))
    lbl_rear = ttk.Label(root, text="Arka Fren Dağılımı: –", font=('Arial', 11, 'bold'))
    lbl_rear.pack(pady=(0,10))

    for vn, (text, mn, mx, default) in vars_def.items():
        frame = ttk.Frame(root)
        frame.pack(fill='x', padx=10, pady=5)
        ttk.Label(frame, text=text).pack(anchor='w')
        var = tk.DoubleVar(value=default)
        slider = ttk.Scale(frame, from_=mn, to=mx, variable=var,
                           command=lambda val, name=vn: update_and_compute(name, val))
        slider.pack(fill='x')
        val_lbl = ttk.Label(frame, text=f"{default}")
        val_lbl.pack(anchor='e')
        sliders[vn] = var
        labels[vn] = val_lbl

    ttk.Button(root, text="Hesapla", command=lambda: update_and_compute('speed', sliders['speed'].get())).pack(pady=15)
    root.mainloop()

# Main
if __name__ == '__main__':
    sim = create_brake_controller()
    launch_gui(sim)
