import os
import pyperclip
import json, requests
f=open("trans_config.ini")
def trans(query):
    url = 'http://fanyi.youdao.com/translate'
    fr=f.readline()
    to=f.readline()
    data = {
        "i": query,  # 待翻译的字符串
        "from": fr,
        "to": to,
        "doctype": "json"
    }
    res = requests.post(url, data=data).json()
    return res['translateResult'][0][0]['tgt']

txt = pyperclip.paste()
a=trans(txt)
os.popen("notify-send "+"翻译结果 "+a)