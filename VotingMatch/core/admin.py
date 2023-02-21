from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(Model)
admin.site.register(models.Voter)
admin.site.register(models.Candidate)
# admin.site.register(models.Issue)
# admin.site.register(models.CandidateOpinion)
# admin.site.register(models.UserOpinion)
