import csv
import random
from Gene import Gene
class Crewmate(object):
	@staticmethod
	def same_crewmate(a,b):
		if a.get_id() == b.get_id():
			return True
		else:
			return False

	id_counter = 0
	def __init__(self):
		self.crew_id = Crewmate.id_counter
		Crewmate.id_counter += 1

		# Setting default values
		self.alive = True
		self.adult = False
		self.name = "Unnamed"
		self.set_parents()
		self.sex = -1
		self.sterile = False
		self.job = "None"
		# self.training = False
		self.empathy = 0
		self.intelligence = 0 
		self.creativity = 0
		self.age = 0
		self.genome = [] #pairs of genes
		self.traits = []
		self.breeding = False

	def get_id(self):
		return self.crew_id

	def set_parents(self,D=None,M=None):
		self.dad = D
		self.mom = M
		if D == None and M == None:
			self.dad = type('X', (object,), dict(name="Lost to the ages",crew_id=-1))
			self.mom = type('X', (object,), dict(name="Lost to the ages",crew_id=-1))

	def set_sex(self,value=None):
		if value is None:
			self.sex = random.choice([0,1])
		else:
			self.sex = value

	def set_name(self,last=None,first=None):
		Name_File = "names.txt"
		if last == None or first == None:
			with open(Name_File, 'r') as f:
				reader = csv.reader(f)
				last_names = reader.next()
				boys_names = reader.next()
				girls_names = reader.next()
				if last == None:
					last = random.choice(last_names)
				if first == None:
					if self.sex == -1:
						print "Tried to name while sex isn't set!"
						return
					elif self.sex == 0:
						first = random.choice(boys_names)
					elif self.sex == 1:
						first = random.choice(girls_names)

		self.name = first+" "+last

	def grow_one_year(self):
		self.age += 1
		if self.age == 15:
			self.become_adult()
		if self.sex == 1 and self.age == 45:
			self.sterile = True
		if self.sex == 0 and self.age == 65:
			self.sterile = True
		# self.training = False

	def become_adult(self):
		print self.name+" crew id:"+str(self.crew_id)+" has become an adult"
		self.adult = True
		for gene in self.genome:
			Gene.get_dominant(gene).adult_effects(self)

	def get_gamete(self):
		gamete = []
		for gene in self.genome:
			gamete.append(random.choice(gene))
		return gamete

	def inherit(self):
		gamete1 = self.dad.get_gamete()
		gamete2 = self.mom.get_gamete()
		self.genome = zip(gamete1,gamete2)

	def be_born(self,D=None,M=None):
		self.set_parents(D,M)
		last_name = M.name.split(' ')[0]
		self.set_sex()
		self.set_name(last_name)
		self.inherit()
		for gene in self.genome:
			Gene.get_dominant(gene).birth_effects(self)


