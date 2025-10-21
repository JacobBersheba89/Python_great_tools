import os
import json
import tkinter as tk
from tkinter import messagebox
import keyboard
import threading
import time

CONFIG_PATH = os.path.join(os.getenv("APPDATA"), "FolderCreatorConfig.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("default_path", "")
        except Exception:
            return ""
    return ""

def save_config(path):
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump({"default_path": path}, f, ensure_ascii=False, indent=2)
    except Exception as e:
        messagebox.showerror("Chyba při ukládání", str(e))

def create_directory():
    def run_dialog():
        modal = tk.Toplevel(root)
        modal.title("Vytvoření nové složky")
        modal.geometry("480x180")
        modal.attributes("-topmost", True)

        default_path = load_config()

        tk.Label(modal, text="Cesta k adresáři:").pack(pady=(10, 0))
        path_entry = tk.Entry(modal, width=60)
        path_entry.insert(0, default_path)
        path_entry.pack(pady=3)

        tk.Label(modal, text="Název nové složky:").pack(pady=(10, 0))
        name_entry = tk.Entry(modal, width=60)
        name_entry.pack(pady=3)

        def confirm():
            path = path_entry.get().strip()
            name = name_entry.get().strip()

            if not path:
                messagebox.showwarning("Chybí cesta", "Zadej prosím cestu k adresáři.", parent=modal)
                return
            if not os.path.exists(path):
                messagebox.showerror("Chyba", f"Cesta neexistuje:\n{path}", parent=modal)
                return
            if not name:
                messagebox.showwarning("Chybí název", "Zadej prosím název složky.", parent=modal)
                return

            save_config(path)
            new_dir = os.path.join(path, name)
            try:
                os.makedirs(new_dir)
                messagebox.showinfo("Hotovo", f"Složka vytvořena:\n{new_dir}", parent=modal)
            except FileExistsError:
                messagebox.showwarning("Pozor", "Složka už existuje.", parent=modal)
            except Exception as e:
                messagebox.showerror("Chyba", f"Nepodařilo se vytvořit složku:\n{e}", parent=modal)

            modal.destroy()

        tk.Button(modal, text="Vytvořit složku", command=confirm).pack(pady=10)
        modal.grab_set()

    # Spuštění dialogu ve vlastním vlákně
    threading.Thread(target=run_dialog).start()

# Hlavní skryté okno
root = tk.Tk()
root.withdraw()

# Nastavení hotkey (Ctrl+F5)
keyboard.add_hotkey("ctrl+f5", create_directory)

print("Aplikace běží na pozadí... (Ctrl+F5 pro vytvoření složky)")

# Nekonečná smyčka, aby aplikace běžela stále
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Aplikace ukončena.")


