from selenium.webdriver.common.by import By
from functions.login import login_to_site

debug = True
wanted_level = 50 if debug else int(input('Insert wanted level: '))
link_placement = 8 if debug else int(input('Insert placement of number memory test: '))

if debug:
    from user_data import *

else:
    user = input('Insert benchmark username: ')
    password = input('Insert benchmark password: ')

XPATH_TEST = f'/html/body/div/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[{link_placement + 1}]/td[2]/div/a[1]'
XPATH_BEGIN = '/html/body/div/div/div[4]/div[1]/div/div[1]/div[2]/button'
XPATH_NEXT_LEVEL = '/html/body/div/div/div[4]/div[1]/div/div[1]/div[3]/button'
TILE_CLASS_NAME = 'css-19b5rdt'

driver = login_to_site(user, password)
driver.implicitly_wait(wanted_level)

test_button = driver.find_element(By.XPATH, XPATH_TEST)
test_button.click()

begin_button = driver.find_element(By.XPATH, XPATH_BEGIN)
begin_button.click()

level = 1
while level < wanted_level:
    numbered_tiles = sorted(driver.find_elements(By.CLASS_NAME, TILE_CLASS_NAME), key=lambda item: int(item.text))

    for tile in numbered_tiles:
        tile.click()

    next_button = driver.find_element(By.XPATH, XPATH_NEXT_LEVEL)
    next_button.click()

    level += 1