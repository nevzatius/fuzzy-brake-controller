#!/usr/bin/env python3
"""
main.py

Bu script, komut satırından --gui argümanıyla
Tkinter veya PyQt5 tabanlı GUI'yi ayağa kaldırır.
"""
import argparse

def run_tkinter():
    from fuzzy_brake_controller import create_brake_controller, launch_gui
    sim = create_brake_controller()
    launch_gui(sim)

def run_pyqt():
    import qt_gui
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    gui = qt_gui.BrakeControllerGUI()
    gui.show()
    sys.exit(app.exec_())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gui', choices=['tk', 'qt'], required=True,
                        help='Çalıştırılacak GUI: "tk" için Tkinter, "qt" için PyQt5')
    args = parser.parse_args()

    if args.gui == 'tk':
        run_tkinter()
    else:
        run_pyqt()

if __name__ == '__main__':
    main()
