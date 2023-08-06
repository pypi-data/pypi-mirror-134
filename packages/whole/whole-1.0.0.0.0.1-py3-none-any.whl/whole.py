#coding:utf-8
#!/usr/bin/python3
import os   #操作系统接口模块
import time #时间的访问和转换
import urllib.request   #用于打开 URL 的可扩展库
import zipfile  #ZIP模块
import sqlite3  #SQLite 数据库


def __init__():
    i=os.popen("pip list").read()
    print(i)
    #if im.find('not found') != -1:
        #os.system('sudo apt-get install -y python3-pip')    #Ubuntu安装pip

    if i.find('xlrd') == -1 or i.find('baostock') == -1 or i.find('beautifulsoup4') == -1:
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pip')#临时使用国内镜像升级pip
        os.system('pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple')#设置默认使用国内镜像,pip版本需要大于或等于10.0.0
        #os.system('pip install beautifulsoup4 xlrd baostock')#自动安装包
        os.system('pip install beautifulsoup4 xlrd')#自动安装包

from bs4 import BeautifulSoup   #解析html
import xlrd #xls文件解析
#import baostock as bs   #证券宝www.baostock.com


def m(a):   #列表求平均值
    b=0
    for c in a:
        b+=float(c)
    return b/len(a)

def t(a='%Y-%m-%d %H:%M:%S',b=0,c=0,d=0,e='+'): #输出时间格式,输入时间，输入时间格式，时间秒（加减时间），+或-（默认+）
    if b==0:
        return time.strftime(a,time.localtime())    #当前时间
    else:
        try:
            z=time.strptime(b,c)
            if e=='+':
                y=time.mktime(z)+d
            elif e=='-':
                y=time.mktime(z)-d
            else:
                return '第5个参数请输入+或-'
            return time.strftime(a, time.localtime(y))
        except:
            return "输入时间格式错误"