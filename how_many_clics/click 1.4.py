import tkinter as tk
from tkinter import ttk
import mouse
import threading
import time

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Počítadlo kliků")
root.geometry("300x200")
root.configure(bg="#2c2f33")  
# Styl pro tlačítko
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 12),
                padding=10,
                background="#7289da",  
                foreground="grey")

counter = 0
tracking_enabled = True

# Poslední čas kliknutí
last_click_time = 0
click_delay = 0.01  

# Funkce pro zpracování kliknutí
def on_click(event):
    global counter, last_click_time
    current_time = time.time()

    if tracking_enabled and event.event_type == 'down' and event.button == 'left' and (current_time - last_click_time > click_delay):
        last_click_time = current_time
        counter += 1
        root.after(0, update_gui)  # Volání funkce pro aktualizaci GUI
        
#aktualizace textu po kliknutí
def update_gui():
    label.config(text=f"Počet kliků: {counter}")  

# Funkce pro zapnutí/vypnutí počítání kliků
def toggle_tracking():
    global tracking_enabled
    tracking_enabled = not tracking_enabled
    button.config(text="Zapnout počítání" if not tracking_enabled else "Vypnout počítání")

# Vytvoření GUI prvků - štítek a tlačítko
label = tk.Label(root, text="Počet kliků: 0", font=("Arial", 14), bg="#2c2f33", fg="white")
label.pack(pady=20)

button = ttk.Button(root, text="Vypnout počítání", command=toggle_tracking, style="TButton")
button.pack(pady=10)

# Funkce pro spuštění listeneru v samostatném vlákně
def start_listener():
    mouse.hook(on_click)

listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

# Spuštění hlavní smyčky Tkinteru
root.mainloop()
