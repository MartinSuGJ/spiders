# -*- coding: utf-8 -*-

# Define your models here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib
import re
import datetime
import sys

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def rph(a,b,c):
    #建立显示进度函数
    per=100.0*a*b/c
    if per>100:
        per=100
    sys.stdout.write('文件大小：%s byte   下载进度：%.2f%% \r'%(c,per))

def checkDownloaded(path):
    return 1 if os.path.getsize(path)>6000 else 0

def getImg(html,path):
    splitReg=r'[\s\"]+'
    tempList=re.split(splitReg,html)
    imgUrls=[]
    x=0
    for str in tempList :
        matchReg=r'http:.*.jpg'
        dateStr=datetime.datetime.now().strftime('%Y-%m-%d ')
        if(re.match(matchReg,str)):
            print '%s--'%x + str
            #print '%s %s.jpg'%(dateStr,x)
            imgUrls.append(str)
            x=x+1
            fileName=path+'%s %s.jpg'%(dateStr,x)
            urllib.urlretrieve(str,fileName,rph)
        matchReg1=r'http:.*.png'
        if re.match(matchReg1,str) :
            print '%s --' %x + str
            #print '%s %s.png'%(dateStr,x)
            imgUrls.append(str)
            x=x+1
            fileName=path+'%s %s.png'%(dateStr,x)
            urllib.urlretrieve(str,fileName,rph)
    return imgUrls
html=getHtml('http://cn.bing.com/images/search?q=%E6%97%A5%E7%B3%BB&qs=n&form=QBIR&pq=%E6%97%A5%E7%B3%BB&sc=8-2&sp=-1&sk=')
getImg(html,'/Users/guangjun/Desktop/Guangjun/Wallpapers/1')
