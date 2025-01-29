import tkinter as tk

root = tk.Tk()
root.title("Počítadlo kliků")
root.geometry("300x200")

counter = 0
colors = ["#312580", "g#3b42a1", "#435cde", "p#7aa3e6", "#cce7ff", "#9db0cd","#3d2157","#301939","#5e106c","#872b59", "#b1385c"]

def click():
    global counter
    counter += 1
    new_color = colors[counter % len(colors)]
    label.config(text=f"počet kliků: {counter}", fg=new_color)
    root.config(bg=new_color)

label = tk.Label(root, text="Počet kliků: 0", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Klikni", font=("Arial", 14), command=click)
button.pack()

root.mainloop()