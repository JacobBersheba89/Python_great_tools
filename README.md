<h1>PYTHON_EXPERIMETALS</h1>

### I'm trying to point everything towards python 🐍. All new experiences show how usable, variable, all-encompassing, fun and above all how fast python can be. I'm really surprised that a lot of complex kernels don't run on python. The base are the libraries... biolion of options...  ### <br>

### Všechno se snažím směřovat k pythonu. Veškeré nové zkušenosti ukazují, jak moc je python použitelný, variabilní, všepokrývající, zábavný a především jak může být rychlý. Moc se divím, že spoustu složitých jader neběží na pythonu. Základ jsou rozhodně knihovny.. miliardy možností..  ###


## 1 ##
📂 text_tooltip 📂

CZ Aplikace text_tooltip je jednoduchý a užitečný nástroj pro zobrazování zkopírovaného textu jako tooltipu přímo u kurzoru. Tento projekt jsem vytvořil pro potřeby kontroly různých dat, kdy kopírujeme text a potřebujeme jej porovnat.. <br><br>
EN The text_tooltip app is a simple and handy tool that displays copied text as a tooltip right next to the cursor. This project was created for the needs of checking different data when we copy text and need to compare it..

## Funkce ##
V první řadě musíte vytvořit .exe soubor. <br>
Je to jednoduché. Použitjete VS code a konzoli (View -> Terminal) a zadaáte tyto příkazy:<br>
je potřeba být ve složce, ve které se nachází python soubor text_tooltip_1.1.py:<br>
Do terminálu zadejte:
➡️ cd C:\Users\Desktop\tooltip_project<br>
➡️ pip install pyinstaller<br>
➡️ pyinstaller --onefile text_tooltip_1.1.py #### Tento příkaz vytvoří kompletní program. #### <br>

Po spuštění programu se otevře okno, ve kterém uvidíte probíhající děje.<br> 
Pokud použijeme klávesovou zkratku ctrl+c, text se zkopíruje také do paměti programu.<br>
Prostřednictvím zkratky ctrl+shift+q zobrazíme zkopírovaný text vedle kurzoru myši. <br>
Text v rámečku zmizí po 5000 milisekundách.<br>
Samozřejmě program si můžete v .py souboru upravovat. <br>
V konzoli VS code můžete následně vytvořit celý nový .exe program pomocí příkazu: pyinstaller **--onefile text_tooltip_1.1.py**<br>
ten bude reagovat na vaše úpravy. <br>

## Features ##
First of all, you need to create an .exe file.<br>
It's simple. You use VS code and the console (View -> Terminal) and enter these commands:<br>
You need to be in the folder where the python file text_tooltip_1.1.py is located:<br>
➡️ cd C:\Users\Desktop\tooltip_project<br>
➡️ pip install pyinstaller<br>
➡️ pyinstaller --onefile text_tooltip_1.1.py #### This command will create a complete program. ####<br>

After running the program, a window will open in which you can see the current events.<br>
If we use the keyboard shortcut ctrl+c, the text will also be copied to the program memory.<br>
Using the shortcut ctrl+shift+q, we will display the copied text next to the mouse cursor.<br>
The text in the frame will disappear after 5000 milliseconds.<br>
Of course, you can edit the program in the .py file.<br>
In the VS code console, you can then create a whole new .exe program using the command: pyinstaller **--onefile text_tooltip_1.1.py**<br>
which will respond to your edits.<br>

## libraries ##
📗import pyperclip <br>
📘import keyboard<br>
📙import tkinter as tk<br>
📔import threading<br>
📖import pyautogui<br>
📚import time <br>

## 2 ##
📂 click 📂

This small app counting yours mouse clicking.. in first versions it´s just about GUI app windows.. and you have to click buttom for count +1
The goal is to make more usefull app, which will counting not just mouse clicking but also move of cursor. 
Also want to next steps follow os my visiting websites, computer apps etc. 
This instruments would like to use for monitoring of my computer works. 
📚🚧⛔ library @pyinput se ukázalo jako méně funkční řešení...

## libraries ##
📙import tkinter as tk<br>
📔import mouse
📖import threading
📘import time


## 3 ##
📂 folder_in_a-directory 📂

This little app will create a directory for you wherever you enter it. It's simply an app for officials and managers who need to create folders quickly. They have large directories and simply want to save themselves work. Just press ctrl+F5 and watch this!

📔 import os
📙 import tkinter as tk
📗 from tkinter import simpledialog, messagebox
📖 import keyboard
