# Documentation about QuerySet API:
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/

from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Decorators
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods

# Models and Forms
from core.models import *

@login_required
def form_add_user_issue(request, id):
	voter = request.user
	issue = Issue.objects.get(pk=id)
	op = VoterOpinion(voter=voter, issue=issue, position=0.0, weight=0.0)
	op.save()

	update_weights(voter)

	selected = voter.opinions.all()
	issues = Issue.objects.all().exclude(name__in=voter.issues.all().values_list('name', flat=True))

	context = {
		'selected': selected,
		'issues': issues,
	}
	return render(request, 'content/form/user-issues.html', context)

@login_required
@require_http_methods(['DELETE'])
def form_remove_user_issue(request, id):
	voter = request.user
	issue = Issue.objects.get(pk=id)
	op = VoterOpinion.objects.get(voter=voter, issue=issue)
	op.delete()

	update_weights(voter)

	selected = voter.opinions.all()
	issues = Issue.objects.all().exclude(name__in=voter.issues.all().values_list('name', flat=True))

	context = {
		'selected': selected,
		'issues': issues,
	}
	return render(request, 'content/form/user-issues.html', context)

@login_required
def form_issue_search(request):
	search_text = request.POST.get('form-issue-search')
	user_issues = request.user.issues.all()
	results = Issue.objects.filter(name__icontains=search_text).exclude(name__in=user_issues.values_list('name', flat=True))
	
	context = {
		'issues': results,
	}
	return render(request, 'content/form/issue-search-results.html', context)

@login_required
def form_save_user_issue(request, id):
	try:
		voter_opinion = VoterOpinion.objects.get(pk=id)
		voter_opinion.position = request.POST.get(str(id))
		voter_opinion.save()
	except VoterOpinion.DoesNotExist:
		pass
	
	return HttpResponse('')

@login_required
def form_sort(request):
	voter = request.user
	issue_order = request.POST.getlist('user-issue-order')

	size = len(issue_order)
	weight = 1.0
	for id in issue_order:
		try:
			voter_opinion = VoterOpinion.objects.get(pk=id)
			voter_opinion.weight = weight
			voter_opinion.save()
			weight -= 1.0/size
		except VoterOpinion.DoesNotExist:
			pass


	selected = voter.opinions.all()
	issues = Issue.objects.all().exclude(name__in=voter.issues.all().values_list('name', flat=True))

	context = {
		'selected': selected,
		'issues': issues,
	}
	return render(request, 'content/form/user-issues.html', context)

def update_weights(voter):
	opinions = voter.opinions.all().order_by('weight').reverse()

	size = len(opinions)
	weight = 1.0
	for opinion in opinions:
		opinion.weight = weight
		opinion.save()
		weight -= 1.0/size

@staff_member_required
def edit_candidate_issue(request, id):
	candidate = Candidate.objects.get(pk=id)
	issue = Issue.objects.get(pk=request.POST.get('issue'))
	value = float(request.POST.get('value'))

	try:
		op = CandidateOpinion.objects.get(candidate=candidate, issue=issue)
		op.position = value
		op.save()
	except CandidateOpinion.DoesNotExist:
		op = CandidateOpinion(candidate=candidate, issue=issue, position=value)
		op.save()

	return HttpResponse('')