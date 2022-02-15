'''
Author: LetMeFly
Date: 2022-02-03 19:48:13
LastEditors: LetMeFly
LastEditTime: 2022-02-15 23:14:14
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
        JsonResponse - {"code": 状态码}
            0 - 发送成功
            1 - 内容为空
    """
    userid = request.session.get("userid")
    content = json.loads(request.body).get("content", "")
    remindTime = json.loads(request.body).get("remindTime", None)
    if not content:
        return JsonResponse({"code": 1}, safe=False)
    models.diaries.objects.create(userid=userid, content=content, remind_time=remindTime)
    return JsonResponse({"code": 0}, safe=False)


def ORMObject2diaryObject(ORMObject):
    """
    django ORM -> python dict
    将django ORM查询出来的其中一条日记转化为python的字典

    Parameters:
        ORMObject - 单条日记的ORM（~_~不知道这样描述规范不规范）

    Returns:
        diaryObject - python dict
            {
                "content": 日记内容,
                "id": 日记id,
                "publishTime": 发布时间,
                "remindTime": 提醒时间
            }
    """
    diary = {
        "content": ORMObject.content,
        "id": ORMObject.id,
        "publishTime": ORMObject.publish_time,
        "remindTime": ORMObject.remind_time
    }
    return diary


def getAllDiaries(request):
    """
    获取所有日记

    Parameters:
        request - http request
            request.session - 包含登录时保存到小程序Storage中的sessionid，由此来获取用户的userid

    Returns:
        JsonResponse - {"code": 0, "diaries": diaries}
            diaries - [日记1, 日记2, 日记3, ...]
                日记1 - {"content": 日记内容, "id": 日记id, "publishTime": 发布时间, "remindTime": 提醒时间}
    """
    userid = request.session.get("userid")
    result = models.diaries.objects.filter(userid=userid)
    diaries = []
    for this_diary in result:
        diaries.append(ORMObject2diaryObject(this_diary))
    return JsonResponse({"code": 0, "diaries": diaries}, safe=False)


def ifCouldOperateOneDiary(request):
    """
    此http请求是否可以操纵一个日记
    (目前仅有自己的日记才有权限操纵)

    Parameters:
        request - http request
            session - session
            diaryId - 要操纵的日记的id

    Returns:
        code/diary - 状态码/日记ORM
            False - 无权限操纵
            日记ORM - 可以操纵
    """
    userid = request.session.get("userid")
    diary_id = json.loads(request.body).get("diaryId")
    result = models.diaries.objects.filter(userid=userid, id=diary_id)
    return result if len(result) else False


def get1diary(request):
    """
    获取一个日记

    Parameters:
        request - http request
            session - session
            diaryId - 要操作的日记的id

    Returns:
        JsonResponse - http response
            成功 - {"code": 0, "diary": 日记}
                日记 - {"content": 日记内容, "id": 日记id, "publishTime": 发布时间, "remindTime": 提醒时间}
            失败 - {"code": 非0}
                code - 1 没有权限
    """
    result = ifCouldOperateOneDiary(request)
    if not result:
        return JsonResponse({"code": 1}, safe=False)
    return JsonResponse({"code": 1, "diary": ORMObject2diaryObject(result[0])}, safe=False)


def del1diary(request):
    """
    删除一条日记

    Parameters:
        request - http request
            session - session
            diaryId - 要操作的日记的id

    Returns:
        code - 状态码
            0 - 删除成功
            1 - 没有权限或日记不存在
    """
    result = ifCouldOperateOneDiary(request)
    if not result:
        return JsonResponse({"code": 1}, safe=False)
    result[0].delete()
    return JsonResponse({"code": 0}, safe=False)
