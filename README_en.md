# copy-translator
A application which is translator of text uses system notifications to send the translation result.
The inspiration:[CopTrans](https://github.com/maxuewei2/CopyTrans/)

Depends:pyperclip,plyer

The command to install depends:

```
pip install pyperclip plyer
```

Then add your system shortcuts.Here is the command:

```
 python "your file path"
```

Youdao api is used to translate.

Edit the file trans.py . The first line is the language you translate from,the first line is the language you translate to.(or "auto")

Here is languages it supports:
[网易支持列表](https://ai.youdao.com/DOCSIRMA/html/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E7%BF%BB%E8%AF%91/API%E6%96%87%E6%A1%A3/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E6%9C%8D%E5%8A%A1-API%E6%96%87%E6%A1%A3.html#section-9)

Usege:copy the text you will translate,then click your shortcut that is set.

Advantage:little system source is used,and don't have to have been run.

Disadvantage:you have to click twice.

I just want to practice my writting.Sorry for my poor English.
