from bs4 import BeautifulSoup
import json
from models.position import Position

def handlePosition(html):
    document = BeautifulSoup(html,'html5lib')
    table = document.find('table', attrs={'class': 'oa_table4'})
    trs = table.tbody.find_all('tr')

    for tr in trs:
        model = []

        for td in tr.find_all('td'):
            model.append(td.text)

        if len(model) > 0:
            position = Position(model[1], model[2], model[3], model[4], model[5], model[6], model[7], model[8], model[9])
            print(position.show())

def handleProject(html):
    document = BeautifulSoup(html,'html5lib')
    table = document.find('table', attrs={'class': 'oa_table4'})
    trs = table.tbody.find_all('tr')

    for tr in trs:
        model = []

        for td in tr.find_all('td'):
            model.append(td.text)

        if len(model) > 0:
            position = Position(model[1], model[2], model[3], model[4], model[5], model[6], model[7], model[8], model[9])
            print(position.show())

# file = open('index.html', 'r')

# document = BeautifulSoup(file.read(), 'html5lib')
# table = document.find('table', attrs={'class': 'oa_table4'})
# trs = table.tbody.find_all('tr')

# for tr in trs:
#     model = []

#     for td in tr.find_all('td'):
#         model.append(td.text)

#     if len(model) > 0:
#         position = Position(model[1], model[2], model[3], model[4], model[5], model[6], model[7], model[8], model[9])
#         print(position.show())