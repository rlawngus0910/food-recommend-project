from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommendView),
    path('result/', views.recommendResultView)
]