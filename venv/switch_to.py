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

browser.get("https://chercher.tech/practice/frames")

iframe1 = browser.find_element(By.XPATH, '//*[@id="frame1"]')
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH,'//input[@type="text"]').send_keys("iframe")
time.sleep(3)

iframe3 = browser.find_element(By.XPATH, '//iframe[@id="frame3"]')
browser.switch_to.frame(iframe3)
box = browser.find_element(By.XPATH, '//input[@id= "a"]').click()
time.sleep(3)

browser.switch_to.default_content()

iframe2= browser.find_element(By.XPATH, '//iframe[@id="frame2"]')
browser.switch_to.frame(iframe2)
caixa = Select(browser.find_element(By.XPATH, '//select[@id="animals"]'))
caixa.select_by_visible_text("Avatar")
time.sleep(3)