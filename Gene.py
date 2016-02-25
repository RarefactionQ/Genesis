import random
class Gene(object):
	
	def __init__(self):
		self.locus = -1
		self.condition = None 
		self.condition_prob = -1
		self.congential = -1 #Congential = 0, Adult = 1
		self.dominant = None #Genes are either recessive or dominant. We Mendel for now
		self.emp = 0
		self.int = 0
		self.cre = 0

	@staticmethod
	def get_dominant(pair):
		Gene1 = pair[0]
		Gene2 = pair[1]
		if Gene1.locus != Gene2.locus :
			print "Comparing different Gene loci!"
		if Gene1.locus == -1 or Gene2 == -1:
			print "Uninitialized locus/loci Gene1:"+str(Gene1.locus)+" Gene2:"+str(Gene2.locus)
		if Gene1.dominant:
			return Gene1
		elif Gene2.dominant:
			return Gene2
		else:
			return Gene1

	def improper_gene(self):
		if self.locus == -1 or self.condition_prob == -1 or self.congential == -1:
			return True
		return False

	def birth_effects(self,baby):
		if self.improper_gene():
			print "Tried to use an improper gene on a baby"
			return
		if self.congential != 0:
			return
		if random.random() < self.condition_prob:
			baby.traits.append(self.condition)
			baby.empathy += self.emp
			baby.intelligence += self.int
			baby.creativity += self.cre

	def adult_effects(self,adult):
		if self.improper_gene():
			print "Tried to use an improper gene on a new adult"
			return
		if self.congential != 1:
			return
		if random.random() < self.condition_prob:
			adult.traits.append(self.condition)
			adult.empathy += self.emp
			adult.intelligence += self.int
			adult.creativity += self.cre
