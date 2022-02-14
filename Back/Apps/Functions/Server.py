'''
Author: LetMeFly
Date: 2022-02-14 15:47:47
LastEditors: LetMeFly
LastEditTime: 2022-02-14 21:04:28
'''
import requests
import json
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


def send1Message(toWho, templateId, data: dict, jumpto=""):
    """
    推送一次消息给用户

    Parameters:
        toWho - 用户的openid
        templateId - 模板的template_id
        data - 要替换的模板中的内容
            {"date4": {"value": "2022-02-14 16:58"}, "thing1": {"value": "..."}, ...}

    Returns:
        code - 状态码
            0 - 发送成功
            1 - 用户拒收（用户撤销了订阅 或 用户未订阅）
            2 - 不合法的用户openid
            -1 - 其他错误
    """
    url = f"https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token={getAccessToken()}"
    send_data = {
        "touser": toWho,
        "template_id": templateId,
        "data": data
    }
    if jumpto:
        send_data["page"] = jumpto
    response = requests.post(url, data=json.dumps(send_data))  # 直接传递dict类型的数据会导致微信服务器解析失败
    response_data = response.json()
    print(response_data)  # FIXME: 取消打印
    errorCode2myCode = {
        "0": 0,
        "43101": 1,
        "40003": 2
    }
    code = errorCode2myCode.get(str(response_data["errcode"]), -1)
    return code



def send1Message_DiaryReminder(toWho, date, content, jumpto="MyDairies"):
    """
    推送一次用户设置的提醒给用户

    Parameters:
        toWho - 用户的openid
        date - 提醒时间
        content - 消息内容 （微信要求20字以内，若超过将会被截取为{{前17个字}...}）
        jumpto - 用户点击消息卡片所跳转到的页面，默认我“我的日记页面”

    Returns:
        code - 状态码
            0 - 发送成功
            1 - 用户拒收（用户撤销了订阅 或 用户未订阅）
            2 - 不合法的用户openid
            -1 - 其他错误
    """

    data = {
        "date4": {  # 日程时间
            "value": date
        },
        "thing2": {  # 提醒内容
            "value": content if len(content) <= 20 else content[:17] + "..."
        },
        "thing11": {  # 备注
            "value": "你所设定的提醒到时间了呢"
        }
    }

    code = send1Message(toWho=toWho, templateId=Secrets.TEMPLATE_ID_DIARY_REMINDER, data=data, jumpto=jumpto)
    return code


def send1Message_Try(reqeust="Temp For url调用"):
    """
    发送消息测试函数
    """
    code = send1Message_DiaryReminder(toWho=Secrets.USERID_LetMeFly, date="2022-02-14 16:58", content="第一个提醒设置")
    from django.http import HttpResponse
    return HttpResponse("Success!" if code == 0 else "Failed")

