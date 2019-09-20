from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

import requests

import os

from time import sleep
from random import randint




def get_proxies():
    req = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all').content
    with open('proxy_list.txt', 'wb') as file:
        file.write(req)


class Driver:
    def __init__(self):
        options = Options()
        options.headless = False

        self.driver_path = os.getcwd() + '/geckodriver'

        # with open('proxy_list.txt') as file:
        #     proxy_list = file.readlines()
        #
        # for proxy in proxy_list:
        #     PROXY = proxy.replace('\n', '')
        #     webdriver.DesiredCapabilities.FIREFOX['proxy']={
        #         "httpProxy":PROXY,
        #         "ftpProxy":PROXY,
        #         "sslProxy":PROXY,
        #         "proxyType":"MANUAL",
        #     }
        #     try:
        #         self.driver = webdriver.Firefox(executable_path=path,options=options)
        #         self.driver.set_page_load_timeout(10)
        #     except:
        #         self.driver.close()





if __name__ == '__main__':
    get_proxies()



# ValuableCandy
# temp123!
