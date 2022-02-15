'''
Author: LetMeFly
Date: 2022-02-02 12:32:03
LastEditors: LetMeFly
LastEditTime: 2022-02-15 21:23:49
'''
from django.shortcuts import render

from Apps.Functions.User import login
from Apps.Functions.User import add1diary
from Apps.Functions.User import getAllDiaries
from Apps.Functions.User import get1diary
from Apps.Functions.User import del1diary


from Apps.Functions.Server import getAccessToken
from Apps.Functions.Server import send1Message
from Apps.Functions.Server import send1Message_DiaryReminder
from Apps.Functions.Server import send1Message_Try
from Apps.Functions.Server import autoCheck2Remind
from Apps.Functions.Server import autoCheck2Remind_Try

# Create your views here.

def html(html_name):
    def main(request):
        return render(request, html_name)
    return main
