from django.shortcuts import render
import models

def listtwet(request):
    all_tweet = models.Tweet.objects.all()
    tweet_dic = {"tweet" : all_tweet}
    return render(request,"twetterapp/listtwet.html", context=tweet_dic)

def addtwetter(request):
    return render(request,"twetterapp/addtwet.html")
