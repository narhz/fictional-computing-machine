from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

import requests
from bs4 import BeautifulSoup as bs

from guerrillamail import GuerrillaMailSession

import os

import json
from time import sleep
from random import randint, choice
from secrets import token_urlsafe

from constants import Urls, Paths, Elements




URLS = Urls()
PATHS = Paths()
ELEMENTS = Elements()



def get_proxies():
    print('Getting proxy list...')
    req = requests.get(URLS.PROXIES).content
    with open('proxy_list.txt', 'wb') as file:
        file.write(req)

    with open('proxy_list.txt', 'r') as file:
        proxy_addrs = file.readlines()

    print('Done.')
    print('Finding active proxies')


    return proxy_addrs



def test_proxies():
    proxy_addrs = get_proxies()

    count = 0
    active_proxies = []
    while count != 2:
        proxy = proxy_addrs[randint(0, len(proxy_addrs))].replace('\n', '')

        try:
            req = requests.get(URLS.IP_CHECK, proxies = {'http': proxy, 'https': proxy}, timeout=5).text
            active_proxies.append(proxy)
            count += 1
            print(f'found {count} active')
        except:
            pass

    return active_proxies



def gen_account_creds():
    session = GuerrillaMailSession()
    with open('short_words.json', 'r') as file:
        words = json.load()

    user_name_opts = {
        'camel_case': choice(words) + choice(words).title(),
        'camel_case_num': choice(words) + choice(words).title + str(randint(0, 5000),
        'flat_num': choice(words) + str(randint(0, 50000)),
        'upper': choice(words).upper() + str(randint(0, 50000)),
        'upper_lower': choice(words).upper + choice(words)
    }

    account = {
        'email': session.get_session_state()['email_address'],
        'pass': token_urlsafe(16),
        'user': user_name_opts[choice(list(user_name_opts.keys()))]
    }

    return account



def create_account():
    options = Options()
    options.headless = False

    proxy_addrs = test_proxies()

    for proxy in proxy_addrs:
        webdriver.DesiredCapabilities.FIREFOX['proxy']={
            "httpProxy":proxy,
            "ftpProxy":proxy,
            "sslProxy":proxy,
            "proxyType":"MANUAL",
        }

        account = gen_account_creds()

        driver = webdriver.Firefox(executable_path=PATHS.DRIVER_PATH, options=options)
        driver.set_page_load_timeout(40)
        try:
            driver.get(URLS.REGESTER)

            email = driver.find_element_by_xpath(ELEMENTS.EMAIL_FIELD)
            email.send_keys(account['email'])
            email.send_keys(Keys.RETURN)

            user_name = driver.find_element_by_xpath(ELEMENTS.USER_FIELD)
            user_name.send_keys(account['user'])

            pass_field = driver.find_element_by_xpath(ELEMENTS.PASS_FIELD)
            pass_field.send_keys(account['pass'])

            sleep(5)
            driver.close()
        except:
            driver.close()
            pass



if __name__ == '__main__':
    pass


# /html/body/div[1]/div/div[2]/div/form/div[3]/div[2]/div[2]/div/div/a[1]
# /html/body/div[1]/div/div[2]/div/form/div[3]/div[2]/div[2]/div/div/a[1]
