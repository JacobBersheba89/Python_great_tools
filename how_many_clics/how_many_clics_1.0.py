from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
import pyautogui 
import screeninfo 
import pygetwindow 

mouse = Controller()

print('The current pointer position is {0}'.format(
    mouse.position))
mouse.position = (10,20)
print('Now we have moved it to {0}'.format(
    mouse.position))

mouse.press(Button.left)
mouse.release(Button.left)

