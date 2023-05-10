import requests
from bs4 import BeautifulSoup


def get_html(url):
    """Получаем объект response в виде всей стринцы html"""
    r = requests.get(url)
    return r.text

def get_data(html):
    """
    В этой функции уже работаем с самими даными, которые 
    получили из ф. get_html. и дергаем теги которые нам нужны
    """
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', class_="wp-site-blocks").find('h1').text
    return h1



def main():
    """ф. обработчик через нее вызываем все предыдущие"""
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))









if __name__ == '__main__':
    main()
