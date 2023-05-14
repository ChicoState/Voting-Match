# Documentation about Django models:
# https://docs.djangoproject.com/en/4.1/topics/db/models/
#
# Model fields:
# https://docs.djangoproject.com/en/4.1/ref/models/fields/

from django.db import models
from django.contrib.auth.models import AbstractUser

from core.managers import CandidateOpinionManager


# Extending the User model:
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
class Voter(AbstractUser):
    pass

    # def __str__(self):
    #     return self.username


class Candidate(models.Model):
    STATES = [
        ("AL", "Alabama"),
        ("AK", "Alaska"),
        ("AZ", "Arizona"),
        ("AR", "Arkansas"),
        ("CA", "California"),
        ("CO", "Colorado"),
        ("CT", "Connecticut"),
        ("DE", "Delaware"),
        ("DC", "District of Columbia"),
        ("FL", "Florida"),
        ("GA", "Georgia"),
        ("HI", "Hawaii"),
        ("ID", "Idaho"),
        ("IL", "Illinois"),
        ("IN", "Indiana"),
        ("IA", "Iowa"),
        ("KS", "Kansas"),
        ("KY", "Kentucky"),
        ("LA", "Louisiana"),
        ("ME", "Maine"),
        ("MD", "Maryland"),
        ("MA", "Massachusetts"),
        ("MI", "Michigan"),
        ("MN", "Minnesota"),
        ("MS", "Mississippi"),
        ("MO", "Missouri"),
        ("MT", "Montana"),
        ("NE", "Nebraska"),
        ("NV", "Nevada"),
        ("NH", "New Hampshire"),
        ("NJ", "New Jersey"),
        ("NM", "New Mexico"),
        ("NY", "New York"),
        ("NC", "North Carolina"),
        ("ND", "North Dakota"),
        ("OH", "Ohio"),
        ("OK", "Oklahoma"),
        ("OR", "Oregon"),
        ("PA", "Pennsylvania"),
        ("RI", "Rhode Island"),
        ("SC", "South Carolina"),
        ("SD", "South Dakota"),
        ("TN", "Tennessee"),
        ("TX", "Texas"),
        ("UT", "Utah"),
        ("VT", "Vermont"),
        ("VA", "Virginia"),
        ("WA", "Washington"),
        ("WV", "West Virginia"),
        ("WI", "Wisconsin"),
        ("WY", "Wyoming"),
        ("N/A", "Not Applicable"),
    ]

    PARTIES = [
        ("R", "Republican"),
        ("D", "Democrat"),
        ("I", "Independent"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    state = models.CharField(max_length=3, choices=STATES, default="N/A")
    party = models.CharField(max_length=1, choices=PARTIES, default="I")
    image_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return (
            self.first_name
            + " "
            + self.last_name
            + " ("
            + self.state
            + "-"
            + self.party
            + ")"
        )


class Issue(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image_name = models.CharField(max_length=50, default='')
    issue_description = models.CharField(max_length=50, default='')
    candidate_opinion = models.ManyToManyField(
        Candidate, through="CandidateOpinion", related_name="issues"
    )
    voter_opinion = models.ManyToManyField(
        Voter, through="VoterOpinion", related_name="issues"
    )

    def __str__(self):
        return self.name


# Cross table model reference:
# https://stackoverflow.com/questions/69687277/how-to-add-custom-field-in-manytomany-through-table-in-django
class CandidateOpinion(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    position = (
        models.FloatField()
    )  # 1.0 is favors, 0.0 is mixed or no opinion, -1.0 is opposes
    objects = CandidateOpinionManager()

    def __str__(self):
        return str(self.candidate) + ": " + str(self.issue)


class VoterOpinion(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, related_name="opinions")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    position = models.FloatField(
        default=0.0
    )  # 1.0 is strongly favors, -1.0 is strongly opposes
    weight = models.FloatField(
        default=0.0
    )  # 1.0 is most important, 0.1 is least important

    def __str__(self):
        return str(self.voter) + ": " + str(self.issue)


class CandidateScore(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE, related_name="scores")
    score = models.FloatField()

    def __str__(self):
        return str(self.voter) + ": " + str(self.candidate)
