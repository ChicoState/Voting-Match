# Documentation about Django models:
# https://docs.djangoproject.com/en/4.1/topics/db/models/
#
# Model fields:
# https://docs.djangoproject.com/en/4.1/ref/models/fields/

from django.db import models
from django.contrib.auth.models import User

# Extending the User model:
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Candidate(models.Model):
    STATES = [
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
        ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'),
        ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'),
        ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'),
        ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
        ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'),
        ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
        ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'),
        ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'),
        ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATES)

    def __str__(self):
        return self.first_name + self.last_name

class Issue(models.Model):
    name = models.CharField(max_length=200, unique=True)
    candidate_opinion = models.ManyToManyField(Candidate, through='CandidateOpinion')
    user_opinion = models.ManyToManyField(Voter, through='VoterOpinion')

    def __str__(self):
        return self.name

# Cross table model reference:
# https://stackoverflow.com/questions/69687277/how-to-add-custom-field-in-manytomany-through-table-in-django
class CandidateOpinion(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    position = models.FloatField() # 1.0 is favors, 0.0 is mixed or no opinion, -1.0 is opposes

    def __str__(self):
        return self.candidate.name + ': ' + self.issue.name

class VoterOpinion(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    position = models.FloatField(default=0.0) # 1.0 is strongly favors, -1.0 is strongly opposes
    weight = models.FloatField(default=0.0) # 1.0 is most important, 0.0 is not important

    def __str__(self):
        return self.voter.user.username + ': ' + self.issue.name

class CandidateScore(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return self.voter.user.username + ': ' + self.candidate.name