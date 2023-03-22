# Documentation about QuerySet API:
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/

from django.shortcuts import render, redirect

# Decorators
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Models and Forms
from core.forms import *
from core.models import *

# Old views, will be removed soon.
def home(request):
	candidates = Candidate.objects.all()
	
	context = {
		'candidates': candidates,
	}

	return render(request, 'core/home.html', context)

def voter_form(request):
	form = VoterForm()

	context = {
		'form': form,
	}

	# On form submission
	if request.method == 'POST':			
		form = VoterForm(request.POST)
		if form.is_valid():
			voter = Voter.objects.get(id=1)

			def paired(iterable):
				a = iter(iterable)
				return zip(a,a)
			
			# Iterate through every 2 form entries
			for issue, issue_w in paired(form.cleaned_data):
				position = float(form.cleaned_data[issue])
				weight = float(form.cleaned_data[issue_w])

				# Update existing db entry, otherwise create it
				try:
					VoterOpinion.objects.get(issue=Issue.objects.get(name=issue), voter=voter)
					op = VoterOpinion.objects.filter(issue=Issue.objects.get(name=issue), voter=voter).update(position=position, weight=weight)
				except VoterOpinion.DoesNotExist:
					op = VoterOpinion(
						issue=Issue.objects.get(name=issue),
						position=position,
						voter=voter,
						weight=weight,
					)
					op.save()
				
			# Candidate scoring goes here
			for candidate in Candidate.objects.all():
				score = 0
				for issue in Issue.objects.all():
					vop = VoterOpinion.objects.get(voter=voter, issue=issue)
					cop = CandidateOpinion.objects.get(candidate=candidate, issue=issue)

					# Calculate score
					score += abs(vop.position-cop.position)*vop.weight

				# Update existing db entry, otherwise create it
				try:
					CandidateScore.objects.get(candidate=candidate, voter=voter)
					cscore = CandidateScore.objects.filter(candidate=candidate, voter=voter).update(score=score)
				except CandidateScore.DoesNotExist:
					cscore = CandidateScore(
						candidate=candidate,
						voter=voter,
						score=score,
					)
					cscore.save()

			
			return redirect('/candidate-scores/'+str(voter.id))

	return render(request, 'core/voter-form.html', context)

def candidate_form(request, id):
	candidate = Candidate.objects.get(id=id)
	form = CandidateForm()

	context = {
		'candidate': candidate,
		'form': form,
	}

	if request.method == 'POST':			
		form = CandidateForm(request.POST)
		if form.is_valid():
			# Iterate through every form entry
			for issue in form.cleaned_data:
				position = float(form.cleaned_data[issue])

				# Update existing db entry, otherwise create it
				try:
					CandidateOpinion.objects.get(issue=Issue.objects.get(name=issue), candidate=candidate)
					op = CandidateOpinion.objects.filter(issue=Issue.objects.get(name=issue), candidate=candidate).update(position=position)
				except CandidateOpinion.DoesNotExist:
					op = CandidateOpinion(
						candidate=candidate,
						issue=Issue.objects.get(name=issue),
						position=position,
					)
					op.save()
							
			return redirect('home')

	return render(request, 'core/candidate-form.html', context)

def candidate_scores(request, id):
	voter = Voter.objects.get(id=id)
	candidates = Candidate.objects.all()
	issues = Issue.objects.all()
	candidate_opinions = CandidateOpinion.objects.all()
	voter_opinions = VoterOpinion.objects.all()
	candidate_scores = CandidateScore.objects.all()

	context = {
		'voter': voter,
		'candidates': candidates,
		'issues': issues,
		'candidateopinions': candidate_opinions,
		'voteropinions': voter_opinions,
		'candidatescores': candidate_scores,
	}

	return render(request, 'core/candidate-scores.html', context)

@login_required
def form_add_user_issue(request, id):
	voter = request.user
	issue = Issue.objects.get(pk=id)
	op = VoterOpinion(voter=voter, issue=issue, position=0.0, weight=0.0)
	op.save()

	selected = voter.issues.all()
	issues = Issue.objects.all().exclude(name__in=selected.values_list('name', flat=True))

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

	selected = voter.issues.all()
	issues = Issue.objects.all().exclude(name__in=selected.values_list('name', flat=True))

	context = {
		'selected': selected,
		'issues': issues,
	}
	return render(request, 'content/form/user-issues.html', context)

@login_required
def form_issue_search(request):
	search_text = request.POST.get('form-issue-search')
	print(search_text)

	user_issues = request.user.issues.all()
	results = Issue.objects.filter(name__icontains=search_text).exclude(name__in=user_issues.values_list('name', flat=True))
	
	context = {
		'issues': results,
	}
	return render(request, 'content/form/issue-search-results.html', context)