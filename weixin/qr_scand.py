# -*- coding: utf-8 -*-
#当用户扫描二维码的时候，post数据到指定的url
import tornado.ioloop
import tornado.web
import requests
import sqlite3
import time
class MainHandler(tornado.web.RequestHandler):
    def post(self): 
        body = self.request.body
        #url=body[body.index('<EventKey>')+19:body.index('</EventKey>')-3]
        #respone=requests.post(url,data=body)
        #self.write(respone.text)
        print body
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        uid=body[body.index('<EventKey>')+19:body.index('</EventKey>')-3]
        openid=body[body.index('<FromUserName>')+23:body.index('</FromUserName>')-3]
        print uid,openid
        toUser = body[body.index('<ToUserName>')+21:body.index('</ToUserName>')-3]
        fromUser = body[body.index('<FromUserName>')+23:body.index('</FromUserName>')-3]
        createTime = int(time.time())
        sql="SELECT * from limit_id where openid='%s' and uid='%s'"%(openid,uid)
        cursor = c.execute(sql)
        print sql
        length=int(len(list(cursor)))
        if length==0:
            # from与to在返回的时候要交换
            c.execute("insert into limit_id values('%s','%s')"%(openid,uid));
            conn.commit()
            conn.close()
            textTpl = """<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[绑定成功]]></Content>
            </xml>"""
            out = textTpl % (fromUser, toUser, createTime)

            self.write(out)
        elif length==1:
            conn.close()
            # from与to在返回的时候要交换
            textTpl = """<xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[已经绑定过该设备]]></Content>
            </xml>"""
            out = textTpl % (fromUser, toUser, createTime)

            self.write(out)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(10080)
    tornado.ioloop.IOLoop.instance().start()
