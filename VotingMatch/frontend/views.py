from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, FormView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import RegisterForm
from core.models import Candidate, Voter

# Create your views here.
class DashboardView(TemplateView):
	template_name = 'dashboard.html'

class DashboardRedirect(RedirectView):
	url = 'dashboard/'

class Login(LoginView):
	template_name = 'content/login.html'
	
	def get_success_url(self):
		return reverse_lazy('dashboard')

class Logout(LogoutView):

	def get_success_url(self): 
		return reverse_lazy('login')

class RegisterView(FormView):
	form_class = RegisterForm
	template_name = 'content/register.html'
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		form.save() # save the user
		return super().form_valid(form)

class CandidatesView(ListView):
	template_name = 'candidates.html'
	model = Candidate