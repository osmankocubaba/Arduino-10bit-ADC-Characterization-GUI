# Arduino 10-Bit ADC Characterization and GUI Voltmeter

This project covers the experimental characterization of the ATmega328P internal 10-bit SAR ADC on an Arduino Uno and features a dual-mode desktop voltmeter application developed in Python.

## Key Features
- **Hardware Circuit:** 10 kΩ linear rotary potentiometer voltage divider connected to Arduino Analog Pin A1.
- **Arduino Firmware:** C++ code sampling the ADC and streaming raw integer values (0–1023) at 9600 baud rate.
- **Python Desktop GUI:** Dual-mode (Online/Offline) interface developed using Tkinter and PySerial, multithreaded to ensure real-time voltage monitoring without UI lag.
- **Performance Evaluation:** Linearity and INL evaluation, quantization analysis, and characterization of the USB bus supply voltage drop (4.82 V saturation).

## AI Tool Acknowledgment
The Arduino C++ firmware and Python GUI scripts were developed with the assistance of Generative AI tools (ChatGPT) for algorithm structuring and serial communication handling.

## Repository Contents
- `Arduino-10bit-ADC-Characterization-and-GUI-Report.pdf`: Comprehensive lab report covering theoretical calculations, measurements, and error analysis.
- `adc_firmware.ino`: Microcontroller firmware source code.
- `adc_gui.py`: Python desktop voltmeter application source code.
