import pyperclip
import keyboard
import tkinter as tk
import threading
import pyautogui
import time  

def show_tooltip(text, duration=10000):
    x, y = pyautogui.position()
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.0)
    label = tk.Label(root, text=text, bg="moccasin", fg="black", padx=10, pady=5, font=("Arial", 14))
    label.pack()
    root.geometry(f"+{x+10}+{y+10}")

    def fade_in(current_alpha=0.0, step=0.1): 
        if current_alpha < 1.0:  
            current_alpha += step
            root.attributes("-alpha", current_alpha)
            root.after(50, fade_in, current_alpha)  
        else:
            root.attributes("-alpha", 1.0)  

    fade_in()
    root.after(duration, root.destroy)
    root.mainloop()

def on_shortcut():
    try:
        clipboard_text = pyperclip.paste()
        if clipboard_text:
            print(f"Zobrazování textu: {clipboard_text}")
            threading.Thread(target=show_tooltip, args=(clipboard_text,), daemon=True).start()
        else:
            print("Schránka je prázdná.")
    except Exception as e:
        print(f"Chyba při zpracování zkratky: {e}")

if __name__ == "__main__":
    print("Aplikace běží. Prvně zkopíruj jakýkoliv text a následně stiskni ctrl+y pro zobrazení textu. Text se zobrazí na 5 vteřin tam, kde je právě kurzor.")
    keyboard.add_hotkey("ctrl+y", on_shortcut)

    # Periodický výpis
    def periodic_feedback():
        while True:
            print("Program běží stále... Až program nebudeš potřebovat, stiskni Esc pro ukončení.")
            time.sleep(10)  

    threading.Thread(target=periodic_feedback, daemon=True).start()
    keyboard.wait("esc")
    print("Program ukončen.")

    
    #first step: pip install pyinstaller
    #second step - move in to the folder, where is the .py file (I have .py file on the desktop): cd C:\Users\jpawlas\Desktop\tooltip_project_1.4 
    #thirt step: pyinstaller --onefile text_tooltip_1.4.py
