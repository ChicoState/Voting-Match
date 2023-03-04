# Documentation about Django urls:
# https://docs.djangoproject.com/en/4.1/topics/http/urls/

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.issue_form, name='form'),
]
