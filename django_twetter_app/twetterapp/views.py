from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

def listtwet(request):
    all_tweet = models.Tweet.objects.all()
    tweet_dic = {"tweets" : all_tweet}
    return render(request,"twetterapp/listtwet.html", context=tweet_dic)

@login_required(login_url="/login")
def addtwetter(request):
    if request.POST:
        message = request.POST["message"]
        models.Tweet.objects.create(username = request.user, messange = message)
        return redirect(reverse("twetterapp:listtwet"))
    else:
        return render(request,"twetterapp/addtwet.html")

@login_required
def deletetwet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect("twetterapp:listtwet")

class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/singup.html"