import pyautogui as pag
import keyboard

REGION_X_START = 497
REGION_Y_START = 220
REGION_X_END = 1331
REGION_Y_END = 517

COLOR = (149, 195, 232)

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
        flag = 0
        screen = pag.screenshot(region=REGION)

        width, height = screen.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r, g, b = screen.getpixel((x, y))

                if (r, g, b) == COLOR:
                    pag.click(x + REGION_X_START, y + REGION_Y_START)

                    flag = 1
                    break

            if flag:
                break