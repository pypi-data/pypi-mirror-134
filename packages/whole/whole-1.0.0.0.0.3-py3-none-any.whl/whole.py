#coding:utf-8
#!/usr/bin/python3
import os   #操作系统接口模块
import time #时间的访问和转换
import urllib.request   #用于打开 URL 的可扩展库
import zipfile  #ZIP模块
import sqlite3  #SQLite 数据库

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

if os.name=="nt":
    sq3 = sqlite3.connect("C:\\Users\\sh\\Desktop\\stock.db")   #连接sqlite   Windows
else:
    sq3 = sqlite3.connect("stock.db")   #连接sqlite   Linux
c = sq3.cursor()
def StockData():    #获取股票数据
    PipList = os.popen("pip list").read()
    #if im.find('not found') != -1:
        #os.system('sudo apt-get install -y python3-pip')    #Ubuntu安装pip
    if PipList.find('xlrd')==-1 or PipList.find('beautifulsoup4')==-1 or PipList.find('baostock')==-1 :
        os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U pip')#临时使用国内镜像升级pip
        os.system('pip install xlrd beautifulsoup4 baostock -i https://pypi.tuna.tsinghua.edu.cn/simple')#自动安装包
    from bs4 import BeautifulSoup   #解析html
    import xlrd #xls文件解析
    import baostock as bs   #证券宝www.baostock.com

    print("开始获取股票代码："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #c.execute('drop table code')    #删除表格
    c.execute("CREATE TABLE IF NOT EXISTS code (id INTEGER PRIMARY KEY,code TEXT,name TEXT,minimum TEXT)")   #判断表格不存在，创建“股票代码”表格
    #下载文件
    html1 = urllib.request.urlopen('http://47.97.204.47/syl/',timeout=3000).read()
    html2 = BeautifulSoup(html1,'html.parser').find_all('a')[-2].get('href') #解析数据//结果：csi20211221.zip
    urllib.request.urlretrieve("http://47.97.204.47/syl/"+html2, html2)  #下载股票代码
    fff = zipfile.ZipFile(html2,"r")
    for fff1 in fff.namelist():  #获取ZIP文档内所有文件的列表名称
        fff.extract(fff1,os.getcwd())   #解压
    fff.close()
    os.remove(html2) #删除文件
    trading_time = html2.replace('.zip','').replace('csi','')	#获取股票交易时间//结果：20211221
    #解析xls文件
    file3 = xlrd.open_workbook("csi"+trading_time+".xls",encoding_override="gb2312")    #打开文件，文件路径
    sheet1 = file3.sheet_by_name('个股数据')   #通过sheet名称获得sheet对象
    sh_sz = ["sh."+i if i[0]=='6' else "sz."+i for i in sheet1.col_values(0)]    #sh或sz
    stock_obtain = list(zip( sh_sz, sheet1.col_values(1)))#获取第1，2列内容转换列表
    del stock_obtain[0]
    c.execute("delete from code") #清空数据库表格
    sq3.commit()
    c.executemany("INSERT INTO code (code,name) VALUES (?,?)",stock_obtain)  #股票代码写入数据库
    sq3.commit()
    os.remove("csi"+trading_time+".xls") #删除文件
    print("获取股票代码成功："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    print("开始获取股票数据："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    stock_data_1 = []   #获取股票数据列表
    c.execute("SELECT code FROM code") #选择股票表格
    stock_code_1 = c.fetchall()  #获取股票表格所有记录
    #stock_code_1.extend([('sh.000001',),('sz.399001',),('sz.399006',)])
    li = len(stock_code_1)
    n = 0
    bs.login() #登陆系统   lg = bs.login() #登陆系统???
    for stock_code_2 in stock_code_1:                                  # id                   日期       开盘价   最高价    最低价   收盘价     前收盘价         涨跌幅%     dr
        c.execute("CREATE TABLE IF NOT EXISTS ["+ stock_code_2[0] +"] (id INTEGER PRIMARY KEY,date TEXT,preclose TEXT,open TEXT,high TEXT,low TEXT,close TEXT,pctChg TEXT,dr TEXT)")   #判断表格不存在，创建股票代码表格
        n+=1
        print(stock_code_2[0]+"   总数："+str(li)+"   当前数："+str(n)+"   剩余："+str(li-n))
        c.execute("SELECT date FROM ["+ stock_code_2[0] +"] ORDER BY id DESC LIMIT 1")    #最后更新日期
        lud = c.fetchone()   #最后更新日期
        last_update_date = "1990-12-18" if lud==None else lud[0]   #判断最后更新日期为空1990-12-18
        last_update_date_1 = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.strptime(last_update_date,'%Y-%m-%d'))+86400))  #最后更新日期加一天
        if float(time.mktime(time.strptime(last_update_date_1,"%Y-%m-%d")))<=float(time.mktime(time.strptime(trading_time,"%Y%m%d"))):
            #股票数据
            rs=bs.query_history_k_data_plus(stock_code_2[0],"date,preclose,open,high,low,close,pctChg",start_date=last_update_date_1, end_date="",frequency="d", adjustflag="3")
            while (rs.error_code == '0') & rs.next():
                stock_data_1.append(tuple(rs.get_row_data()))
            c.executemany("INSERT INTO ["+ stock_code_2[0] +"] (date,preclose,open,high,low,close,pctChg) VALUES (?,?,?,?,?,?,?)",stock_data_1)  #数据写入数据库
            sq3.commit()
            stock_data_1.clear()   #清空列表stock_data_1
            #股票除夕除权
            last_update_years=time.strptime(last_update_date,'%Y-%m-%d').tm_year #最后更新年份
            while last_update_years <= time.localtime(time.time()).tm_year:
                rs_dividend=bs.query_dividend_data(code=stock_code_2[0],year=last_update_years,yearType="report")
                while (rs_dividend.error_code=='0') & rs_dividend.next():
                    s1 = rs_dividend.get_row_data()
                    if s1[8] != "":
                        c.execute("UPDATE ["+ stock_code_2[0] +"] SET dr=? WHERE date=?",("DR",s1[6]))
                        sq3.commit()
                last_update_years+=1
    bs.logout() #登出系统
    print("获取股票数据成功："+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))    #获取股票数据