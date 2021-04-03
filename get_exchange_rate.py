# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


def getdata(url):
    r=requests.get(url)
    return r.text

def get_exchange_rate(from_currency, to_currency):
    '''
    From yahoo to get exchange rate informations
    from_currency and to_currency should use upper.
    i.e. USD,CNY,HKD,etc.
    '''
    request_term = from_currency + to_currency
    htmldata = getdata(f"https://finance.yahoo.com/quote/{request_term}=X?ltr=1")
    soup = BeautifulSoup(htmldata, 'html.parser')
    result = soup.find('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).get_text()
    return result