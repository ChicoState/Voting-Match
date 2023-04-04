# Documentation about Django urls:
# https://docs.djangoproject.com/en/4.1/topics/http/urls/

from django.urls import path

from frontend import views

urlpatterns = [
	path('', views.DashboardRedirect.as_view()),
	path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
	path('candidates/', views.CandidatesView.as_view(), name='candidates'),
	path('candidate/<pk>', views.CandidateDetailView.as_view(), name='candidate'),
	path('issues/', views.IssuesView.as_view(), name='issues'),
	path('scores/', views.ScoresView.as_view(), name='scores'),

	# Issue form
	path('issue-form/pt-1', views.IssueFormViewPt1.as_view(), name='issue-form-pt1'),
	path('issue-form/pt-2', views.IssueFormViewPt2.as_view(), name='issue-form-pt2'),

	# Login/Logout/Register
	path('login/', views.Login.as_view(), name='login'),
	path('logout/', views.Logout.as_view(), name='logout'),
	path('register/', views.RegisterView.as_view(), name='register'),
]
