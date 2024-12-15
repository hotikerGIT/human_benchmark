import keyboard
import time
import pyautogui as pag

# square coordinates
matrix_dict = [
    (850, 300),
    (975, 300),
    (1100, 300),
    (850, 425),
    (975, 425),
    (1100, 425),
    (850, 550),
    (975, 550),
    (1100, 550)
]

# current sequence
sequence = []

'''
these are the most important parameters
the more exact they are, the better the score will be

this parameter are based off on tests, not calculations.
it is enough to get you a score of 100.
'''

SQUARE_FLASH = 0.5125
SCREEN_FLASH = 1

running = True
work = False
while running:
    if keyboard.is_pressed('shift'):
        running = False

    if keyboard.is_pressed('ctrl'):
        # NOTE: in order for programme to work properly,
        # you should launch it while the first square is flashing on the screen
        work = True

    if keyboard.is_pressed('alt'):
        work = False
        sequence = []

    if work:
        # skipping previous steps as we memorized them already
        for i in range(len(sequence)):
            time.sleep(SQUARE_FLASH)

        # screening the last square, which is new
        screen = pag.screenshot(region=(849, 299, 252, 252))

        # checking all the squares of the screenshot for being lit up
        for coord in matrix_dict:
            img_coord = (coord[0] - 849, coord[1] - 299)

            if screen.getpixel(img_coord) == (255, 255, 255):
                sequence.append(coord)

        # letting the square disappear before clicking
        time.sleep(SQUARE_FLASH)

        # click all the coordinates of squares in sequence
        for square in sequence:
            pag.click(square)

        # let screen light up after completing sequence
        time.sleep(SCREEN_FLASH)