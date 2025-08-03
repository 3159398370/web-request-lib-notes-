from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# 设置 ChromeDriver 路径
driver_path = "C:\chrome\chromedriver.exe"# 替换为你的实际路径
service = Service(executable_path=driver_path)

# 设置浏览器选项（可选）
options = Options()
# options.add_argument("--headless")  # 无头模式示例

# 启动浏览器
browser = webdriver.Chrome(service=service, options=options)

url = 'https://baidu.com'
browser.get(url)

#元素定位
# 新代码（正确）
#根据 id 属性来获取对象
# button = browser.find_element(By.ID, "su")
# print(button)

# 根据标签属性的属性值来获取对象的
# button = browser.find_element(By.NAME, "wd")
# print(button)

# button = browser.find_elements(By.XPATH,'//*[@id="su"]')
# print(button)
# 根据标签名来获取对象
# button = browser.find_element(By.TAG_NAME, "input")
# print(button)
# 使用 bs4 的语法来获取对象
# button = browser.find_element(By.CSS_SELECTOR, "#su")
# print(button)
# 根据链接文本来获取对象
button = browser.find_element(By.LINK_TEXT, "新闻")
print(button)
# 添加等待，防止浏览器自动关闭
input("按回车键关闭浏览器...")  # 等待用户输入
browser.quit()  # 手动关闭浏览器

