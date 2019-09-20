from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

import os

from time import sleep



class Driver:
    def __init__(self):
        options = Options()
        options.headless = False

        path = os.getcwd() + '/geckodriver'

        with open('proxy_list.txt') as file:
            proxy_list = file.readlines()

        for proxy in proxy_list:
            PROXY = proxy.replace('\n', '')
            webdriver.DesiredCapabilities.FIREFOX['proxy']={
                "httpProxy":PROXY,
                "ftpProxy":PROXY,
                "sslProxy":PROXY,
                # "noProxy":None,
                "proxyType":"MANUAL",
                # "autodetect":False
            }
            try:
                driver = webdriver.Firefox(executable_path=path, options=options)
                driver.set_page_load_timeout(10)
                driver.get('https://api.ipify.org')
                print(driver.page_source)
                driver.close()
            except:
                driver.close()


    def test(self):
        self.driver.get('https://api.ipify.org')
        sleep(5)
        self.driver.close()




if __name__ == '__main__':
    Driver()



# ValuableCandy
# temp123!
