from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://google.com")

browser.maximize_window()
time.sleep(5)

browser.refresh_window()#refresh_window atualiza a pagina 
time.sleep(5)


browser.forward()
time.sleep(5)

browser.get

time.sleep(5)