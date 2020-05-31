# # -*- coding: utf-8 -*-
#当用户输入image的时候，回应客服消息
import tornado.ioloop
import tornado.web
import time
class MainHandler(tornado.web.RequestHandler):
    def post(self): 
        body = self.request.body
        toUser = body[body.index('<ToUserName>')+21:body.index('</ToUserName>')-3]
        fromUser = body[body.index('<FromUserName>')+23:body.index('</FromUserName>')-3]
        createTime = int(time.time())
        # from与to在返回的时候要交换
        textTpl = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
        <FromUserName><![CDATA[%s]]></FromUserName>
        <CreateTime>%s</CreateTime>
        <MsgType><![CDATA[transfer_customer_service]]></MsgType>
        </xml>"""
        out = textTpl % (fromUser, toUser, createTime)
        self.write(out)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(20080)
    tornado.ioloop.IOLoop.instance().start()