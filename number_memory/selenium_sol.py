from selenium.webdriver.common.by import By
from functions.login import login_to_site

TEST = 'Number Memory'
XPATH_BEGIN = '/html/body/div/div/div[4]/div[1]/div/div/div/div[3]/button'
XPATH_INPUT = '/html/body/div/div/div[4]/div[1]/div/div/div/form/div[2]/input'
XPATH_INPUT_BUTTON = '/html/body/div/div/div[4]/div[1]/div/div/div/form/div[3]/button'
XPATH_NEXT_LEVEL = '/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/button'

debug = True
wanted_level = 50 if debug else int(input('Insert wanted level: '))
link_placement = 3 if debug else int(input('Insert placement of number memory test: '))

if debug:
    from user_data import *

else:
    user = input('Insert benchmark username: ')
    password = input('Insert benchmark password: ')

XPATH_TEST = f'/html/body/div/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[{link_placement + 1}]/td[2]/div/a[1]'

driver = login_to_site(user, password)
driver.implicitly_wait(wanted_level)

test_button = driver.find_element(By.XPATH, XPATH_TEST)
test_button.click()

begin_button = driver.find_element(By.XPATH, XPATH_BEGIN)
begin_button.click()

level = 1
while level < wanted_level:
    number_class_name = 'big-number '
    number = driver.find_element(By.CLASS_NAME, number_class_name).text

    number_input = driver.find_element(By.XPATH, XPATH_INPUT)
    number_input.send_keys(str(number))

    input_button = driver.find_element(By.XPATH, XPATH_INPUT_BUTTON)
    input_button.click()

    next_level = driver.find_element(By.XPATH, XPATH_NEXT_LEVEL)
    next_level.click()

    level += 1