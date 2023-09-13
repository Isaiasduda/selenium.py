from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.saucedemo.com/")

username = browser.find_element(By.ID, "username")
password = browser.find_element(By.ID, "password")
botao_login = browser.find_element(By.ID, "login-button")

#send_keys
username.send_keys("standard_user")
password.send_keys("secret_sauce")
time.sleep(2)
botao_login.click()
time.sleep(3)

#text 
segunda_tela_produtos = browser.find_element(By.XPATH, '//*[@class="product_label"]')

print(segunda_tela_produtos.text)
assert segunda_tela_produtos.text =="$0"
time.sleep(5)