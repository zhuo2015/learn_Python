import urllib.request
import urllib.parse
import json

content = input('输入需要的翻译内容：')

# 通过查看网页元素，得到POST方法需要提交的内容
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'
# Form Data 数据
data = { }
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion']='1.8'
data['keyfrom'] = 'fanyi.web'
data['ue']='UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult']='true'

data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

target=json.loads(html)

print("翻译结果是： %s" % (target['translateResult'][0][0]['tgt']))

