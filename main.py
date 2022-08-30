import urllib.request
import chromedriver_binary
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)

    top_raw = urllib.request.urlopen('https://nipponcolors.com/')
    top_soup = BeautifulSoup(top_raw.read(), 'html.parser')
    series_selector = top_soup.find(id='colors')
    series_list = series_selector.find_all('a')
    colors = []
    for i in range(len(series_list)):
        co = series_list[i]
        co_name = co.text.split(' ')[-1]
        driver.get('https://nipponcolors.com/#' + co_name)
        time.sleep(5)
        html = driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        co_selector = soup.find(id='bgWrap').get('style')
        colors.append({u'name': co_name, u'code': co_selector.split(
            ': ')[1].split(';')[0], u'id': f'{(i+1):03}'})
        print(co_name)
    print(colors)
    driver.quit()
