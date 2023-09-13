from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://saucedemo.com/")

#find_element()
username = browser.find_element(By.ID,"user-name")
password = browser.find_element(By.ID,"password")

#send_keys
username.send_keys("standard_user")
password.send_keys("secret_sauce")

variavel_va = browser.find_elements(By.XPATH, '//*[@class= "form_input"]')
print(variavel_va)
print(len(variavel_va))

time.sleep(5)

submit = browser.find_element(By.XPATH, '//*[@id="user-name"]')
submit.click()

time.sleep(5)

browser.quit()