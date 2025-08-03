import urllib.request

#下载一个网页
# url_page = 'https://www.baidu.com/'
# urllib.request.urlretrieve(url_page,'baidu.html')
#下载图片
# url_img = 'https://pic1.zhimg.com/v2-7a9a56edc251673a09b26250c5542338_b.jpg'
# urllib.request.urlretrieve(url_img, 'test.jpg')
#下载视频
url_video = 'http://files.youth.cn/video/zq_video/202507/P020250710362552897402.mp4'
urllib.request.urlretrieve(url_video, '央视.mp4')