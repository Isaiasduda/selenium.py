from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as CE 

browser = webdriver.Chrome()

browser.maximize_window()



browser.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

wait = WebDriverWait(browser, 30)


browser.find_element(By.ID,"alert").click()
wait.until(CE.alert_is_present())
time.sleep(2)

browser.find_element(By.ID,"populate-text").click()
wait.until(CE.text_to_be_present_in_element((By.XPATH ,'//*[@id="h2"]'),"Selenium Webdriver"))
time.sleep(2)

browser.find_element(By.XPATH,'//*[@id="display-other-button"]').click()
wait.until(CE.element_to_be_clickable((By.XPATH,'//*[@id="hidden"]')))  
time.sleep(2)