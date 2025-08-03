# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = path
# browser = webdriver.Chrome(options=chrome_options)
#
# url = 'https:www.baidu.com'
# browser.get(url)
#
# browser.save_screenshot('baidu.png')
# 封装的handless
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(options=chrome_options)
    return browser

browser = share_browser()

url = 'https://www.baidu.com'

browser.get(url)

