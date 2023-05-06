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

    def test_single_candidate(self):
        candidate1 = Candidate.objects.create(
            first_name="Bob", last_name="Test", state="CA", party="D"
        )
        issue = Issue.objects.create(name="Unit Testing")
        CandidateOpinion.objects.create(candidate=candidate1, issue=issue, position=1.0)
        VoterOpinion.objects.create(
            voter=self.voter, issue=issue, position=1.0, weight=1.0
        )

        self.calculate_scores()
        qs = CandidateOpinion.objects.get_voter_order(self.voter)
        self.assertEqual(len(qs), 1)

    def test_two_candidates(self):
        candidate1 = Candidate.objects.create(
            first_name="Bob", last_name="Test", state="CA", party="D"
        )
        candidate2 = Candidate.objects.create(
            first_name="Bill", last_name="Test", state="TX", party="R"
        )
        issue = Issue.objects.create(name="Unit Testing")
        VoterOpinion.objects.create(
            voter=self.voter, issue=issue, position=1.0, weight=1.0
        )
        CandidateOpinion.objects.create(candidate=candidate1, issue=issue, position=1.0)
        CandidateOpinion.objects.create(
            candidate=candidate2, issue=issue, position=-1.0
        )

        self.calculate_scores()
        qs = CandidateOpinion.objects.get_voter_order(self.voter)
        self.assertEqual(len(qs), 2)

        # Ensure ordering is correct
        candidates = list(qs)
        self.assertEqual(candidates[0], candidate1)
        self.assertEqual(candidates[1], candidate2)

    def test_three_candidates(self):
        candidate1 = Candidate.objects.create(
            first_name="Bob", last_name="Test", state="CA", party="D"
        )
        candidate2 = Candidate.objects.create(
            first_name="Bill", last_name="Test", state="TX", party="R"
        )
        candidate3 = Candidate.objects.create(
            first_name="Bert", last_name="Test", state="WA", party="I"
        )
        issue = Issue.objects.create(name="Unit Testing")
        VoterOpinion.objects.create(
            voter=self.voter, issue=issue, position=1.0, weight=1.0
        )
        CandidateOpinion.objects.create(candidate=candidate1, issue=issue, position=1.0)
        CandidateOpinion.objects.create(
            candidate=candidate2, issue=issue, position=-1.0
        )
        CandidateOpinion.objects.create(candidate=candidate3, issue=issue, position=0.0)

        self.calculate_scores()
        qs = CandidateOpinion.objects.get_voter_order(self.voter)
        self.assertEqual(len(qs), 3)

        # Ensure ordering is correct
        candidates = list(qs)
        self.assertEqual(candidates[0], candidate1)
        self.assertEqual(candidates[1], candidate3)
        self.assertEqual(candidates[2], candidate2)
