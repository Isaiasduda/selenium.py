from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(browser, 30)

browser.maximize_window()

browser.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

dropdown_productos = Select( browser.find_element(By.XPATH, '//select[@id="first"]'))#importar a biblioteca select 
dropdown_productos.select_by_visible_text("Google")#texto visivel da pagina
time.sleep(2)

animals = Select(browser.find_element(By.XPATH,'//select[@id="animals"]'))
animals.select_by_value("avatar")
time.sleep(2)
animals.select_by_index(2)
time.sleep(2)

dropdown_food = Select(browser.find_element(By.XPATH,'/html/body/div/div/div/div/div[2]/div[2]/p/select'))
dropdown_food.select_by_value("pizza")
time.sleep(2)
dropdown_food.select_by_visible_text("Burger")
time.sleep(2)
                       

                 