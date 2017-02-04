#!/usr/bin/python
import urllib2
import cookielib
import re
import zlib

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.dat', ignore_discard=True, ignore_expires=True)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
opener.addheaders = [('Upgrade-Insecure-Requests','1'),('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),('Accept-Encoding','gzip, deflate, sdch'),('Accept-Language','zh-CN,zh;q=0.8'),('Host','jxgl.hdu.edu.cn'),('Referer','http://jxgl.hdu.edu.cn/xs_main.aspx?xh=15058214'),('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36')]
response = opener.open('http://jxgl.hdu.edu.cn/xskbcx.aspx?xh=15058214&xm=%BD%B9%C5%F4%CE%C4&gnmkdm=N121603')
content = response.read()
if response.headers.get("content-encoding") == 'gzip':
    content = zlib.decompress(content, 16+zlib.MAX_WBITS)    
content = content.decode('gbk').encode('utf-8')
classes = re.compile('<td align="center".*?>(.*?)<\/td>').findall(content)
for i in range(len(classes)-1, -1, -1):
    if not '<br>' in classes[i]:
	classes.pop(i)

for item in classes:
    print item.replace('<br>', ' '), "has added in the database"

