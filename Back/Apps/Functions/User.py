'''
Author: LetMeFly
Date: 2022-02-03 19:48:13
LastEditors: LetMeFly
LastEditTime: 2022-02-14 22:35:59
'''
import Secrets
import requests
import json
from Apps import models
from django.http import JsonResponse



def login(request):
    """
    登录函数，实现微信小程序的登陆功能
    函数根据登陆请求中的code向微信服务器索要用户openid和session_key
        openid - 每个用户独一无二，唯一不变，用来唯一标识每个用户
        session_key - 用来“数据签名校验”、“数据加密解密”等，会过期(但此次登陆结束之前不会过期)

    Parameters:
        request - http request
            request.GET - {"code": (wx.login -> msg) msg.code}
    
    Returns:
        JsonResponse - {"code": 0}
    """
    code = request.GET.get("code")
    response = requests.get(f"https://api.weixin.qq.com/sns/jscode2session?appid={Secrets.APP_ID}&secret={Secrets.APP_SECRET}&js_code={code}&grant_type=authorization_code")
    data = response.json()
    session_key = data['session_key']
    openid = data['openid']
    # result = models.user.objects.filter(userid=openid)
    # if not result:  # 第一次注册
    #     models.user.objects.update_or_create()
    models.user.objects.update_or_create(defaults={"userid": openid, "session_key": session_key}, userid=openid)
    request.session['userid'] = openid
    return JsonResponse({"code": 0}, safe=False)


def add1diary(request):
    """
    添加一个日记

    Parameters:
        request - http request
            request.session - 包含登录时保存到小程序Storage中的sessionid，由此来获取用户的userid
            json.loads(request.body) - {"content": 要添加的日记的内容}

    Returns:
        JsonResponse - {"code": 0}
    """
    userid = request.session.get("userid")
    content = json.loads(request.body).get("content")
    models.diaries.objects.create(userid=userid, content=content)
    return JsonResponse({"code": 0}, safe=False)


def getAllDiaries(request):
    """
    获取所有日记

    Parameters:
        request - http request
            request.session - 包含登录时保存到小程序Storage中的sessionid，由此来获取用户的userid

    Returns:
        JsonResponse - {"code": 0, "diaries": diaries}
            diaries - [日记1, 日记2, 日记3, ...]
                日记1 - {"content": 日记内容, "id": 日记id}
    """
    userid = request.session.get("userid")
    result = models.diaries.objects.filter(userid=userid)
    diaries = []
    for this_diary in result:
        diaries.append({
            "content": this_diary.content,
            "id": this_diary.id
        })
    return JsonResponse({"code": 0, "diaries": diaries}, safe=False)
