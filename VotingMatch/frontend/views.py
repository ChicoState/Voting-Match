from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView

# Create your views here.
class DashboardView(TemplateView):
	template_name = 'dashboard.html'

class DashboardRedirect(RedirectView):
	url = 'dashboard/'