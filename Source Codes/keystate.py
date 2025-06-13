import tkinter as tk
from ctypes import windll

# Windows API function to check toggle state
def get_key_state(vk):
    return bool(windll.user32.GetKeyState(vk) & 0x0001)

class KeySentinelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("KeySentinel - Lock Key Monitor")
        self.root.geometry("320x160")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)

        self.label_caps = tk.Label(root, font=('Arial', 14), bg="#1e1e2f")
        self.label_num = tk.Label(root, font=('Arial', 14), bg="#1e1e2f")
        self.label_scroll = tk.Label(root, font=('Arial', 14), bg="#1e1e2f")

        self.label_caps.pack(pady=8)
        self.label_num.pack(pady=8)
        self.label_scroll.pack(pady=8)

        self.update_status()

    def update_status(self):
        # Virtual key codes
        caps = get_key_state(0x14)
        num = get_key_state(0x90)
        scroll = get_key_state(0x91)

        self.set_label(self.label_caps, "Caps Lock", caps)
        self.set_label(self.label_num, "Num Lock", num)
        self.set_label(self.label_scroll, "Scroll Lock", scroll)

        self.root.after(200, self.update_status)

    def set_label(self, label, name, state):
        color = "#00ff00" if state else "#ff5555"
        label.config(text=f"{name}: {'ON' if state else 'OFF'}", fg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeySentinelApp(root)
    root.mainloop()
