from django.shortcuts import render, redirect
from . import models
from django.urls import reverse

def listtwet(request):
    all_tweet = models.Tweet.objects.all()
    tweet_dic = {"tweets" : all_tweet}
    return render(request,"twetterapp/listtwet.html", context=tweet_dic)

def addtwetter(request):
    if request.POST:
        nick_name = request.POST["nickname"]
        message = request.POST["message"]
        models.Tweet.objects.create(nickName = nick_name, messange = message)
        return redirect(reverse("twetterapp:listtwet"))
    else:
        return render(request,"twetterapp/addtwet.html")
