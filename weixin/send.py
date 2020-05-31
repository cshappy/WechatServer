#-*- coding:utf-8 -*-
#此文件的功能主要是将报警消息发给对应的用户
import tornado.web
import tornado.ioloop
import datetime
import requests
import json
import urllib2
class IndexHandler(tornado.web.RequestHandler):
    def post(self):
        data=json.loads(self.request.body) 
        uid=data["groupid"]
        #获取json里面的数据        
        time=data["Time"]
        SourceID=data["SourceID"]
        SubConditionName=data["SubConditionName"]
        Severity=data["Severity"]
        Message=data["Message"]
        data={"template_id":"ItU6ZWHprgykIZjMOGyCFpuOkbxUaqlT4_0Y4GBFDng","url":"http://www.baidu.com","topcolor":"#FF0000","data":{"first":{"value":"你绑定的设备有报警，请及时处理","color":"#173177"},"keyword1":{"value":"%s"%SourceID,"color":"%23173177"},"keyword2": {"value":"%s"%Message,"color":"%23173177"},"keyword3": {"value":"%s"%SubConditionName,"color":"%23173177"},"keyword4": {"value":"%s"%Severity,"color":"%23173177"},"keyword5": {"value":"%s"%time,"color":"%23173177"},"remark":{"value":"查看报警详情","color":"#173177"}}}
        
        #获取这个公司的所有成员信息
        cursor = c.execute("SELECT * from limit_id where uid='%s'"%uid)
        #sql = """select * from limit_id where uid='%s'"""%(uid)
        try:
            #cursor.execute(sql)
            #results = cursor.fetchall()
            #循环遍历每个成员信息
            for row in cursor:
                #获取成员的openid信息
                openid = row[0]
                data["touser"]=openid
                json_template=json.dumps(data)
                #获取access_token
                with open('app.ini','r') as f:
                    access_token=f.read()
                    f.close()
                url="https://api.weixin.qq.com/cgi-bin/message/template/send?access_token="+access_token
                try:
                    respone=requests.post(url,data=json_template)
                    errcode=respone.json().get("errcode")
                    print("test--",respone.json())
                    fo = open("history.txt", "a")
                    fo.write(str(respone.json())+"\n")
                    fo.close()
                    if(errcode==0):
                        fo = open("history.txt", "a")
                        fo.write("模板发送成功，状态码：",errcode)
                        fo.close()
                        print("模板发送成功，状态码：",errcode)
                    else:
                        fo = open("history.txt", "a")
                        fo.write("模板发送失败，状态码：",errcode)
                        fo.close()
                        print("模板发送失败，状态码：",errcode)
                except Exception as e:
                    print("test++",e)
            self.write(respone.json())
        except:
            print "Error: unable to fecth data"

if __name__ == '__main__':
    #import MySQLdb
    #db = MySQLdb.connect("localhost","root","chenshuai","user",charset='utf8' )
    #cursor = db.cursor()
    import sqlite3
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    app = tornado.web.Application([(r'/',IndexHandler)])
    app.listen(50090)
    tornado.ioloop.IOLoop.current().start()

