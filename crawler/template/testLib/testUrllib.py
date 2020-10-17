# -*- coding = utf-8 -*-
# @Time: 2020/10/15 6:51 PM
# @Author: haotianmichael
# @File: testUrllib.py
# @Software: PyCharm

import urllib.request
import urllib.parse


'''
获取get请求
response = urllib.request.urlopen("http://www.baidu.com")  # 将访问网页的数据返回成为一个对象
print(response)
print(response.read().decode('utf-8'))  # 将网页源码解码  按照正常格式输出
'''


'''
获取一个Post请求
    但是必须按照post的方式封装数据， parse

data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
reponse = urllib.request.urlopen("http://httpbin.org/post", data= data)
print(reponse.read().decode('utf-8'))
'''

'''
超时处理
    当网页发现IP Agent为爬虫时，会做一些防御  
try:
    reponse = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
    print(reponse.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out!")
'''


'''
    status = 200 状态码    
    status = 418  就是对方服务器发现你是爬虫hhh
    reponse = urllib.request.urlopen("http://douban.com")
    print(reponse.status)
'''



'''
    将数据进行封装
    爬虫伪装成为一个浏览器
    头部信息
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}
# url = "https://www.douban.com"
    data = bytes(urllib.parse.urlencode({'name':'eric'}), encoding="utf-8")
    req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
    reponse = urllib.request.urlopen(req)
    print(reponse.read().decode('utf-8'))
'''


headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}
url = "http://httpbin.org"
req = urllib.request.Request(url=url,headers=headers)
reponse = urllib.request.urlopen(req)
print(reponse.read().decode('utf-8'))




