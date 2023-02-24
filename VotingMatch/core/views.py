from django.shortcuts import render, redirect

from .forms import VoterIssueForm

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
            # do form stuff
            return redirect('home')

    return render(request, 'core/form.html', context)
        