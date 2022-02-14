'''
Author: LetMeFly
Date: 2022-02-02 12:32:03
LastEditors: LetMeFly
LastEditTime: 2022-02-14 16:54:47
'''
from django.shortcuts import render

from Apps.Functions.User import login
from Apps.Functions.User import add1diary
from Apps.Functions.User import getAllDiaries

from Apps.Functions.Server import getAccessToken
from Apps.Functions.Server import sendAMessage

# Create your views here.

def html(html_name):
    def main(request):
        return render(request, html_name)
    return main
