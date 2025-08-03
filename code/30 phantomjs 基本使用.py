from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# 设置 ChromeDriver 路径
driver_path = "C:\chrome\phantomjs.exe"
service = Service(driver_path)
browser = webdriver.PhantomJS(service=service)

url = 'https://baidu.com'
browser.get(url)
