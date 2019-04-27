import urllib
import requests
import time
import random
import hashlib
import json

def begin():
    #有道翻译地址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    #请求头
    headers = {
        'Cookie':'OUTFOX_SEARCH_USER_ID=-1394029542@60.170.26.43; OUTFOX_SEARCH_USER_ID_NCOO=263982759.7499639; _ga=GA1.2.1250288161.1552366488; JSESSIONID=aaajMmlKuyU6M-0bs6EPw; ___rl__test__cookies=1556379480295',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
    }
    #输入翻译内容
    key = input("请输入要翻译的内容：")
    #salt盐加密
    salt = int(time.time()*1000 + random.randint(0,10))
    salt_str = str(salt)
    #ts = salt/10
    ts_str = str(salt/10)
    #sign签名MD5加密
    S = "fanyideskweb"
    D = "@6f#X3=cCuncYssPsuRUE"
    sign_str = S + key + salt_str + D
    sign_md5_str = hashlib.md5(sign_str.encode('utf-8')).hexdigest()
    #bv为app版本信息加密
    app_version = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    bv_str = hashlib.md5(app_version.encode(encoding='UTF-8')).hexdigest()
    #请求体
    data = {
        'i':key,
        'form':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt_str,
        'sign':sign_md5_str,
        'ts':ts_str,
        'bv':bv_str,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME',
    }
    #数据编码
    data = urllib.parse.urlencode(data).encode()
    #构造请求对象并返回信息
    request = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(request).read().decode()
    #将字符串转换为python字典，筛选所需信息并输出
    target = json.loads(response)
    result = target['translateResult'][0][0]['tgt']
    print(result)

if __name__ == '__main__':
    while True:
        begin()
