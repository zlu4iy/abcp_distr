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
        table = soup.find("div", {"class": "fr-table-responsive"})
        data_tr = table.find('tbody').find_all('tr')
        table_data = ['Таблица']
        for dth in data_tr:
            dth = dth.text.strip()
            # print(dth)
            table_data.append(dth)
        with open(file='data.csv', mode='w') as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                    table_data
                )
            )


def main():
    get_data(url='https://www.abcp.ru/suppliers')

if __name__ == '__main__':
    main()