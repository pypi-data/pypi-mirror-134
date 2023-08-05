# Eitaa Pykit
Toolkit for [Eitaa](https://eitaa.com/) messenger.

[![Pypi](https://img.shields.io/pypi/v/eitaa-pykit)](https://pypi.org/project/Eitaa-PyKit)
[![Downloads](https://img.shields.io/pypi/dm/eitaa-pykit)](https://pypi.org/project/Eitaa-PyKit)

## Install via pip
Windows:
```
pip install eitaapykit
```
Linux:
```
pip3 install eitaapykit
```

## Get information of a channel
you can get information of a channel with `get_info(channel_id)` function in `eitaa` module \
params :
- ***channel_id***: your channel id to get information of it(without `@`)

Example :
```py
import eitaa
print(eitaa.get_info("channel ID"))
```
It is returns a `dict` object contains channel name, image url, subscribers count, channel description.
```json
{
  "name": "channel name",
  "image_url": "channel image url",
  "users" : "subscribers count",
  "desc" : "description of channel",
}
```

## Send a message
you can send a meesage to your channel\group with `send_message(token,chat_id,text,pin=False,view_delete=-1)` function in `eitaa` moduel \
params :
- ***token*** : your [eitaayar.ir](https://eitaayar.ir) token
- ***chat_id*** : your chat id(if your chat is a channel set it to channel id, and if your chat is a group set it to your group's invite link)
- ***text*** : text to send
- ***pin***(optional) : if you want to message pinned in chat, set it `True`
- ***view_delete***(optional) : if view counts be equal to `view_delete`, message will delete

Example :
```py
import eitaa
TOKEN = "eitaayar.ir_token"
print(eitaa.send_message(TOKEN,"chat id","message text",pin=1)
```
It is returns a bool value that shows send status

- `True` : message sent successfully
- `False` : error in send message

## Send a file
you can send a file to your channel with `send_file(token,chat_id,caption,file,pin=False,view_delete=-1)` function in `eitaa` moduel \
params :
- ***token*** : your [eitaayar.ir](https://eitaayar.ir) token
- ***chat_id*** : your chat id(if your chat is a channel set it to channel id, and if your chat is a group set it to group invite link)
- ***caption*** : caption of your file(similar to `text` in `send_message` function)
- ***file*** : your file name to send to chat
- ***pin***(optional) : if you want to file pinned in chat, set it `True`
- ***view_delete***(optional) : if view counts be equal to `view_delete`, file will delete

Example :
```py
import eitaa
TOKEN = "eitaayar.ir_token"
print(eitaa.send_file(TOKEN,"chat id","caption","README.txt",pin=1)
```
It is returns a bool value that shows send status
`True` --> file sent successfully
`False` --> error in send message

## Todo
More options with selenium.

## About
This project is licensed under the **MIT** License, for more information read [License](LICENSE)
