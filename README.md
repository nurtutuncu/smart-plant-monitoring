# 🌱 Smart Plant Monitoring System

A smart plant monitoring system developed using **Arduino Uno** and **Python** to monitor soil moisture in real time and notify users when watering is needed.

---

## 📖 Project Overview

This project was designed to help users monitor their plants by measuring soil moisture continuously.

The Arduino collects data from a soil moisture sensor and sends it to a Python desktop application through serial communication. The application displays the moisture level and alerts the user when the soil becomes dry.

---

## ✨ Features

- 🌱 Real-time soil moisture monitoring
- 💻 Python desktop interface
- 📡 Arduino serial communication
- 🔔 Watering notification
- 📊 Moisture percentage display
- 🎯 Easy to use

---

## 🔧 Hardware

- Arduino Uno
- Soil Moisture Sensor
- USB Cable
- Breadboard
- Jumper Wires

---

## 💻 Software

- Arduino IDE
- Python
- PySerial
- Tkinter

---

## 📂 Project Structure

smart-plant-monitoring/
│
├── arduino/
│ └── smart_plant.ino
│
├── python/
│ └── app.py
│
├── images/
│
├── docs/
│
├── README.md
├── requirements.txt
└── LICENSE

---

## 🚀 How It Works

1. The soil moisture sensor measures the moisture level.
2. Arduino reads the sensor value.
3. The value is sent to the computer via Serial Port.
4. Python receives the data.
5. The interface displays the current moisture level.
6. If the soil is dry, the application warns the user.

---

## 📈 Future Improvements

- Temperature and humidity monitoring
- Mobile application
- Wi-Fi support (ESP32)
- Cloud data logging
- Automatic irrigation system

---

## 👩‍💻 Author

**Nur Tütüncü**

High School Student interested in

- Artificial Intelligence
- Embedded Systems
- Robotics
- Electrical & Electronics Engineering

---

## 📜 License

MIT License
