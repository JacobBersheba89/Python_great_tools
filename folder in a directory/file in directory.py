import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import keyboard
import pandas

# Základní cesta, kam se budou vytvářet nové složky
base_path = r"C:\Users\jpawlas\OneDrive - Státní fond životního prostředí ČR\Plocha\Výpisy"

def create_new_folder():
    # Otevře malé dialogové okno pro zadání názvu složky
    root = tk.Tk()
    root.withdraw()  # skryje hlavní okno
    folder_name = simpledialog.askstring("Nová složka", "Zadej název nové složky:")
    
    if folder_name:
        new_folder_path = os.path.join(base_path, folder_name)
        try:
            os.makedirs(new_folder_path)
            messagebox.showinfo("Hotovo", f"Vytvořeno: {new_folder_path}")
        except Exception as e:
            messagebox.showerror("Chyba", f"Chyba při vytváření složky: {e}")
    root.destroy()

# Nastavení klávesové zkratky Ctrl+F5
keyboard.add_hotkey('ctrl+U', create_new_folder)

print("Program běží. Stiskni Ctrl+U pro vytvoření nové složky. Pro ukončení stiskni Ctrl+C.")
keyboard.wait()

