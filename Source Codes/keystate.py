import tkinter as tk
from tkinter import Label
import keyboard  # pip install keyboard

class KeySentinelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KeySentinel - Lock Key Monitor")
        self.root.geometry("320x160")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)

        self.labels = {
            'Caps Lock': Label(root, font=('Arial', 14), bg="#1e1e2f", fg="white"),
            'Num Lock': Label(root, font=('Arial', 14), bg="#1e1e2f", fg="white"),
            'Scroll Lock': Label(root, font=('Arial', 14), bg="#1e1e2f", fg="white"),
        }

        for i, label in enumerate(self.labels.values()):
            label.pack(pady=8)

        self.update_status()

    def update_status(self):
        for key in self.labels:
            is_on = keyboard.is_pressed(key.lower())
            color = "#00ff00" if is_on else "#ff5555"
            status_text = f"{key}: {'ON' if is_on else 'OFF'}"
            self.labels[key].config(text=status_text, fg=color)

        # Schedule the next update in 200 ms
        self.root.after(200, self.update_status)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeySentinelApp(root)
    root.mainloop()
