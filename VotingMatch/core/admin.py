from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(Model)
admin.site.register(models.Voter)
admin.site.register(models.Candidate)
