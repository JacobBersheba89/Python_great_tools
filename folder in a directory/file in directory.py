import os
import tkinter as tk
from tkinter import simpledialog, messagebox
import keyboard

def create_directory():
    # Inicializace GUI
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)  # 🟢 Zaručí, že se okno objeví v popředí

    # 1️⃣ Zadání cesty
    target_path = simpledialog.askstring("Cíl", "Zadej cestu, kam chceš vytvořit adresář:", parent=root)
    if not target_path:
        messagebox.showinfo("Zrušeno", "Nebyla zadána žádná cesta.", parent=root)
        root.destroy()
        return
    if not os.path.exists(target_path):
        messagebox.showerror("Chyba", f"Cesta neexistuje:\n{target_path}", parent=root)
        root.destroy()
        return

    # 2️⃣ Zadání názvu nové složky
    folder_name = simpledialog.askstring("Název složky", "Zadej název nové složky:", parent=root)
    if not folder_name:
        messagebox.showinfo("Zrušeno", "Nebyl zadán název složky.", parent=root)
        root.destroy()
        return

    new_folder_path = os.path.join(target_path, folder_name)

    # 3️⃣ Vytvoření složky
    try:
        os.makedirs(new_folder_path)
        messagebox.showinfo("Hotovo", f"Složka vytvořena:\n{new_folder_path}", parent=root)
    except FileExistsError:
        messagebox.showwarning("Pozor", "Složka už existuje.", parent=root)
    except Exception as e:
        messagebox.showerror("Chyba", f"Nepodařilo se vytvořit složku:\n{e}", parent=root)

    root.destroy()

# 🧩 Klávesová zkratka
keyboard.add_hotkey("ctrl+f5", create_directory)

print("Skript běží... (Ctrl+F5 pro vytvoření složky, ESC pro ukončení)")
keyboard.wait("esc")


