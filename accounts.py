from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

import requests

from guerrillamail import GuerrillaMailSession

import os

from time import sleep
from random import randint




def get_proxies():
    print('Getting proxy list...\n')
    req = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all').content
    with open('proxy_list.txt', 'wb') as file:
        file.write(req)

    with open('proxy_list.txt', 'r') as file:
        proxy_addrs = file.readlines()

    print('Done.')


    return proxy_addrs


def gen_email():
    session = GuerrillaMailSession()
    print(session.get_session_state()['email_address'])
    for email_id in session.get_email_list():
        print(session.get_email(email_id.guid).subject)
        print(session.get_email(email_id.guid).body)


def test_proxies():
    proxy_addrs = get_proxies()

    count = 0
    active_proxies = []
    while count != 10:
        proxy = proxy_addrs[randint(0, len(proxy_addrs))].replace('\n', '')

        try:
            req = requests.get('https://api.ipify.org', proxies = {'http': proxy, 'https': proxy}, timeout=5).text
            active_proxies.append(proxy)
            count += 1
        except:
            pass

    return active_proxies




class Driver:
    def __init__(self):
        options = Options()
        options.headless = False

        self.driver_path = os.getcwd() + '/geckodriver'

        proxy_addrs = test_proxies()

        for proxy in proxy_addrs:
            PROXY = proxy.replace('\n', '')
            webdriver.DesiredCapabilities.FIREFOX['proxy']={
                "httpProxy":PROXY,
                "ftpProxy":PROXY,
                "sslProxy":PROXY,
                "proxyType":"MANUAL",
            }

            driver = webdriver.Firefox(executable_path=self.driver_path, options=options)
            driver.set_page_load_timeout(10)
            try:
                driver.get('https://old.reddit.com')

                sign_up = driver.find_element_by_xpath('//*[@id="header-bottom-right"]/span[1]/a[2]')
                driver.click(sign_up)



                sleep(10)
                driver.close()
            except:
                driver.close()





if __name__ == '__main__':
    print(test_proxies())



# ValuableCandy
# temp123!
