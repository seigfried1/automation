from bs4 import BeautifulSoup
import requests
import re
import urllib.request

# Requesting the HTML code of the URL.
html = requests.request('get', 'https://en.wikipedia.org/wiki/Ramana_Maharshi')
html.encoding = 'ISO-8859-1' # It makes the HTML source code print nicely

# Providing the HTML sourcecode to bs4 method
soup = BeautifulSoup(html.text, 'html.parser')

# Searching for all images on the page.
imageList = []
contents = soup.find_all('img')

# Saving the image
for num, i in enumerate(contents):
	try:
		urllib.request.urlretrieve('http://' + str(i['src'])[2:], str(num) + '.jpg')
	except:
		pass
