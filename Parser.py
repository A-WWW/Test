import bs4
from bs4 import BeautifulSoup
import requests
import csv
URL='https://electrica-shop.com.ua/c74-rozetki_i_viklyuchateli/filter/494p-1228.m-5/page/2'
HEADERS={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36', 'accept':'*/*'}
def get(url, params=None):
    r=requests.get(url, headers=HEADERS, params=params)
    return r
def parse():
    html=get(URL)
    if html.status_code ==200:
        print('ok we have 200')
        get_cont(html.text)
    else:
        print("что то пошло не так")
def get_cont(html):
    soup = BeautifulSoup(html,'html.parser')
    items=soup.find_all(class_='products-txt-block')
    # print(type(items))
    prod = []
    presence=[]
    for item in items:
        prod.append({'Изделие': item.find(class_='products-name').get_text(strip=True),'Наличие': item.find(class_='products-quantity instock').get_text(strip=True)})
    # print(items)
    # print(prod)
    print(f'Получено {len(prod)} товарных едениц')
    for value in prod:
        print(value)


parse()












