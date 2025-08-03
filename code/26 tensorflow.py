from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 设置 ChromeDriver 路径
driver_path = "C:\chrome\chromedriver.exe"# 替换为你的实际路径
service = Service(executable_path=driver_path)

# 设置浏览器选项（可选）
options = Options()
# options.add_argument("--headless")  # 无头模式示例

# 启动浏览器
browser = webdriver.Chrome(service=service, options=options)

# 访问网站
url = 'https://jd.com'
browser.get(url)

# 获取页面源码
content = browser.page_source
print(content)

input("按回车键关闭浏览器...")
browser.quit()
