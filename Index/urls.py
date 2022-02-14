from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('blog1',views.blog1,name='blog1'),
    path('blog2',views.blog2,name='blog2'),
    path('blog3',views.blog3,name='blog3'),
    path('auditorium',views.auditorium,name='auditorium'),
]
