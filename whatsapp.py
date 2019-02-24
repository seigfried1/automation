from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
time.sleep(10)
search = driver.find_element_by_xpath( "//input[@class='jN-F5 copyable-text selectable-text']")
search.send_keys("Name") # Name of the receipient
search.send_keys(Keys.RETURN)

text_box = driver.find_element_by_xpath("//div[@class='_2S1VP copyable-text selectable-text']")
for x in range(20):
	text_box.send_keys("Message") # Message
	text_box.send_keys(Keys.RETURN)


