from django.shortcuts import render
from django.views.generic import View, RedirectView, FormView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegisterForm
from core.models import Candidate, Voter, Issue

class DashboardView(LoginRequiredMixin, View):
	login_url = reverse_lazy('login')
	template_name = 'dashboard.html'

	def get(self, request, *args, **kwargs):
		voter = self.request.user
		context = {
			'candidates': voter.scores.all(),
			'issues': voter.issues.all(),
		}
		return render(request, self.template_name, context)

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
	context_object_name = 'candidates'

	def get_queryset(self):
		return super().get_queryset()

class VoterFormView(View):
	template_name = 'form.html'

	def get(self, request, *args, **kwargs):
		voter = self.request.user
		selected = voter.issues.all()
		issues = Issue.objects.all().exclude(name__in=selected.values_list('name', flat=True))
		context = {
			'selected': selected,
			'issues': issues,
		}
		return render(request, self.template_name, context)