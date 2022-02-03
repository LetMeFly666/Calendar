'''
Author: LetMeFly
Date: 2022-02-03 19:48:13
LastEditors: LetMeFly
LastEditTime: 2022-02-03 23:37:34
'''
import Secrets
import requests
import json
from Apps import models
from django.http import JsonResponse



def login(request):
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
    userid = request.session.get("userid")
    content = json.loads(request.body).get("content")
    models.diaries.objects.create(userid=userid, content=content)
    return JsonResponse({"code": 0}, safe=False)


def GetAllDiaries(request):
    userid = request.session.get("userid")
    result = models.diaries.objects.filter(userid=userid)
    diaries = []
    for this_diary in result:
        diaries.append(this_diary.content)
    return JsonResponse({"code": 0, "diaries": diaries}, safe=False)
