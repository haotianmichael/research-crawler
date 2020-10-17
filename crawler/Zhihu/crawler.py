# -*- coding = utf-8 -*-
# @Time: 2020/10/17 9:28 AM
# @Author: haotianmichael
# @File: crawler.py
# @Software: PyCharm


from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


findStar = re.compile("")   # Star number Q got
findComment = re.compile(" ")   # Comment number Q got
findTitle = re.compile("")    # each topic's name when tapped key words
findTitleLink = re.compile("")   # each topic's link, for further crawler


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.75 Safari/537.36 "
    }
    req = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        elif hasattr(e, "reason"):
            print(e.reason)
    return html


def initDB(dbpath):
    sql = '''
        create table zhihu(
            star numeric,
            comment numeric,
            title text,
            titleLink text
        ) 
    
    '''
    con = sqlite3.connect(dbpath)
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()


def getData(baseurl):
    datalist = []
    for i in range(1, 1):
        url =
        return ""


def saveToDB(datalist, dbpath):
    initDB(dbpath)
    con = sqlite3.connect(dbpath)
    cur = con.cursor()

    for data in datalist:
        for index in range(len(data)):


def main():
    baseurl = "https://www.zhihu.com/search?type=content&q=%E7%BC%96%E8%AF%91%E5%99%A8"
    datalist = getData(baseurl)
    saveToDB(datalist)


if __name__ == "__main__":
    main()
    print("crawler Done!")
