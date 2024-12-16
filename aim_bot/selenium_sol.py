from selenium.webdriver.common.by import By
from functions.login import login_to_site
import pyautogui as pag

# this one is like 30ms faster than scanning for aims

debug = True
aim_amount = 31 if debug else int(input('Insert wanted level: '))
link_placement = 8 if debug else int(input('Insert placement of number memory test: '))

if debug:
    from user_data import *

else:
    user = input('Insert benchmark username: ')
    password = input('Insert benchmark password: ')

XPATH_TEST = f'/html/body/div/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[{link_placement + 1}]/td[2]/div/a[1]'
XPATH_NEXT_LEVEL = '/html/body/div/div/div[4]/div[1]/div/div[1]/div[3]/button'
XPATH_BEGIN = '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]'
XPATH_AIM = '/html/body/div/div/div[4]/div[1]/div/div[1]/div'
SCREEN_X = 150
SCREEN_Y = 200


def get_cords_from_code(code):
    first = code.index('matrix3d')
    cords = eval(code[first + len('matrix3d'): code.index(')', first) + 1])
    return cords


driver = login_to_site(user, password)
driver.implicitly_wait(aim_amount)

test_button = driver.find_element(By.XPATH, XPATH_TEST)
test_button.click()

cur_aim = 0
while cur_aim < aim_amount:
    if cur_aim == 0:
        aim = driver.find_element(By.XPATH, XPATH_BEGIN)

    else:
        aim = driver.find_element(By.XPATH, XPATH_AIM)

    html_code = aim.get_attribute('outerHTML')
    all_cords = get_cords_from_code(html_code)

    aim_cords = (all_cords[-4] + SCREEN_X, all_cords[-3] + SCREEN_Y)
    pag.click(*aim_cords)

    cur_aim += 1