# Documentation about Django urls:
# https://docs.djangoproject.com/en/4.1/topics/http/urls/

from django.urls import path

from frontend import views

urlpatterns = [
	path('', views.DashboardRedirect.as_view()),
	path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
	path('candidates/', views.CandidatesView.as_view(), name='candidates'),
	path('form/', views.VoterFormView.as_view(), name='form'),

	# Login/Logout/Register
	path('login/', views.Login.as_view(), name='login'),
	path('logout/', views.Logout.as_view(), name='logout'),
	path('register/', views.RegisterView.as_view(), name='register'),
]
