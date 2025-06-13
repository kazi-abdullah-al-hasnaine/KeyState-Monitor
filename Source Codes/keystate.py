import tkinter as tk
from tkinter import ttk
from ctypes import windll
import threading
import time

# Windows API function to check toggle state
def get_key_state(vk):
    return bool(windll.user32.GetKeyState(vk) & 0x0001)

class ModernKeyFrame(tk.Frame):
    def __init__(self, parent, key_name, **kwargs):
        super().__init__(parent, **kwargs)
        self.key_name = key_name
        self.current_state = False
        self.animation_running = False
        
        # Configure the frame
        self.configure(bg="#2a2d3e", relief="flat", bd=0)
        
        # Create main container with rounded effect
        self.container = tk.Frame(self, bg="#363950", relief="flat", bd=0)
        self.container.pack(fill="both", expand=True, padx=2, pady=2)
        
        # Key name label
        self.name_label = tk.Label(
            self.container,
            text=key_name,
            font=("Segoe UI", 12, "bold"),
            bg="#363950",
            fg="#e6e6e6"
        )
        self.name_label.pack(pady=(12, 2))
        
        # Status indicator (circle)
        self.status_canvas = tk.Canvas(
            self.container,
            width=20,
            height=20,
            bg="#363950",
            highlightthickness=0
        )
        self.status_canvas.pack(pady=2)
        
        # Status text
        self.status_label = tk.Label(
            self.container,
            text="OFF",
            font=("Segoe UI", 10, "bold"),
            bg="#363950",
            fg="#ff6b6b"
        )
        self.status_label.pack(pady=(2, 12))
        
        # Initial draw
        self.draw_indicator(False)
    
    def draw_indicator(self, state):
        self.status_canvas.delete("all")
        color = "#4ecdc4" if state else "#ff6b6b"
        # Outer glow effect
        self.status_canvas.create_oval(2, 2, 18, 18, fill=color, outline=color, width=2)
        # Inner bright spot
        if state:
            self.status_canvas.create_oval(6, 6, 14, 14, fill="#7fffd4", outline="")
    
    def update_state(self, new_state):
        if new_state != self.current_state and not self.animation_running:
            self.current_state = new_state
            self.animate_change()
    
    def animate_change(self):
        if self.animation_running:
            return
        
        self.animation_running = True
        
        # Update colors and text
        if self.current_state:
            new_color = "#4ecdc4"
            new_text = "ON"
            new_bg = "#2d4a47"
        else:
            new_color = "#ff6b6b"
            new_text = "OFF"
            new_bg = "#4a2d2d"
        
        # Animate background change
        self.animate_background(new_bg)
        
        # Update status
        self.status_label.config(text=new_text, fg=new_color)
        self.draw_indicator(self.current_state)
        
        # Reset animation flag after a delay
        self.after(300, lambda: setattr(self, 'animation_running', False))
    
    def animate_background(self, target_color):
        # Simple background flash effect
        original_bg = self.container.cget("bg")
        self.container.config(bg=target_color)
        self.after(150, lambda: self.container.config(bg=original_bg))

class KeySentinelApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.setup_styles()
        self.update_status()
        
    def setup_window(self):
        self.root.title("KeyState Monitor")
        self.root.geometry("400x320")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)
        
        # Try to set window icon (optional)
        try:
            self.root.iconbitmap("")  # You can add an .ico file path here
        except:
            pass
        
        # Center the window
        self.center_window()
    
    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (320 // 2)
        self.root.geometry(f"400x320+{x}+{y}")
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="KeyState Monitor",
            font=("Segoe UI", 16, "bold"),
            bg="#1e1e2f",
            fg="#ffffff"
        )
        title_label.pack(pady=(15, 20))
        
        # Main container for key frames
        main_frame = tk.Frame(self.root, bg="#1e1e2f")
        main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Configure grid
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        
        # Create key frames
        self.caps_frame = ModernKeyFrame(main_frame, "Caps Lock", height=80)
        self.caps_frame.grid(row=0, column=0, padx=5, sticky="ew")
        
        self.num_frame = ModernKeyFrame(main_frame, "Num Lock", height=80)
        self.num_frame.grid(row=0, column=1, padx=5, sticky="ew")
        
        self.scroll_frame = ModernKeyFrame(main_frame, "Scroll Lock", height=80)
        self.scroll_frame.grid(row=0, column=2, padx=5, sticky="ew")
        
        # Status bar
        self.status_bar = tk.Label(
            self.root,
            text="● Active - Monitoring lock keys",
            font=("Segoe UI", 9),
            bg="#2a2d3e",
            fg="#4ecdc4",
            anchor="w",
            padx=10
        )
        self.status_bar.pack(fill="x", side="bottom")
        
        # Credit link
        credit_frame = tk.Frame(self.root, bg="#1e1e2f")
        credit_frame.pack(fill="x", side="bottom")
        
        credit_label = tk.Label(
            credit_frame,
            text="Created by Kazi Abdullah Al Hasnaine",
            font=("Segoe UI", 8),
            bg="#1e1e2f",
            fg="#888888",
            cursor="hand2"
        )
        credit_label.pack(pady=(5, 8))
        
       
        credit_label.bind("<Button-1>", self.open_github)
        credit_label.bind("<Enter>", lambda e: credit_label.config(fg="#4ecdc4"))
        credit_label.bind("<Leave>", lambda e: credit_label.config(fg="#888888"))
    
    def setup_styles(self):
        # Set up a modern theme using ttk
        style = ttk.Style()
        style.theme_use('clam')
    
    def open_github(self, event):
        import webbrowser
        webbrowser.open("https://github.com/kazi-abdullah-al-hasnaine")
    
    def update_status(self):
        # Virtual key codes
        caps = get_key_state(0x14)
        num = get_key_state(0x90)
        scroll = get_key_state(0x91)
        
        # Update frames
        self.caps_frame.update_state(caps)
        self.num_frame.update_state(num)
        self.scroll_frame.update_state(scroll)
        
        # Update status bar
        active_keys = sum([caps, num, scroll])
        if active_keys > 0:
            self.status_bar.config(
                text=f"● {active_keys} key{'s' if active_keys != 1 else ''} active",
                fg="#4ecdc4"
            )
        else:
            self.status_bar.config(
                text="● All keys inactive",
                fg="#ff6b6b"
            )
        
        # Schedule next update
        self.root.after(200, self.update_status)

if __name__ == "__main__":
    root = tk.Tk()
    app = KeySentinelApp(root)
    root.mainloop()