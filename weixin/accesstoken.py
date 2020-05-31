# coding:utf-8
#此文件是获取accesstoken，将各个公众号的accesstoken写入各自的配置文件中
import json
import urllib
import time
import ConfigParser
conf = ConfigParser.SafeConfigParser()
expiresin={}
while True:
    conf.read("accesstoken.ini")
    sectionnames=conf.sections()
    for name in sectionnames:
        if name not in expiresin or expiresin["%s"%name]<time.time():
            appId=conf.get("%s"%name, "appId")
            appSecret=conf.get("%s"%name, "appSecret")
            postUrl = ('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appId, appSecret))
            urlResp = urllib.urlopen(postUrl)
            urlResp = json.loads(urlResp.read())
            accesstoken = urlResp['access_token']
            expiresin["%s"%name]=float(urlResp['expires_in']-100)+time.time()
            with open('%s.ini'%name,'wb+') as f:
                f.write(accesstoken)
                f.close()
    time.sleep(10)
    
