from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.implicitly_wait(12)# espera ate 12 segundos 
browser.maximize_window()



browser.get("https://chercher.tech/practice/implicit-wait-example")
checkbox = browser.find_element(By.XPATH,  '//*[@id="q"]/input[1]')
time.sleep(5)
assert checkbox.is_displayed()
print('checkbox realizado com sucesso.')
