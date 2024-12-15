import pyautogui as pag
import keyboard
import time

REG_X_START = 600
REG_Y_START = 240
REG_X_END = 800
REG_Y_END = 400

REGION = (
    REG_X_START,
    REG_Y_START,
    REG_X_END,
    REG_Y_END
)

# NOTE: at lvl 94 the matrix becomes rectangular
# and i dont care enough to fix it
def determine_square(image):
    # going to check one row to determine side of square
    y = 5

    # square size and square coordinates
    count = 0
    cords = []

    # color of the background
    blank_color = (43, 135, 209)

    # determining blank / square
    cur_color = False

    for x in range(image.width):
        # check if color matches square color
        clr = image.getpixel((x, y))

        if clr != blank_color:
            # update counter and coordinates if we transfer from blank to square
            if not cur_color:
                count += 1
                cords.append((x, y))

            # always set current color to true
            cur_color = True

        else:
            # set to false otherwise
            cur_color = False

    # return side of square, distance between two squares and coordinates of first square
    return count, cords[1][0] - cords[0][0], cords[0]


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
        screen = pag.screenshot(region=REGION)
        side, gap, first_square = determine_square(screen)

        # create array of the selected squares
        to_click = []

        # determine selected squares
        for column in range(side):
            for row in range(side):
                cur_square_x = first_square[0] + gap * row
                cur_square_y = first_square[1] + gap * column

                cur_square = (cur_square_x, cur_square_y)

                if screen.getpixel(cur_square) == (255, 255, 255):
                    to_click.append((cur_square_x + REG_X_START, cur_square_y + REG_Y_START))

        # letting squares flash away
        time.sleep(1.75)

        # click selected squares
        for choice in to_click:
            pag.click(*choice)

        # letting screen flash away
        time.sleep(1.75)
