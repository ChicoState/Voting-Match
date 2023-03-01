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
    Abortion = forms.ChoiceField(label='Abortion', choices=((i,i) for i in range(1,6)))
    Abortion_weight = forms.ChoiceField(label='Abortion_weight', choices=((i,i) for i in range(1,6)))