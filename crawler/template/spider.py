# -*- coding = utf-8 -*-
# @Time: 2020/10/15 3:22 PM
# @Author: haotianmichael
# @File: spider.py
# @Software: PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，文字匹配
import urllib.request, urllib.error  # 指定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3

findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBD = re.compile(r'<p class="">(.*?)</p>', re.S)


# 得到指定一个指定URL网页内容
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
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            data.append(re.findall(findLink, item)[0])
            data.append(re.findall(findImgSrc, item)[0])
            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                data.append(titles[0])
                data.append(titles[1].replace("/", ""))
            else:
                data.append(titles[0])
                data.append(' ')
            data.append(re.findall(findRating, item)[0])
            data.append(re.findall(findJudge, item)[0])
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBD, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())
            datalist.append(data)
    return datalist


# 保存数据
def saveDate(datalist, dbpath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('doubanTop250', cell_overwrite_ok=True)
    col = ('link', 'img', 'ctitle', 'etitle', 'rating', 'rating number', 'abstract', 'related')
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条"%i)
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])
    book.save(dbpath)


def initDB(dbpath):
    # 创建数据表
    sql = '''
        create table movie250(
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text
        ) 
    
    '''
    con = sqlite3.connect(dbpath)
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    con.close()


def saveToDB(datalist, dbpath):
    initDB(dbpath)
    con = sqlite3.connect(dbpath)
    cur = con.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250(
                info_link, pic_link,cname, ename, score, rated,introduction,info ) 
                values (%s)
            '''%",".join(data)
        cur.execute(sql)
        con.commit()
    cur.close()
    con.close()


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    # 保存到xls
    # saveDate(datalist, r'douban.xls')

    # 保存到数据库
    saveToDB(datalist, r'movie.db')


if __name__ == "__main__":
    main()
    print("crawler Done!")
