import tkinter as tk
from tkinter import filedialog, messagebox
import serial
import threading
import time

class VoltmetreGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Arduino 10-bit ADC Voltmetre")
        self.root.geometry("400x380")
        self.ser = None
        self.running = False
        
        # Gösterge
        tk.Label(root, text="Ölçülen Gerilim", font=("Arial", 14)).pack(pady=10)
        self.lbl_voltage = tk.Label(root, text="0.00 V", font=("Arial", 36, "bold"), fg="blue")
        self.lbl_voltage.pack(pady=10)
        
        self.lbl_raw = tk.Label(root, text="Ham ADC Değeri (10-bit): -", font=("Arial", 10))
        self.lbl_raw.pack()
        
        # Online Mod
        frame_online = tk.LabelFrame(root, text="Online Mod (Arduino Canlı)", padx=10, pady=10)
        frame_online.pack(fill="x", padx=20, pady=10)
        self.btn_connect = tk.Button(frame_online, text="Bağlan & Oku", command=self.toggle_serial, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.btn_connect.pack(fill="x")
        
        # Offline Mod
        frame_offline = tk.LabelFrame(root, text="Offline Mod (Dosyadan Oku)", padx=10, pady=10)
        frame_offline.pack(fill="x", padx=20, pady=10)
        self.btn_file = tk.Button(frame_offline, text="CSV / TXT Dosyası Yükle", command=self.load_file)
        self.btn_file.pack(fill="x")

    def toggle_serial(self):
        if not self.running:
            try:
                self.ser = serial.Serial('COM5', 9600, timeout=1)
                self.running = True
                self.btn_connect.config(text="Durdur", bg="#f44336")
                threading.Thread(target=self.read_serial, daemon=True).start()
            except Exception as e:
                messagebox.showerror("Port Hatası", f"COM5 portuna bağlanılamadı:\n{e}\n\nSerial Monitor'ün kapalı olduğundan emin olun!")
        else:
            if self.ser:
                self.running = False
                self.ser.close()
                self.btn_connect.config(text="Bağlan & Oku", bg="#4CAF50")

    def read_serial(self):
        while self.running:
            try:
                if self.ser and self.ser.in_waiting:
                    line = self.ser.readline().decode('utf-8', errors='ignore').strip()
                    if line.isdigit():
                        raw_val = int(line)
                        voltage = (raw_val * 5.0) / 1023.0
                        self.lbl_voltage.config(text=f"{voltage:.2f} V")
                        self.lbl_raw.config(text=f"Ham ADC Değeri (10-bit): {raw_val}")
                time.sleep(0.1)
            except:
                break

    def load_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text/CSV Files", "*.txt *.csv")])
        if filepath:
            with open(filepath, "r") as f:
                lines = f.readlines()
                values = [line.strip() for line in lines if line.strip()]
            messagebox.showinfo("Dosya Yüklendi", f"{len(values)} adet veri okundu.")

if __name__ == "__main__":
    app = tk.Tk()
    VoltmetreGUI(app)
    app.mainloop()