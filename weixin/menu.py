# -*- coding:utf-8 -*-
#此文件是生成微信公众号下面的菜单栏
import urllib
class Menu(object):
    def __init__(self):
        pass
    #创建菜单
    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()
    #获取菜单
    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()
    #删除菜单
    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()
    #获取自定义菜单接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "name": "官网讯息",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "公司简介",
                        "url": "http://www.sealu.net/plus/list.php?tid=44"
                    },
                    {
                        "type": "view",
                        "name": "首页",
                        "url": "http://www.sealu.net/"
                    },
                    {
                        "type": "view",
                        "name": "关于我们",
                        "url": "http://www.sealu.net/plus/list.php?tid=22"
                    }
                ]
            },
            {
                "type": "media_id",
                "name": "联系我们",
                "media_id": "BVHRrY3mTLO8clmPUuOy9eEZ-mxcDCoxZQXHLHDW_A8"
            }
            
        ]
    }
    """
    with open('app.ini','r') as f:
        accessToken=f.read()
    #myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)
