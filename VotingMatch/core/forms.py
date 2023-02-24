# Documentation about Django forms: 
# https://docs.djangoproject.com/en/4.1/topics/forms/
#
# Form fields:
# https://docs.djangoproject.com/en/4.1/ref/forms/fields/
#
# Widgets:
# https://docs.djangoproject.com/en/4.1/ref/forms/widgets/

from django import forms

class VoterIssueForm(forms.Form):
    abortion_opinion = forms.ChoiceField(label='Abortion', choices=((i,i) for i in range(1,6)))