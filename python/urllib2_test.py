import urllib
import urllib2
###post
''' 
values = {"username " : "1016903103@qq.com","password" : "XXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()

'''

values = {}
values["username"] = "106903103@qq.com"
values["password"] = "XXXX"
data = urllib.urlencode(values)
url = "http://passport.cs dn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
