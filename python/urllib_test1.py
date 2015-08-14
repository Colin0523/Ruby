import urllib
import urllib2
###urillib high using 
url = "http://www.server.com/login"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
values = {"username" : "cqc","password" : "xxxx"}
headers = {"User-Agent" : user_agent,"Referer" : "http://www.zhihu.com/articles"}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page  = response.read()
print page 