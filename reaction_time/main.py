import pyautogui as pag
import keyboard

running = True
work = False
while running:
    if keyboard.is_pressed('shift'):
        running = False

    if keyboard.is_pressed('ctrl'):
        work = True

    if keyboard.is_pressed('alt'):
        work = False

    if work:
        screen = pag.screenshot(region=(500, 500, 1, 1))
        r, g , b = screen.getpixel((0, 0))

        if g > 200:
            pag.click()