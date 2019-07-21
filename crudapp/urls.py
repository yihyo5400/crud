from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls import url

urlpatterns = [

    path('', views.read , name="home"),
    path('newblog/', views.create, name="newblog"),
    path('<int:board_id>/',views.detail, name="detail"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('<int:pk>/comment/write/', views.comment_write, name='comment_write'),
    path('<int:board_pk>/comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
]