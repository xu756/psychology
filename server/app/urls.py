from django.urls import path
from app import views

urlpatterns = [
    path('getdefault', views.getdefault, name='获取默认信息'),
]
