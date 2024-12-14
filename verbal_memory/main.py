import pyautogui as pag
import pytesseract as ts
import keyboard

REGION_X_START = 700
REGION_Y_START = 350
REGION_X_END = 600
REGION_Y_END = 100

REGION = (
    REGION_X_START,
    REGION_Y_START,
    REGION_X_END,
    REGION_Y_END
)

SEEN = (900, 475)
NEW = (1050, 475)

word_list = set()

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
        word = pag.screenshot(region=REGION)
        text = ts.image_to_string(word)

        if text in word_list:
            pag.click(*SEEN)

        else:
            word_list.add(text)
            pag.click(*NEW)
