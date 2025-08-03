from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# 设置 ChromeDriver 路径
driver_path = "C:\chrome\chromedriver.exe"
service = Service(executable_path=driver_path)

# 设置浏览器选项（可选）
options = Options()
# options.add_argument("--headless")  # 无头模式示例

# 启动浏览器
browser = webdriver.Chrome(service=service, options=options)

url = 'https://baidu.com'
browser.get(url)

import time
time.sleep(5)
# 获取文本框的对象
user_input = browser.find_element(By.ID, 'kw')
#在文本框中输入周杰伦
user_input.send_keys('周杰伦')
time.sleep(2)

#获取百度一下的按钮
button = browser.find_element(By.ID, 'su')
button.click()
time.sleep(2)

#划到底部
js_bottom = 'document.documentElement.scrollTop = 100000'
browser.execute_script(js_bottom)
time.sleep(2)
#获取下一页的数据
next = browser.find_element(By.XPATH,'//*[@id="page"]/div/a[10]')
next.click()
time.sleep(2)
#回到上一页
browser.back()
time.sleep(2)
# 回到下一页
browser.forward()
time.sleep(3)
# 添加等待，防止浏览器自动关闭
input("按回车键关闭浏览器...")  # 等待用户输入
browser.quit()  # 手动关闭浏览器
