import requests
import time
from win10toast import ToastNotifier

url1 = 'https://api.qtrade.io/v1/currency/HTR'
url2 = 'https://api.kucoin.com/api/v1/prices'

tn = ToastNotifier()


def get_price_qtrade():
    r1 = requests.get(url1).json()
    price_q = (r1['data']['currency']['config']['price'])
    price_qtrade = round(price_q, 3)
    return price_qtrade


def get_price_kucoin():
    r2 = requests.get(url2).json()
    price = r2['data']['HTR']
    price_k = float(price)
    price_kucoin = round(price_k, 3)
    return price_kucoin


def check_price(a, b):
    price_dif = a-b
    if price_dif <= 0.060:
        tn.show_toast('alarm', 'message')
    else:
        pass


while True:
    check_price(get_price_kucoin(), get_price_qtrade())
    time.sleep(20)
