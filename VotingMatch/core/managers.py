from django.db import models

class CandidateOpinionManager(models.Manager):
	def get_voter_order(self, voter):
		voter_ops = voter.opinions.all().order_by('-weight')
		cand_scores = voter.scores.all().filter(voter=voter).order_by('score')
		qs = {}
		for score in cand_scores:
			candidate = score.candidate
			temp=[]
			for voter_op in voter_ops:
				temp.append(self.get(candidate=score.candidate, issue=voter_op.issue))
			qs[candidate] = temp
		return qs