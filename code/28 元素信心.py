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
user_input = browser.find_element(By.ID, 'su')
# 获取标签的属性
print(user_input.get_attribute('class'))
# 获取标签的名字
print(user_input.tag_name)
# 获取元素文本
a = browser.find_element(By.LINK_TEXT, '新闻')
print(a.text)
# 添加等待，防止浏览器自动关闭
input("按回车键关闭浏览器...")  # 等待用户输入
browser.quit()  # 手动关闭浏览器
