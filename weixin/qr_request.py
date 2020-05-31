# -*- coding: utf-8 -*-
#此文件的操作是生成二维码，当获取到json的时候，生成一个二维码
import tornado.web
import tornado.ioloop
import json
import urllib2
import random
import string
from PIL import Image
class IndexHandler(tornado.web.RequestHandler):
    def post(self):
        body = self.request.body
        body = json.loads(body)
        body["expire_seconds"]=300
        with open('app.ini','r') as f:
            access_token=f.read()
            f.close()
        url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s"%(access_token)
        jsons = json.dumps(body)
        ret = urllib2.Request(url,jsons)
        result_string = urllib2.urlopen(ret).read()
        ticket=json.loads(result_string)['ticket']
        ticket_url="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s"%ticket
        ret=urllib2.urlopen(ticket_url).read()
        self.write(ret)
        self.set_header("Content-type","image/png")
if __name__ == '__main__':
    app = tornado.web.Application([(r'/',IndexHandler)])
    app.listen(40080)
    tornado.ioloop.IOLoop.current().start()
