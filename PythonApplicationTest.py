import math    
import base64
import urllib, urllib.request, urllib.parse, urllib.error

import sys
import os

import threading
#import urllib
#from urllib.request import urlopen


'''
def isPrime(n):    
    if n <= 1:    
        return False   
    for i in range(2, int(math.sqrt(n)) + 1):    
        if n % i == 0:      
            return False   
    return True 

primes = []
for tem in range(12+31+1):
    if isPrime(tem):
        primes.append(tem)

result = []
for p in primes:
    if(p>10):
        strTemp = "10月" + str(p-10)
        result.append(strTemp)

for p in primes:
    if(p>11):
        strTemp = "11月" + str(p-11)
        result.append(strTemp)

for p in primes:
    if(p>12):
        strTemp = "12月" + str(p-12)
        result.append(strTemp)

print(result)
'''
#output = os.popen('cat /proc/cpuinfo')

#cmd = 'ping www.baidu.com'

#resultStr = os.popen(cmd).read();

data={base64.b64encode(b"imei"):base64.b64encode(b"868403023453860"),
base64.b64encode(b"mac"):base64.b64encode(b"6a5320db8d"), 
base64.b64encode(b"ro_product_brand") : base64.b64encode(b"HUAWEI"),
base64.b64encode(b"ro_product_model") : base64.b64encode(b"HUAWEI NXT-TL00"), 
base64.b64encode(b"ro_build_fingerprint"):base64.b64encode(b"xx"),
base64.b64encode(b"ro_product_baseversion"):base64.b64encode(b"NXT-TL00C01B368SP01"),
base64.b64encode(b"unlock_sn") : base64.b64encode(b"x1"),
base64.b64encode(b"unlock_product_no") : base64.b64encode(b"x2"),
base64.b64encode(b"hour") : base64.b64encode(b"16"),
base64.b64encode(b"min") : base64.b64encode(b"49"),
base64.b64encode(b"update_md5") : base64.b64encode(b"c6ceb8fc5b5fe74692a5ed34c60587e1")

}
#https://www.xrroot.com:881/param.php
#http://www.xrroot.com:880/rom_apiv1/param.php
#http://www.rdlzz.com/Trade/Hemai.html
#fp = urllib.request.urlopen("https://www.xrroot.com:881/param.php", urllib.parse.urlencode(data).encode("utf8"))
#print(data)
#print("\n\n\n")
#w = urllib.parse.urlencode(data)#.encode("utf8")

#http://www.rdlzz.com/Trade/hemai.asp
#http://www.rdlzz.com/Trade/Ssc/Project-Info-245630.html





#或者
s = 'ab,cde,fgh,ijk'
print(s.split('span'))

urlBase = "http://www.rdlzz.com/Trade/Ssc/Project-Info-"

#file = open("f:\\result.txt" ,"a")

def GetList( name ,range1,addrange):
    for Num in range(range1,range1+addrange):
        urlGet = urlBase + str(Num) + ".html"
        try:
            fp = urllib.request.urlopen(urlGet);
        except Exception as err:
            continue
        fileContent = fp.read()
        strResult = fileContent.decode('gb2312') 
        if (name in strResult):
           pos = strResult.find("发起时间")
           oneResult = strResult[pos:pos+24]
           strWrite = str(Num) + oneResult +"\n"
           file = open("f:\\result.txt" ,"a")
           file.writelines(strWrite)
           file.close()
        fp.close()
    return
       # fileContent.find("发起时间")
name='花絮'
beginNum = 245981
per = 200
threads = []
t1 = threading.Thread(target=GetList,args=(name,beginNum-per,per))
threads.append(t1)
t2 = threading.Thread(target=GetList,args=(name,beginNum-per*2,per))
threads.append(t2)
t3 = threading.Thread(target=GetList,args=(name,beginNum-per*3,per))
threads.append(t3)
t4 = threading.Thread(target=GetList,args=(name,beginNum-per*4,per))
threads.append(t4)
t5 = threading.Thread(target=GetList,args=(name,beginNum-per*5,per))
threads.append(t5)
for t in threads:
    t.setDaemon(True)
    t.start()
t.join()
#243384

GetList("花絮",245405,245636)  

fp = urllib.request.urlopen("http://www.rdlzz.com/Trade/Ssc/Project-Info-245603.html")

#open('d:/data1.txt', 'wb').write(w) 
print("\n\n\n")
mybytes = fp.read()
#mystr = mybytes.decode("utf8") #不需要转utf8

fp.close()

res = base64.b64decode(mybytes)

print(mybytes)
print("\n\n\n\n")
print(res)

open('d:/data.txt', 'wb').write(res) 
