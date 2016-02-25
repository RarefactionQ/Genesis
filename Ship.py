from Crewmate import Crewmate

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


	def compute_healthiness(self):
		sum_healthcare = 0.0
		temp = 0.0
		for member in self.crew:
			if member.job == "Doctor":
				temp += member.empathy
				temp += member.intelligence
				sum_healthcare += temp
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
