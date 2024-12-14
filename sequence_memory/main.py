import keyboard
import time
import pyautogui as pag

# this one is tougher so comments are here

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

running = True
work = False
while running:
    if keyboard.is_pressed('shift'):
        running = False

    if keyboard.is_pressed('ctrl'):
        work = True

    if keyboard.is_pressed('alt'):
        work = False
        sequence = []

    if work:
        # skipping previous steps as we memorized them already
        for i in range(len(sequence)):
            '''
            this is the most important parameter
            the more exact it is, the better the score will be
            
            if it is way too long, the programme wont capture the new square
            if it is way too short, the programme will repeat the previous square
            
            this parameter is based off on tests, not calculations.
            '''
            time.sleep(0.5)

        # screening the last square, which is new
        screen = pag.screenshot('screen.png', region=(849, 299, 252, 252))

        # checking all the squares of the screenshot for being lit up
        for coord in matrix_dict:
            img_coord = (coord[0] - 849, coord[1] - 299)

            if screen.getpixel(img_coord) == (255, 255, 255):
                sequence.append(coord)

        # letting the square disappear before clicking
        time.sleep(0.5)

        # click all the coordinates of squares in sequence
        for square in sequence:
            pag.click(square)

        # let screen light up after completing sequence
        time.sleep(1.2)