import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.pravda.com.ua/rus/news/'




def new(link):
    r = requests.get(link)
    soup = bs(r.text, 'lxml')
    news = soup.find_all('div', class_='article_header')
    x = [c.text for c in news]
    del x[0]
    return x


new_ua = new(url)


def new_description(link):
    r = requests.get(link)
    soup = bs(r.text, 'lxml')
    news = soup.find_all('div', class_='article_header')
    a = [x.find('a').get('href') for x in news]
    link = 'https://www.pravda.com.ua/'
    lst = []
    for i in a:
        if i.find('https') < 0:
            lst.append(link + i)
        else:
            lst.append(i)
    return lst
