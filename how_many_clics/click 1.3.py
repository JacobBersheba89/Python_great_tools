import tkinter as tk
import mouse
import threading
import time

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Počítadlo kliků")
root.geometry("300x200")

# Počáteční hodnota počtu kliků
counter = 0
colors = ["#312580", "#27614e", "#435cde", "#ac4d00", "#cce7ff", "#9db0cd", "#3d2157", "#301939", "#5e106c", "#872b59", "#b1385c"]

# Poslední čas kliknutí
last_click_time = 0
click_delay = 0.01  # Nastavení minimálního intervalu mezi kliky (10 ms)

# Funkce pro zpracování kliknutí
def on_click(event):
    global counter, last_click_time
    current_time = time.time()

    # Zabráníme ztrátě rychlých kliků
    if event.event_type == 'down' and event.button == 'left' and (current_time - last_click_time > click_delay):
        last_click_time = current_time
        counter += 1
        new_color = colors[counter % len(colors)]
        
        # Aktualizace GUI v hlavním vlákně
        root.after(0, lambda: update_gui(new_color))

def update_gui(color):
    label.config(text=f"Počet kliků: {counter}", fg=color)
    root.config(bg=color)

# Vytvoření GUI prvků
label = tk.Label(root, text="Počet kliků: 0", font=("Arial", 14))
label.pack(pady=20)

# Funkce pro spuštění listeneru v samostatném vlákně
def start_listener():
    mouse.hook(on_click)

listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

# Spuštění hlavní smyčky Tkinteru
root.mainloop()

