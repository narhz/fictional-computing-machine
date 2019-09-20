from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

import requests

from guerrillamail import GuerrillaMailSession

import os

from time import sleep
from random import randint
from secrets import token_urlsafe

from constants import Urls, Paths, Elements




URLS = Urls()
PATHS = Paths()
ELEMENTS = Elements()



def get_proxies():
    print('Getting proxy list...\n')
    req = requests.get(URLS.PROXIES).content
    with open('proxy_list.txt', 'wb') as file:
        file.write(req)

    with open('proxy_list.txt', 'r') as file:
        proxy_addrs = file.readlines()

    print('Done.')


    return proxy_addrs



def test_proxies():
    proxy_addrs = get_proxies()

    count = 0
    active_proxies = []
    while count != 10:
        proxy = proxy_addrs[randint(0, len(proxy_addrs))].replace('\n', '')

        try:
            req = requests.get(URLS.IP_CHECK, proxies = {'http': proxy, 'https': proxy}, timeout=5).text
            active_proxies.append(proxy)
            count += 1
        except:
            pass

    return active_proxies



def gen_account_creds():
    session = GuerrillaMailSession()

    account = {
        'email': session.get_session_state()['email_address'],
        'pass': token_urlsafe(16)
    }

    return account

    # print(session.get_session_state()['email_address'])
    # for email_id in session.get_email_list():
    #     print(session.get_email(email_id.guid).subject)
    #     print(session.get_email(email_id.guid).body)



def create_account():
    options = Options()
    options.headless = False

    proxy_addrs = test_proxies()

    for proxy in proxy_addrs:
        webdriver.DesiredCapabilitis.getcwd() + '/geckodriver'es.FIREFOX['proxy']={
            "httpProxy":proxy,
            "ftpProxy":proxy,
            "sslProxy":proxy,
            "proxyType":"MANUAL",
        }

        driver = webdriver.Firefox(executable_path=PATHS.DRIVER_PATH, options=options)
        # driver.set_page_load_timeout(10)
        driver.get(URLS.REGESTER)
        sleep(5)
        driver.close()



# class Driver:
#     def __init__(self):
#
#
#
#             try:
#                 driver.get('https://old.reddit.com')
#
#                 sign_up = driver.find_element_by_xpath('//*[@id="header-bottom-right"]/span[1]/a[2]')
#                 driver.click(sign_up)
#
#
#
#                 sleep(10)
#                 driver.close()
#             except:
#                 driver.close()





if __name__ == '__main__':
    print(gen_account()



# ValuableCandy
# temp123!
