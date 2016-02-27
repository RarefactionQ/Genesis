from Crewmate import Crewmate
import random

class Ship:

	def __init__(self):
		self.crew = []
		self.fuel = -1
		self.ship_consumption = 500.0
		self.total_consumption = -1
		self.healthiness = -1
		self.safety = -1
		self.satisfaction = -1
		self.mission_year = -1
		self.speed = -1
		self.distance = -1
		self.priority = -1
		self.research = [-1.0,-1.0,-1.0,-1.0,-1.0] #health,safety,art,research,engine


	def compute_healthiness(self):
		sum_healthcare = 0.0
		temp = 0.0
		for member in self.crew:
			if member.job == "Doctor":
				temp += member.empathy
				temp += member.intelligence
				sum_healthcare += temp * self.research[0]
		morbidity = 10.0 * len(self.crew)
		self.healthiness = sum_healthcare/morbidity


	def compute_safety(self):
		sum_maintenance = 0.0
		temp = 0.0
		for member in self.crew:
			if member.job == "Engineer":
				temp += member.intelligence
				sum_maintenance += temp
		self.total_consumption = 10 * len(self.crew) + self.ship_consumption
		self.safety = sum_maintenance/self.total_consumption

	def compute_satisfaction(self):
		sum_happiness = 0.0
		temp = 0.0
		for member in self.crew:
			if member.job == "Artist":
				temp += member.empathy
				temp += member.creativity
				sum_happiness += temp
		unhappiness = 10 * len(self.crew)
		self.satisfaction = sum_happiness/unhappiness

	def compute_all(self):
		self.compute_satisfaction()
		self.compute_safety()
		self.compute_healthiness()

	def get_research_credits(self):
		sum_research = 0.0
		temp = 0.0
		for member in self.crew:
			if member.job == "Researcher":
				temp += member.intelligence
				temp += member.creativity
				sum_research += temp
		return sum_research

	def kill(self,mate):
		if random.random() < (mate.age - 20) / (self.healthiness * 100):
			mate.alive = False
			self.crew.remove(mate)

	def breed(self,mate):
		if mate.sterile or mate.breeding:
			return
		for partner in self.crew:
			if partner.sterile or partner.breeding:
				continue
			if partner.sex == mate.sex:
				continue
			prob = .2
			if mate.dad.crew_id == partner.dad.crew_id and mate.dad.crew_id!= -1:
				prob *= .1
			if mate.mom.crew_id == partner.mom.crew_id and mate.dad.crew_id!= -1:
				prob *= .1
			if random.random() > prob:
				baby = Crewmate()
				if mate.sex == 0:
					baby.be_born(mate,partner)
				else:
					baby.be_born(partner,mate)


	def pass_turn(self):

		for mate in self.crew:
			mate.grow_one_year()
			self.kill(mate)
			self.breed(mate)
