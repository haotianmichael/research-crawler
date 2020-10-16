# -*- coding = utf-8 -*-
# @Time: 2020/10/15 7:52 PM
# @Author: haotianmichael
# @File: testbs4.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import re

# 从爬虫的网页中根据标签属性提取有用的信息
file = open("./baidu.html", "rb")
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")  # 通过html.parser解析器解析成为树形结构

# Tag
'''
    标签及其内容，找到所找到的第一个内容
'''
# print(bs.title)
# print(bs.a)
# print(type(bs.head))


# NavigableString
'''
    标签中的内容(字符串)
print(bs.title.string) # 标签本身
print(type(bs.title.string)) # 标签本身
print(bs.a.attrs)  # 标签的所有属性
'''

# BeautifulSoup
'''
    bs表示整个文档
print(type(bs))
print(bs.name)
print(bs.attrs)
print(bs)
'''

# Comment
# print(bs.a.string)
# print(type(bs.a.string))  # 特殊的NavigableString 输出内容不包括注释内容

# ---------------------------------------------应用

# 文档的遍历
'''
    遍历文件树
    将指定的标签内容 以列表的形式返回
'''
# print(bs.head.contents)
# print(bs.head.contents[1])


# 文档的搜索(重要)
'''
# (1) find_all() 字符串过滤:会查找与字符串安全匹配的内容
t_list = bs.find_all("a")   # 将所有a标签内容放到列表中
print(t_list)

'''

# (2) 正则表达式搜索 search()方法匹配内容
# t_list = bs.find_all(re.compile("a"))
# print(t_list)


# (3) 传入一个函数，根据函数要求搜索
# def name_is__exists(tag):
#    return tag.has_attr("name")
# t_list = bs.find_all(name_is__exists)
# print(t_list)
# for item in t_list:  # 格式化输出
#    print(item)


# (4) kwargs  参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)  # class_ 避免关键字
# t_list = bs.find_all(href="http://news.baidu.com")  # class_ 避免关键字
# for item in t_list:
#    print(item)


# (5) text参数
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123", "地图", "贴吧"])
# t_list = bs.find_all(text=re.compile("\d"))  # 应用正则表达式查找包含特定文本的内容(标签中的字符串)
# for item in t_list:
#    print(item)


# (6) limit参数
# t_list = bs.find_all("a", limit=3)
# for item in t_list:
#   print(item)


# (7) css选择器(重要)
# t_list = bs.select('title')   # 通过标签查找
# t_list = bs.select('#u1')   # 通过Id查找
# t_list = bs.select('.mnav')  # 通过类名查找
# t_list = bs.select("a[class='bri']")  # 通过属性查找
# t_list = bs.select("head > title")  # 通过子标签查找
# t_list = bs.select("div > div > div")
# for item in t_list:
#    print(item)


# 正则表达式：字符串模式(判断字符是否符合一定的标准)
# pat = re.compile("AA")   生成正则表达式对象，表示规则
# m = pat.search("ABCAA")
# m = pat.search("ABCAA")
# print(m)
# print(re.findall("[A-Z]+", "ASDaDFAEDAaDV"))


# sub
print(re.sub("a", "A", "abcdcasd"))   # 找到a, 用A替换

# 建议在正则表达式中前面被比较的字符串加上r，不用担心转义字符的问题
