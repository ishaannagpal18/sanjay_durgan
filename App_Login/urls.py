from django.urls import path
from App_Login import views
from django.contrib.auth import views as auth_views

app_name = 'App_Login'

urlpatterns=[
    path('register/',views.register_attempt,name='register_attempt'),
    path('login/',views.login_attempt,name='login_attempt'),
    path('logout/',views.logout_user,name='logout'),
]
