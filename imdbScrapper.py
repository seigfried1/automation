import urllib3
from bs4 import BeautifulSoup
import requests
import xlwt

year = '1995'

url = "https://www.imdb.com/search/title?release_date="+ year + "," + year + "&title_type=feature"
sourceCode = requests.get(url).text
soup = BeautifulSoup(sourceCode, "lxml")

title = soup.find('title').text

# listerList = soup.find_all('div', attrs={'class':'lister-list'})

listerItem = soup.find_all('h3', attrs={'class':'lister-item-header'})

for i in listerItem:
	print(i.span.text)
	print(i.a.text)
	print(i.find('span', attrs={'class':'lister-item-year'}).text)


# Writing in a Text File
with open('imdbText.txt', 'w') as f:
	for i in listerItem:
		f.write(i.span.text)
		f.write(i.a.text)
		f.write(i.find('span', attrs={'class':'lister-item-year'}).text)
		f.write('\n')



# Writing in an Excel Workbook
wb = xlwt.Workbook()
ws = wb.add_sheet('Movie List')
ws.write(0, 0, 'No') # Row, Col, Content
ws.write(0, 1, 'Title')
ws.write(0, 2, 'Year')

with open('imdbText.txt', 'w') as f:
	for num, i in enumerate(listerItem):
		ws.write(num+1, 0, i.span.text)
		ws.write(num+1, 1, i.a.text)
		ws.write(num+1, 2, i.find('span', attrs={'class':'lister-item-year'}).text)

wb.save('MovieList.xls')
