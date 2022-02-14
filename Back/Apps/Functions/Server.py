'''
Author: LetMeFly
Date: 2022-02-14 15:47:47
LastEditors: LetMeFly
LastEditTime: 2022-02-14 16:13:06
'''
import requests
import Secrets


def getAccessToken(reqeust="Temp For url调用"):
    """
    获取小程序全局唯一后台接口调用凭据（access_token）

    Returns:
        json - 调用结果
            正常调用 - {"access_token": "ACCESS_TOKEN", "expires_in": 7200} (过期时间当前为2h，后期可能会有所调整)
            系统繁忙 - {"errcode": 40001, "errmsg": ...}
    """
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={Secrets.APP_ID}&secret={Secrets.APP_SECRET}'

    response = requests.get(url)
    print(response.json())

