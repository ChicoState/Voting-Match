from django.shortcuts import render
from django.views.generic import View, RedirectView, FormView, ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from frontend.forms import RegisterForm, IssueForm
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

class CandidateDetailView(DetailView):
	template_name = 'candidate_detail.html'
	model = Candidate
	context_object_name = 'candidate'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class CandidateEditView(UserPassesTestMixin, DetailView):
	template_name = 'candidate_edit.html'
	model = Candidate
	context_object_name = 'candidate'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["issues"] = Issue.objects.all()
		return context

	def test_func(self):
		return self.request.user.is_staff

class IssuesView(ListView):
	template_name = 'issues.html'
	model = Issue
	context_object_name = 'issues'

	def get_queryset(self):
		return super().get_queryset()
	

class IssueFormViewPt1(LoginRequiredMixin, View):
	login_url = reverse_lazy('login')
	template_name = 'issue-form-pt1.html'

	def get(self, request, *args, **kwargs):
		voter = self.request.user
		selected = voter.opinions.all()
		issues = Issue.objects.all().exclude(name__in=voter.issues.all().values_list('name', flat=True))
		
		context = {
			'selected': selected,
			'issues': issues,
		}
		return render(request, self.template_name, context)

class IssueFormViewPt2(LoginRequiredMixin, View):
	login_url = reverse_lazy('login')
	template_name = 'issue-form-pt2.html'

	def get(self, request, *args, **kwargs):
		voter = self.request.user
		selected = voter.opinions.all()

		context = {
			'selected': selected,
		}
		return render(request, self.template_name, context)

class ScoresView(LoginRequiredMixin, View):
	login_url = reverse_lazy('login')
	template_name = 'scores.html'

	def get(self, request, *args, **kwargs):
		
		context = {}
		return render(request, self.template_name, context)