# Documentation about QuerySet API:
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/

from django.shortcuts import render, redirect

from .forms import VoterIssueForm
from .models import Issue, Voter, VoterOpinion, CandidateOpinion, CandidateScore

# Create your views here.
def home(request):
	context = {}
	return render(request, 'core/home.html')

def issue_form(request):
	form = VoterIssueForm()

	context = {
		'form': form,
	}

	if request.method == 'POST':			
		form = VoterIssueForm(request.POST)
		if form.is_valid():
			# Do form stuff
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
			
			return redirect('home')

	return render(request, 'voter-core/form.html', context)

def candidate_form(request):
	context = {}
	return render(request, 'core/candidate-form.html', {})
