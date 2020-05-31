# -*- coding: utf-8 -*-
import urllib2
import json
import poster.encode
from poster.streaminghttp import register_openers

class Material(object):
    def __init__(self):
        register_openers()

    #获取素材列表
    def batch_get(self, accessToken, mediaType, offset=0, count=20):
        url = ("https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s" % accessToken)
        data = ("{ \"type\": \"%s\", \"offset\": %d, \"count\": %d }" % (mediaType, offset, count))
        urlResp = urllib2.urlopen(url, data)
        print urlResp.read()

if __name__ == '__main__':
    myMaterial = Material()
    with open('app.ini','r') as f:
        accessToken=f.read()
        f.close()
    mediaType = "news"
    myMaterial.batch_get(accessToken, mediaType)
