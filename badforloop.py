from bs4 import BeautifulSoup
import requests

with open('testinghtml.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for tr in soup.find_all('tr'):
	words = soup.td.text
	print(words)
	words = soup.td.next_sibling
	print()
