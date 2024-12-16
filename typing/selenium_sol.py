from selenium.webdriver.common.by import By
from functions.login import login_to_site

debug = True
link_placement = 2 if debug else int(input('Insert placement of number memory test: '))

if debug:
    from user_data import *

else:
    user = input('Insert benchmark username: ')
    password = input('Insert benchmark password: ')

XPATH_TEST = f'/html/body/div/div/div[4]/div/div/div[2]/div[2]/div/table[1]/tbody/tr[{link_placement + 1}]/td[2]/div/a[1]'
XPATH_NEXT_LEVEL = '/html/body/div/div/div[4]/div[1]/div/div[1]/div[3]/button'
XPATH_BEGIN = '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]'
XPATH_INPUT = '//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div'

driver = login_to_site(user, password)
driver.implicitly_wait(1)

test_button = driver.find_element(By.XPATH, XPATH_TEST)
test_button.click()

letters = driver.find_elements(By.CLASS_NAME, 'incomplete')
text = ''

for letter in letters:
    symbol = letter.text
    text += symbol or ' '

input_field = driver.find_element(By.XPATH, XPATH_INPUT)
input_field.send_keys(text)