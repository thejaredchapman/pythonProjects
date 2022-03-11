from bs4 import BeautifulSoup
import requests as rq 

url = "https://www.imdb.com/chart/boxoffice/"
f=open('boxoffice.txt', 'w')

r=rq.get(url)
data_list = []
new_item = []
soup =BeautifulSoup(r.content, 'html.parser')
for item in soup.findAll('', {'chart-boxoffice': 'chartTableColumnTitle'}):
	new_item.append(item.get('content'))
data_list.append(new_item)

new_item=[]
for item in soup.findAll('', {'chart-boxoffice': 'chartTableGross'}):
	new_item.append(item.get('content'))
data_list.append(new_item)

new_item=[]
for item in soup.findAll('', {'chart-boxoffice': 'chartTableGross'}):
	new_item.append(item.get('content'))
data_list.append(new_item)

new_item=[]
for item in soup.findAll('', {'chart-boxoffice': 'chartTableWeeks'}):
	new_item.append(item.get('content'))
data_list.append(new_item)

f.write('(0:60) (1:25) (2:10)\n\n'.format("Movie Title", "Weekend Gross", "Total Gross", "Weeks Since Release") 
	for i in range(len(data_list[0]):
		f.write(('(0:60) (1:25) (2:10)\n'.format(data_list[0][i]),
	data_list[1][i], data_list[2][i]))
f.close
