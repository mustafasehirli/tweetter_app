from django.urls import path
from . import views

app_name = "twetterapp"

urlpatterns = [
    path("list",views.listtwet, name="listtwet"),
    path("add", views.addtwetter, name="addtwet"),
    path("singup",views.SingUpView.as_view(),name="singup"),
    path("delete/<int:id>",views.deletetwet, name="delete")
]