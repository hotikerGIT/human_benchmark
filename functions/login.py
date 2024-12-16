from selenium.webdriver.common.by import By
from selenium import webdriver

def login_to_site(username, passwd):
    driver = webdriver.Firefox()

    driver.get('https://humanbenchmark.com/login')

    user_field = driver.find_element(By.NAME, 'username')
    passwd_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.XPATH, '/html/body/div/div/div[4]/div/div/form/p[3]/input')

    user_field.send_keys(username)
    passwd_field.send_keys(passwd)
    login_button.click()

    return driver