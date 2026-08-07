import tkinter as tk
from tkinter import ttk
import serial
import threading
import time

# -------------------------------
# SERIAL CONNECTION
# -------------------------------

PORT = "COM3"      # Gerekirse COM4, COM5 olarak değiştir
BAUD = 9600

try:
    arduino = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2)
except:
    arduino = None


# -------------------------------
# GUI
# -------------------------------

root = tk.Tk()
root.title("Smart Plant Monitoring System")
root.geometry("500x450")
root.configure(bg="#1e1e1e")
root.resizable(False, False)


title = tk.Label(
    root,
    text="🌱 Smart Plant Monitoring",
    font=("Arial",20,"bold"),
    fg="white",
    bg="#1e1e1e"
)

title.pack(pady=20)


valueLabel = tk.Label(
    root,
    text="-- %",
    font=("Arial",48,"bold"),
    fg="#00ff99",
    bg="#1e1e1e"
)

valueLabel.pack()


statusLabel = tk.Label(
    root,
    text="Waiting for Arduino...",
    font=("Arial",18),
    fg="white",
    bg="#1e1e1e"
)

statusLabel.pack(pady=20)


messageLabel = tk.Label(
    root,
    text="",
    font=("Arial",15),
    fg="orange",
    bg="#1e1e1e"
)

messageLabel.pack()


progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=350,
    mode="determinate"
)

progress.pack(pady=30)


timeLabel = tk.Label(
    root,
    text="",
    font=("Arial",12),
    fg="gray",
    bg="#1e1e1e"
)

timeLabel.pack()


# -------------------------------
# UPDATE FUNCTION
# -------------------------------

def update_gui(moisture):

    valueLabel.config(text=f"{moisture}%")

    progress["value"] = moisture

    if moisture < 30:

        statusLabel.config(
            text="VERY DRY",
            fg="red"
        )

        messageLabel.config(
            text="⚠ Please water your plant!"
        )

    elif moisture < 60:

        statusLabel.config(
            text="DRY",
            fg="orange"
        )

        messageLabel.config(
            text="Watering is recommended."
        )

    else:

        statusLabel.config(
            text="HEALTHY",
            fg="#00ff99"
        )

        messageLabel.config(
            text="Your plant is healthy 🌿"
        )

    timeLabel.config(
        text="Last Update: " +
        time.strftime("%H:%M:%S")
    )


# -------------------------------
# READ SERIAL
# -------------------------------

def read_serial():

    while True:

        if arduino:

            try:

                line = arduino.readline().decode().strip()

                if line.startswith("Moisture:"):

                    value = line.replace("Moisture:","")
                    value = value.replace("%","")

                    moisture = int(value)

                    root.after(
                        0,
                        update_gui,
                        moisture
                    )

            except:
                pass

        time.sleep(0.2)


thread = threading.Thread(
    target=read_serial,
    daemon=True
)

thread.start()


root.mainloop()
