import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('moda.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['brand'],
                         data['old_price'],
                         data['sale_price']))


def change_price(price):
    p = price.split(' ')[:-1]
    price = ' '.join(p)
    return price


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    descriptions = soup.find_all('div', class_="x-product-card-description")
    for description in descriptions:
        try:
            brand = description.find('div', class_="x-product-card-description__brand-name").text.strip()
        except:
            brand = ''

        try:
            old_price = description.find('span', class_="x-product-card-description__price-old").text.strip()
        except:
            old_price1 = description.find('span', class_="x-product-card-description__price-single").text.strip()
            old_price = change_price(old_price1)

        try:
            sale_price1 = description.find('span', class_="x-product-card-description__price-new").text.strip()
            sale_price = change_price(sale_price1)
        except:
            sale_price = ''

        data = {'brand': brand,
                'old_price': old_price,
                'sale_price': sale_price}

        write_csv(data)


def main():
    'Пример реализации парсинга пагинацией'
    # first exempl
    pattern = 'https://www.lamoda.ru/c/3044/clothes-pidzhaki-i-zhaketi/?page={}'
    for i in range(1, 3):
        url = pattern.format(str(i))
        get_page_data(get_html(url))

    # second exempl
    # url = 'some_link'
    # while True:
    #     get_page_data(get_html(url))
    #     soup = BeautifulSoup(get_html(url), 'lxml')
        
    #     try:
    #         pattern = 'Next' # import re
    #         url = 'some_link' + soup.find('ul', class_='paginat').find('a', 
    #         text=re.compile(pattern)).get('href') # find botton and add to link
    #     except:
    #         break


if __name__ == '__main__':
    main()
