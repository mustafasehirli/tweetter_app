from django.urls import path
from . import views

app_name = "twetterapp"

urlpatterns = [
    path("listtwet",views.listtwet, name="listtwet"),
    path("addtwet", views.addtwetter, name="addtwet")
]