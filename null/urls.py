from django.contrib import admin
from django.urls import path
from null import views
app_name="app_abc"

urlpatterns = [
    path("",views.dashbord,name="tab"),
    path("table",views.staticnavigation,name="table"),
    path("table",views.table,name='table1'),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("password",views.password,name="password"),
    path("four",views.four,name="four"),
    path("five",views.five,name="five"),
    path("hundre",views.hundre,name="hundre"),
    path("layout",views.layout,name="layout"),
    path("layout2",views.layout2,name="layout2")

    
]
