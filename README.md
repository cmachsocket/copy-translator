# copy-translator
linux划词翻译软件,使用系统通知发送翻译结果
灵感来源:[CopTrans](https://github.com/maxuewei2/CopyTrans/)

依赖项:pyperclip,plyer

安装依赖:

```
pip install pyperclip plyer
```
将trans.py,拷贝到你的电脑上

添加你的系统快捷键,命令如下:

```
 python 你的.py文件路径
```

采用有道api翻译

修改trans.py文件,第一行为从什么语言翻译,第二行为翻译成什么语言(自动填写auto)

支持语言如下:
[网易支持列表](https://ai.youdao.com/DOCSIRMA/html/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E7%BF%BB%E8%AF%91/API%E6%96%87%E6%A1%A3/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1-API%E6%96%87%E6%A1%A3.html#section-9)

使用:将要翻译的文本复制到剪贴板,然后按设定的快捷键翻译

优点:几乎不占系统资源,而且不用一直运行

缺点:要按两次
