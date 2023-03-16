fr="auto"
to="auto"
from plyer import notification
import pyperclip
import json, requests
def trans(query):
    url = 'http://fanyi.youdao.com/translate'
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
notification.notify(title = '翻译结果',message = a,)
