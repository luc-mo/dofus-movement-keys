import pyautogui
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.up:
        pyautogui.moveTo(962, 36)
        pyautogui.click()

    elif key == keyboard.Key.left:
        pyautogui.moveTo(345, 523)
        pyautogui.click()

    elif key == keyboard.Key.right:
        pyautogui.moveTo(1571, 523)
        pyautogui.click()

    elif key == keyboard.Key.down:
        pyautogui.moveTo(962, 904)
        pyautogui.click()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

while True:
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
