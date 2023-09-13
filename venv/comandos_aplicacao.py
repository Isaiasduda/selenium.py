from selenium import webdriver


browser = webdriver.Chrome()

browser.get("https://saucedemo.com/")
#title 
print("o titulo da pagina : ", browser.title)

#current_url
print("A URL da pagina : ", browser.current_url)

#page_source
print("o codigo fonte da pagina : ", browser.page_source)


