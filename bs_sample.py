import requests
from bs4 import BeautifulSoup

pagetoparse = requests.get('https://www.worldometers.info/coronavirus/')

soup = BeautifulSoup(pagetoparse.text, 'lxml')

cases = soup.find_all('div', class_ = 'maincounter-number')
list = []
for case in cases:
    list.append(case.get_text())

for n in range(len(list)):
    list[n] = list[n].strip()

print(f'Coronavirus Cases: {list[0]}'  '\n' f'Deaths: {list[1]}' '\n' f'Recovered: {list[2]}')