# Documentation about Django urls:
# https://docs.djangoproject.com/en/4.1/topics/http/urls/

from django.urls import path

from core import views

urlpatterns = [
    # Form
    path('form/add-user-issue/<int:id>', views.form_add_user_issue, name='form-add-user-issue'),
    path('form/remove-user-issue/<int:id>', views.form_remove_user_issue, name='form-remove-user-issue'),
    path('form/issue-search/', views.form_issue_search, name='form-issue-search'),
    path('form/save-user-issue/<int:id>', views.form_save_user_issue, name='form-save-user-issue'),
    path('form/sort/', views.form_sort, name='form-sort'),

    # Edit Candidate
    path('edit-candidate-issue/<int:id>', views.edit_candidate_issue, name='edit-candidate-issue'),
]
