'''
Author: LetMeFly
Date: 2022-02-02 12:32:03
LastEditors: LetMeFly
LastEditTime: 2022-02-03 22:42:16
'''
from django.shortcuts import render
from Apps.Functions.User import login
from Apps.Functions.User import add1diary
from Apps.Functions.User import GetAllDiaries

# Create your views here.

def html(html_name):
    def main(request):
        return render(request, html_name)
    return main
