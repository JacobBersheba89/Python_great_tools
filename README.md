## 1 ##
📂 text_tooltip 📂

CZ Aplikace text_tooltip je jednoduchý a užitečný nástroj pro zobrazování zkopírovaného textu jako tooltipu přímo u kurzoru. Tento projekt jsem vytvořil pro potřeby kontroly různých dat, kdy kopírujeme text a potřebujeme jej porovnat.. <br><br>
EN The text_tooltip app is a simple and handy tool that displays copied text as a tooltip right next to the cursor. This project was created for the needs of checking different data when we copy text and need to compare it..

<span style="color: blue;"> ### Funkce ### </span>
V první řadě musíte vytvořit .exe soubor. <br>
Je to jednoduché. Použitjete VS code a konzoli (View -> Terminal) a zadaáte tyto příkazy:<br>
je potřeba být ve složce, ve které se nachází python soubor text_tooltip_1.1.py:<br>
cd C:\Users\jpawlas\Desktop\tooltip_project<br>
pip install pyinstaller<br>
pyinstaller --onefile text_tooltip_1.1.py #### Tento příkaz vytvoří kompletní program. #### <br>

Po spuštění program otevře okno, ve kterém uvidíte probíhající děje.<br> 
Pokud použijeme klávesovou zkratku ctrl+c, text se zkopíruje také do paměti programu.<br>
Prostřednictvím zkratky ctrl+shift+q zobrazíme zkopírovaný text vedle kurzoru myši. <br>
Text v rámečku zmizí po 5000 milisekundách.<br>
Samozřejmě program si můžete v .py souboru upravovat. <br>
V konzoli VS code můžete následně vytvořit celý nový .exe program pomocí příkazu: pyinstaller **--onefile text_tooltip_1.1.py**<br>
ten bude reagovat na vaše úpravy. <br>

<span style="color: blue;">Toto je modrý text.### Features ### </span>  
First of all, you need to create an .exe file.<br>
It's simple. You use VS code and the console (View -> Terminal) and enter these commands:<br>
You need to be in the folder where the python file text_tooltip_1.1.py is located:<br>
cd C:\Users\jpawlas\Desktop\tooltip_project<br>
pip install pyinstaller<br>
pyinstaller --onefile text_tooltip_1.1.py #### This command will create a complete program. ####<br>

After running the program, a window will open in which you can see the current events.<br>
If we use the keyboard shortcut ctrl+c, the text will also be copied to the program memory.<br>
Using the shortcut ctrl+shift+q, we will display the copied text next to the mouse cursor.<br>
The text in the frame will disappear after 5000 milliseconds.<br>
Of course, you can edit the program in the .py file.<br>
In the VS code console, you can then create a whole new .exe program using the command: pyinstaller **--onefile text_tooltip_1.1.py**<br>
which will respond to your edits.<br>

####libraries####
<span style="color: FF66FF;"> import pyperclip </span>
import keyboard
import tkinter as tk
import threading
import pyautogui
import time 
