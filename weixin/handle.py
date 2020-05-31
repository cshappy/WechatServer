# -*- coding: utf-8 -*-
#根据用户的操作，跳转相应的url
import requests
import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def post(self):
        body = self.request.body
        msgtype=body[body.index('<MsgType>')+18:body.index('</MsgType>')-3]+"/"
        url="http://internal2.sealu.net/%s"%(msgtype)
        if msgtype=="event/":
            event=body[body.index('<Event>')+16:body.index('</Event>')-3]+"/"
            url="http://internal2.sealu.net/event_%s"%(event)
        try:
            respone=requests.post(url,data=body,timeout=1)
        except requests.exceptions.RequestException as e:
            print(e)
        self.write(respone.text)


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(60080)
    tornado.ioloop.IOLoop.instance().start()