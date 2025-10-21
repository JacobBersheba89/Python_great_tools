import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import keyboard
import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import time

TARGET_PATH = r"C:\Users\jpawlas\Desktop\Nové složky"

def create_folder():
    # tkinter GUI musí běžet v hlavním vlákně
    def ask_folder_name():
        root = tk.Tk()
        root.withdraw()
        name = simpledialog.askstring("Nová složka", "Zadej název nové složky:")
        if name:
            folder_path = os.path.join(TARGET_PATH, name)
            try:
                os.makedirs(folder_path, exist_ok=False)
                messagebox.showinfo("Hotovo", f"Složka '{name}' byla vytvořena.")
            except FileExistsError:
                messagebox.showwarning("Pozor", "Složka s tímto názvem už existuje.")
        root.destroy()

    # Spuštění tkinter dialogu v samostatném vlákně
    threading.Thread(target=ask_folder_name).start()

def keyboard_listener():
    keyboard.add_hotkey('ctrl+f5', create_folder)
    # Čeká trvale na stisk, nikdy nekončí
    while True:
        time.sleep(1)

def create_image():
    image = Image.new('RGB', (64, 64), color='blue')
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill='white')
    return image

def on_quit(icon, item):
    icon.visible = False
    icon.stop()
    os._exit(0)

def start_tray():
    image = create_image()
    menu = Menu(MenuItem('Ukončit', on_quit))
    icon = Icon("Folder Creator", image, "Folder Creator běží", menu)
    icon.run()

if __name__ == "__main__":
    # Spustí posluchač kláves ve vlákně
    threading.Thread(target=keyboard_listener, daemon=True).start()
    # Tray běží v hlavním vlákně a udržuje program aktivní
    start_tray()
