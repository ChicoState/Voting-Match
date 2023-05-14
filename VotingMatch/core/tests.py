from django.test import TestCase
from core.models import *

# from managers import CandidateOpinionManager


class OpinionOrderTestCase(TestCase):
    def setUp(self):
        self.voter = Voter.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

    def calculate_scores(self):
        """The following is taken from views.py"""
        # For every candidate
        for candidate in Candidate.objects.all():
            score = 0

            # Get every user opinion
            for opinion in self.voter.opinions.all():
                issue = opinion.issue

                # Get candidates opinion on same issue
                try:
                    cand_op = CandidateOpinion.objects.get(
                        candidate=candidate, issue=issue
                    )
                except CandidateOpinion.DoesNotExist:
                    continue

                # Update score
                score += (
                    abs((opinion.position / 100) - cand_op.position) * opinion.weight
                )

            # Update or create score object
            try:
                cand_score = CandidateScore.objects.get(
                    candidate=candidate, voter=self.voter
                )
                cand_score.score = float(score)
                cand_score.save()
            except CandidateScore.DoesNotExist:
                cand_score = CandidateScore(
                    candidate=candidate, voter=self.voter, score=float(score)
                )
                cand_score.save()

    def test_candidate_score(self):
        candidate1 = Candidate.objects.create(
            first_name="Bob", last_name="Test", state="CA", party="D"
        )
        issue1 = Issue.objects.create(name="Unit Testing 1")
        issue2 = Issue.objects.create(name="Unit Testing 2")
        issue3 = Issue.objects.create(name="Unit Testing 3")
        co1 = CandidateOpinion.objects.create(
            candidate=candidate1, issue=issue1, position=1.0
        )
        co2 = CandidateOpinion.objects.create(
            candidate=candidate1, issue=issue2, position=1.0
        )
        co3 = CandidateOpinion.objects.create(
            candidate=candidate1, issue=issue3, position=-1.0
        )
        VoterOpinion.objects.create(
            voter=self.voter, issue=issue1, position=1.0, weight=0.5
        )
        VoterOpinion.objects.create(
            voter=self.voter, issue=issue2, position=1.0, weight=1.0
        )
        VoterOpinion.objects.create(
            voter=self.voter, issue=issue3, position=1.0, weight=0.0
        )

        self.calculate_scores()
        qs = CandidateOpinion.objects.get_voter_order(self.voter)

        # Make sure the candidate opinions are in the same order as
        # the voter put them
        self.assertEqual(qs[candidate1][0], co2)
        self.assertEqual(qs[candidate1][1], co1)
        self.assertEqual(qs[candidate1][2], co3)
