# Documentation about QuerySet API:
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/

from django.shortcuts import render, redirect

from .forms import *
from .models import *

# Create your views here.
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
					score += abs(vop.position-cop.position)/vop.weight

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

			
			return redirect('home')

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
					op = CandidateOpinion.objects.filter(issue=Issue.objects.get(name=issue), candidate=candidate).update(position=position, weight=weight)
				except CandidateOpinion.DoesNotExist:
					op = CandidateOpinion(
						candidate=candidate,
						issue=Issue.objects.get(name=issue),
						position=position,
					)
					op.save()
							
			return redirect('home')

	return render(request, 'core/candidate-form.html', context)
