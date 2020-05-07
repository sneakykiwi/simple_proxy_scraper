import requests
from bs4 import BeautifulSoup
import os


class ProxyScraper:
    def __init__(self):
        self.proxies = []
        self.body = None

    def get_source(self):
        page = requests.get('https://free-proxy-list.net/')
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table', attrs={'id': 'proxylisttable'})
        self.body = table.find('tbody')

    def get_proxies(self):
        for row in self.body.find_all('tr'):
            cols = row.find_all('td')[:7]
            self.proxies.append({
                'ip': cols[0].text,
                'port': cols[1].text,
                'iso': cols[2].text,
                'country': cols[3].text,
                'protocol': 'https' if cols[6].text == 'yes' else 'http',
                'alive': True})

    def save_proxies(self):
        with open("proxies.txt", "w+") as file:
            [file.write(f"{p['ip']}:{p['port']}\n") for p in self.proxies]
            os.startfile('proxies.txt')

    def scrape(self):
        self.get_source()
        self.get_proxies()
        self.save_proxies()


scraper = ProxyScraper()

scraper.scrape()
