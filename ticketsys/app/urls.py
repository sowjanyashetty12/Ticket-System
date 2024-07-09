
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("register",views.registeruser,name="register"),
    path("login",views.loginuser,name="login"),
    path("logout",views.userlogout,name="logout"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("createrecord",views.create_record,name="createrecord"),
    path("updaterecord/<int:pk>",views.update_record,name="updaterecord"),
    #below is to view singular record
    path("viewrecord/<int:pk>",views.viewrecord,name="viewrecord"),
    path("deleterecord/<int:pk>",views.deleterecord,name="deleterecord"),
]
