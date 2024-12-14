import pytesseract as ts
import pyautogui as pag
import keyboard
import cv2
import os

REGION_X_START = 400
REGION_Y_START = 330
REGION_X_END = 1100
REGION_Y_END = 220

REGION = (
    REGION_X_START,
    REGION_Y_START,
    REGION_X_END,
    REGION_Y_END
)

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
        screen = pag.screenshot('tmp.png', region=REGION)

        img = cv2.imread('tmp.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        text = ts.image_to_string(screen) * 2
        pag.click(500, 500)

        pag.typewrite(text)

        work = False

        os.remove('tmp.png')