from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.google.com.br/")
time.sleep(3)

barra_pesquisa = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
barra_pesquisa.send_keys("globo esporte")
time.sleep(1)

globo = browser.find_element(By.XPATH, '//*[@id="Alh6id"]/div[1]/div/ul/li[1]/div/div[2]')
globo.click()
time.sleep(5)

segunda_pagina_globo = browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/a/h3')
segunda_pagina_globo.click()
time.sleep(3)





