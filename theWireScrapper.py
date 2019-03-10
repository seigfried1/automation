from selenium import webdriver # need to install chrome webdriver and pip install selenium
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://thewire.in/search?query=rafael")
elem = driver.find_element_by_tag_name("body")
no_of_pagedowns = 20 # change this value to increase or decrease scroll

# Scrolls down the page
while no_of_pagedowns:
	elem.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.2)
	no_of_pagedowns-=1


post_elems = driver.find_elements_by_class_name("card__title")
post_elems_list = []
for post in post_elems:
	post_elems_list.append(post.get_attribute('innerHTML'))


# Some cleaning still needed for hrefs where 'data-reactid' is mentioned
for i in post_elems_list:
	hrefIndex = i.index('href')
	a = i[hrefIndex+5:]
	subString = a[0:a.index('>')]
	# print(subString)
	url = 'https://thewire.in' + subString
	print(url)

driver.quit()