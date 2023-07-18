# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}
def get_data(url):
    # response = requests.get(url=url, headers=headers)
    #
    # with open(file='index.html', mode='w', encoding='utf-8') as file:
    #     file.write(response.text)

    with open(file='index.html', encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        table = soup.find('tbody', class_='fr-table-tbody').find_all('tr')  # можно и так table = soup.find("div", {"class": "fr-table-responsive"})
        lst = []
        for tr in table[0:1]:
            name = tr.find_next('td', class_='supplierCell').text.strip()
            site = tr.find_next('span').text.strip()
            link = tr.find_next('a')
            url = link.get('href')
            city = get_city()
            lst.append(name)
            lst.append(site)
            # lst.append(url)
            lst.append(city)
        print(lst)

        with open(file='data.csv', mode='w') as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                    lst
                )
            )

def get_city() -> str:
    # response = requests.get(url=url, headers=headers)
    #
    # with open(file='city.html', mode='w', encoding='utf-8') as file:
    #     file.write(response.text)
    with open(file='suplier.html', encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        city = soup.find_all('div', 'fr-form-group')[1].text
        return city


def main():
    get_data(url='https://www.abcp.ru/suppliers')

if __name__ == '__main__':
    main()