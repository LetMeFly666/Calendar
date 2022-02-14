'''
Author: LetMeFly
Date: 2022-02-14 15:47:47
LastEditors: LetMeFly
LastEditTime: 2022-02-14 16:47:58
'''
import requests
import Secrets


def getAccessToken():
    """
    获取小程序全局唯一后台接口调用凭据（access_token）

    Returns:
        json - 调用结果
            正常调用 - {"access_token": "ACCESS_TOKEN", "expires_in": 7200} (过期时间当前为2h，后期可能会有所调整)
            系统繁忙 - {"errcode": 40001, "errmsg": ...}
    """
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={Secrets.APP_ID}&secret={Secrets.APP_SECRET}'

    response = requests.get(url)
    data = response.json()
    
    # 此处做了简化处理，暂不考虑微信后台更改过期时间
    return data["access_token"]


def sendAMessage0(userid, date, content, jumpto="MyDairies"):  # FIXME: 名字改回来
    """
    发送一次消息提醒
    Parameters:
        userid - 用户的openid
        content - 消息内容 （微信要求20字以内，若超过将会被截取为{{前17个字}...}）
        jumpto - 用户点击消息卡片所跳转到的页面，默认我“我的日记页面”

    Returns:
        0 - 发送成功
        1 - 用户拒绝接受消息
    """
    url = f"https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token={getAccessToken()}"

    data = {
        "touser": userid,
        "template_id": Secrets.TEMPLATE_ID,
        "page": jumpto,
        "data": {
            "date4": {  # 日程时间
                "value": date
            },
            "thing2": {  # 提醒内容
                content if len(content) <= 20 else content[:17] + "..."
            },
            "thing11": {  # 备注
                "value": "你所设定的提醒到时间了呢"
            }
        }
    }

    response = requests.post(url, data=data)
    print(response.json())
    return response.json()


def sendAMessage(reqeust="Temp For url调用"):
    sendAMessage0()
    from django.http import HttpResponse
    return HttpResponse("ok")
