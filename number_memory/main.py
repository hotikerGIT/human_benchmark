import pyautogui as pag
import keyboard
import time

import pyscreeze

REG_X_START = 300
REG_Y_START = 330
REG_X_END = 1400
REG_Y_END = 100

INPUT_X = 1000
INPUT_Y = 400

SUBMIT_X = 1000
SUBMIT_Y = 500

NEXT_X = 1000
NEXT_Y = 550

REGION = (
    REG_X_START,
    REG_Y_START,
    REG_X_END,
    REG_Y_END
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
        screen = pag.screenshot('temp.png', region=REGION)
        num_cord = {}
        text = ''

        for num in range(10):
            num = str(num)
            photo = f'assets/{num}.png'

            data = pag.locateAll(photo, screen)

            try:
                for t in data:
                    num_cord[num] = t[0] if t[1] < 400 else t[0] * 100

            except pyscreeze.ImageNotFoundException:
                pass

        num_in_order = dict(sorted(num_cord.items(), key=lambda item: item[1]))

        for key, _ in num_in_order.items():
            text += key

        print(text)
        time.sleep(2)

        pag.click(INPUT_X, INPUT_Y)
        pag.typewrite(text)

        pag.click(SUBMIT_X, SUBMIT_Y)
        time.sleep(1)

        pag.click(NEXT_X, NEXT_Y)
        time.sleep(1)