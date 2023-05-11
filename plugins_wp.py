import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    'Спарсили текст всей страницы'
    r = requests.get(url)
    return r.text


def refined(s: str):
    '''Очистили строку от ненужных символов, путем вычленения срезом
    и привели цифры в один формат без запятых'''
    # rating-count

    rating_new = s.split(' ')[0]
    rating_new = rating_new.replace(',', '')
    return rating_new


def write_scv(data):
    '''создаем файл, с префиксом "а" - добавлять в конец нужные элементы, 
    а не перезаписывать их'''
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'], 
                         data['url'],
                         data['reviews']))      


def get_data(html):
    'вычленяем нужную информацию и создаем словарь для будущего файла'
    soup = BeautifulSoup(html, 'lxml')
    featur = soup.find_all('section')[1]
    plugins = featur.find_all('article')  # find_all return list

    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')
        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(r)

        data = {'name': name, 
                'url': url,
                'reviews': rating}

        write_scv(data)      


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
