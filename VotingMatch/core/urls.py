# Documentation about Django urls:
# https://docs.djangoproject.com/en/4.1/topics/http/urls/

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.voter_form, name='form'),
    path('candidate-form/<int:id>', views.candidate_form, name='candidate-form'),
    path('candidate-scores/<int:id>', views.candidate_scores, name='candidate-scores'),
]
