from os import getcwd




class Urls:
    def __init__(self):
        self.OLD_REDDIT = 'https://old.reddit.com'
        self.PROXIES = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all'
        self.IP_CHECK = 'https://api.ipify.org'
        self.REGESTER = 'https://www.reddit.com/register/'


class Paths:
    def __init__(self):
        self.DRIVER_PATH = getcwd() + '/geckodriver'


class Elements:
    pass
