#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import time

def info():
    pass

def exp():
    pass

def  poc(str):
    url='http://space.bilibili.com/ajax/member/GetInfo?mid='+str
    head={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://space.bilibili.com/4517888/',
        'Origin': 'http://space.bilibili.com',
        'Host': 'space.bilibili.com',
        'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }

    proxies = {
       "https":"122.242.89.26:45748",
"https":"123.161.239.77:29206",
"https":"182.42.47.201:40949",
"https":"120.42.126.172:45789",
"https":"123.55.69.63:47218",
"https":"60.169.218.47:41934",
"https":"183.52.104.5:39788",
"https":"114.239.1.120:31441",
"https":"222.93.241.7:42831",
"https":"60.167.208.75:40774"
    }

    jscontent = requests.get(url, headers=head, verify=False,proxies=proxies).content
    print jscontent
    jsDict=json.loads(jscontent)
    print jsDict['data']
    if jsDict['status']:
        data=jsDict['data']
        print data['name']



for i in range(4517888,13705128):
    time.sleep(1)
    poc(str(i))