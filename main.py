# -*- coding: utf-8 -*-

import requests
from loguru import logger as log
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}
def get_data(url):
    # response = requests.get(url=url, headers=headers)
    #
    # with open(file='index.html', mode='w', encoding='utf-8') as file:
    #     file.write(response.text)
    try:
        with open(file='index.html', encoding='utf-8') as file:
            src = file.read()
            soup = BeautifulSoup(src, 'lxml')
            table = soup.find('tbody', class_='fr-table-tbody').find_all('tr')  # можно и так table = soup.find("div", {"class": "fr-table-responsive"})
            data = []
            for tr in table:
                lst = []
                name = tr.find_next('td', class_='supplierCell').text.strip()
                site = 'https://' + tr.find_next('span').text.strip()
                url = tr.find_next('a').get('href')
                city = get_city(url)
                lst.append(name)
                lst.append(site)
                # data.append(url)
                lst.append(city)
                data.append(lst)
            make_dataframe(data)
    except Exception as ex:
        log.info(f'Возникла ошибка в процессе перебора поставщиков. {ex}')

def get_city(url) -> str:
    response = requests.get(url=url, headers=headers)
    #
    # with open(file='city.html', mode='w', encoding='utf-8') as file:
    #     file.write(response.text)
    try:
        soup = BeautifulSoup(response.text, 'lxml')
        city = soup.find_all('div', 'fr-form-group')[1].text
        return city
    except Exception as ex:
        log.info(f'Возникла ошибка в процессе получения города поставщика. {ex}')

def make_dataframe(data):
    try:
        # log.info(data)
        df = pd.DataFrame(data, columns=['Поставщик', 'Сайт', 'Город'])
        log.info(df)
        save_dataframe(df)
    except Exception as ex:
        log.info(f'Мне не удалось создать датафрейм. {ex}')

def save_dataframe(df):
    try:
        df.to_excel('mydata.xlsx', index=False)
    except Exception as ex:
        log.info(f'Мне не удалось сохранить данные. {ex}')


def main():
    get_data(url='https://www.abcp.ru/suppliers')

if __name__ == '__main__':
    main()