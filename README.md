# web-request-lib-notes-

以下为爬虫学习笔记

笔记文件夹以及支持文档来自于‘尚硅谷’ https://www.bilibili.com/video/BV1Db4y1m7Ho?p=86

## **`urllib-vs-requests`**

### 一、基础设计与安装
| **特性**     | **urllib**                                                   | **requests**                                                 |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **安装方式** | Python 内置，无需安装                                        | `pip install requests`                                       |
| **API 设计** | 底层接口复杂，需手动处理编码、请求对象等                     | 高层封装，链式调用，代码简洁                                 |
| **代码示例** | ```python<br>from urllib.request import urlopen<br>response = urlopen("http://example.com")<br>print(response.read().decode())``` | ```python<br>import requests<br>response = requests.get("http://example.com")<br>print(response.text)``` |

---

### 二、GET 请求（带参数）
| **特性**     | **urllib**                                                   | **requests**                                                 |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **参数处理** | 需手动编码并拼接 URL：<br>`parse.urlencode(params)` → `f"{url}?{params}"` | 通过 `params` 字典自动拼接                                   |
| **代码示例** | ```python<br>from urllib import request, parse<br>params = parse.urlencode({"key": "value"})<br>url = f"http://example.com?{params}"<br>response = request.urlopen(url)``` | ```python<br>response = requests.get(<br>    "http://example.com", <br>    params={"key": "value"}<br>)``` |

---

### 三、POST 请求（JSON 数据）
| **特性**      | **urllib**                                                   | **requests**                                                 |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **JSON 支持** | 需手动编码 + 设置请求头：<br>`json.dumps(data).encode()`<br>`headers={"Content-Type": "application/json"}` | 直接通过 `json` 参数传递，自动设置请求头                     |
| **代码示例**  | ```python<br>from urllib import request<br>import json<br>data = json.dumps({"key": "value"}).encode()<br>req = request.Request(<br>    url, data=data,<br>    headers={"Content-Type": "application/json"}<br>)<br>response = request.urlopen(req)``` | ```python<br>response = requests.post(<br>    "http://example.com", <br>    json={"key": "value"}<br>)``` |

### 一、Cookies 管理对比
#### 1. **`requests`：通过 `Session` 自动管理 Cookies**  
```python
import requests

s = requests.Session()
s.post("http://example.com/login", data={"user": "test"})  # 登录并保存 Cookies
response = s.get("http://example.com/dashboard")  # 自动携带 Cookies
```

#### 2. **`urllib`：需手动结合 `http.cookiejar`**

```
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor

jar = CookieJar()
opener = build_opener(HTTPCookieProcessor(jar))
opener.open("http://example.com/login")  # 手动管理 Cookies
```

- **缺点**：代码冗长，需自行处理 Cookie 存

### 二、代理设置对比

#### 1. **`requests`：通过 `proxies` 参数一键设置**

```
proxies = {"http": "http://proxy_ip:port"}
requests.get(url, proxies=proxies)
```

优势：直接传递字典参数，支持 HTTP/HTTPS/SOCKS 代理

#### 2. **`urllib`：需创建 `ProxyHandler` 和 `Opener`**

```
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({"http": "http://proxy_ip:port"})
opener = build_opener(proxy_handler)
opener.open(url)
```

**缺点**：需额外构建处理器和开启器，灵活性低

### 一、Cookies 管理对比
#### 1. **`requests`：通过 `Session` 自动管理 Cookies**  
```python
import requests

s = requests.Session()
s.post("http://example.com/login", data={"user": "test"})  # 登录并保存 Cookies
response = s.get("http://example.com/dashboard")  # 自动携带 Cookies
```

优势：自动处理 Cookie 持久化，无需手动解析

#### 2. **`urllib`：需手动结合 `http.cookiejar`**

```
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor

jar = CookieJar()
opener = build_opener(HTTPCookieProcessor(jar))
opener.open("http://example.com/login")  # 手动管理 Cookies
```

缺点

：代码冗长，需自行处理 Cookie 存储和发送



------

### 二、代理设置对比

#### 1. **`requests`：通过 `proxies` 参数一键设置**

```
proxies = {"http": "http://proxy_ip:port"}
requests.get(url, proxies=proxies)
```

优势：直接传递字典参数，支持 HTTP/HTTPS/SOCKS 代理

#### 2. **`urllib`：需创建 `ProxyHandler` 和 `Opener`**

```
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({"http": "http://proxy_ip:port"})
opener = build_opener(proxy_handler)
opener.open(url)
```

缺点：需额外构建处理器和开启器，灵活性低



------

### 三、异常处理对比

#### 1. **`requests`：细分异常类型**

```
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # 自动检查状态码（非 2xx 抛异常）
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")  # 捕获超时、连接错误等
```

优势：提供等子类异常，调试友好

#### 2. **`urllib`：仅基础异常类**

```
from urllib.error import HTTPError, URLError

try:
    response = urlopen(url)
except HTTPError as e:
    print(f"HTTP错误: {e.code}")  # 仅 HTTP 错误
except URLError as e:
    print(f"URL错误: {e.reason}")  # 网络层错误
```

缺点：异常分类粗糙，需手动检查状态码



------

### 四、性能与适用场景对比

|    **场景**    |          `urllib`          |          `requests`          |         **关键差异说明**          |
| :------------: | :------------------------: | :--------------------------: | :-------------------------------: |
|  **简单请求**  |      ✅ 轻量级，无依赖      |           ❌ 需安装           | `urllib` 无需安装，适合嵌入式环境 |
|  **复杂请求**  |         ❌ 代码冗长         |   ✅ 会话/JSON/代理一键支持   |    `requests` 简化高级功能实现    |
| **大文件下载** | ❌ `urlretrieve` 不支持流式 |   ✅ `stream=True` 分块下载   | `requests` 节省内存，支持断点续传 |
| **高并发需求** |       ❌ 默认关闭连接       | ✅ 连接池复用（`keep-alive`） |   `requests` 减少 TCP 握手开销    |
|  **推荐场景**  |  标准库限制/底层协议开发   |  95% 的爬虫和 API 交互场景   |  优先选 `requests` 提升开发效率   |

------

### 五、总结

> 💡 **核心结论**：
>
> `requests` 优先：开发效率高、功能全面（会话/代理/JSON）、代码可读性强
>
> **`urllib` 仅限**：无法安装第三方库或需深度定制 HTTP 底层逻辑（如嵌入式设备、协议扩展
