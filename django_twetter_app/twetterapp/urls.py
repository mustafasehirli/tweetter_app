from django.urls import path
from . import views

app_name = "twetterapp"

urlpatterns = [
    path("list",views.listtwet, name="listtwet"),
    path("add", views.addtwetter, name="addtwet")
]