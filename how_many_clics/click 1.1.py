import tkinter as tk

root = tk.Tk()
root.title("Počítadlo kliků")
root.geometry("300x200")

counter = 0

def click():
    global counter
    counter += 1
    label.config(text=f"počet kliků: {counter}")

label = tk.Label(root, text="Počet kliků: 0", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Klikni", font=("Arial", 14), command=click)
button.pack()

root.mainloop()