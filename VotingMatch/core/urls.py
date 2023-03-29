# Documentation about Django urls:
# https://docs.djangoproject.com/en/4.1/topics/http/urls/

from django.urls import path

from core import views

urlpatterns = [
    # Old url paths, will be removed soon.
    path('', views.home, name='home'),
    path('form/', views.voter_form, name='voter-form'),
    path('candidate-form/<int:id>', views.candidate_form, name='candidate-form'),
    path('candidate-scores/<int:id>', views.candidate_scores, name='candidate-scores'),

    path('form/add-user-issue/<int:id>', views.form_add_user_issue, name='form-add-user-issue'),
    path('form/remove-user-issue/<int:id>', views.form_remove_user_issue, name='form-remove-user-issue'),
    path('form/issue-search/', views.form_issue_search, name='form-issue-search'),
    path('form/save-user-issue/<int:id>', views.form_save_user_issue, name='form-save-user-issue')
]
