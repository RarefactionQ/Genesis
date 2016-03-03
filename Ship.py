import random

from Crewmate import Crewmate, Sex
import UI

class Ship(object):

    def __init__(self):
        self.crew = []
        self.fuel = -1
        self.ship_consumption = 500.0
        self.total_consumption = -1
        self.healthiness = -1
        self.safety = -1
        self.satisfaction = -1
        self.current_satisfaction = -1
        self.mission_year = -1
        self.speed = -1
        self.distance = -1
        self.priority = -1
        self.research = [-1.0, -1.0, -1.0, -1.0, -1.0] # health, safety, art, research, engine
        self.happiness_penalty = -1


    def compute_healthiness(self):
        sum_healthcare = 0.0
        temp = 0.0
        for member in self.crew:
            if member.job == "Doctor" and member.adult:
                temp += member.empathy
                temp += member.intelligence
                sum_healthcare += temp * self.research[0] * self.current_satisfaction
            if member.job == "Laborer" and member.adult:
                sum_healthcare += 10
        morbidity = 10.0 * len(self.crew)
        self.healthiness = sum_healthcare/morbidity


    def compute_safety(self):
        sum_maintenance = 0.0
        temp = 0.0
        for member in self.crew:
            if member.job == "Engineer" and member.adult:
                temp += 5 * member.intelligence
                sum_maintenance += temp * self.research[1] * self.current_satisfaction
            if member.job == "Laborer" and member.adult:
                sum_maintenance += 30
        self.total_consumption = (10 * len(self.crew) + self.ship_consumption) / (self.research[4])
        self.safety = sum_maintenance/self.total_consumption

    def compute_satisfaction(self):
        sum_happiness = 0.0
        temp = 0.0
        for member in self.crew:
            if member.job == "Artist" and member.adult:
                temp += member.empathy
                temp += member.creativity
                sum_happiness += temp * self.research[2] * self.current_satisfaction
            if member.job == "Laborer" and member.adult:
                sum_happiness += 5
        unhappiness = 10 * len(self.crew) + self.happiness_penalty
        self.satisfaction = min(sum_happiness/unhappiness, 2.0)

    def compute_all(self):
        self.compute_satisfaction()
        self.compute_safety()
        self.compute_healthiness()

    def get_research_credits(self):
        sum_research = 0.0
        temp = 0.0
        for member in self.crew:
            if member.job == "Researcher" and member.adult:
                temp += member.intelligence
                temp += member.creativity
                sum_research += temp * self.research[3] * self.current_satisfaction
        return sum_research

    def kill(self, mate):
        if random.random() * (mate.age/20) > self.healthiness:
            mate.alive = False
            self.crew.remove(mate)
            print UI.inline_print(mate)+" has died at age "+str(mate.age)

    def breed(self, mate):
        if not mate.breedable():
            return
        for partner in self.crew:
            # no sterile or pregnant partners
            if not partner.breedable():
                continue
            if partner.sex == mate.sex:
                continue
            # no fathers or mothers
            if partner.crew_id == mate.mom.crew_id or partner.crew_id == mate.dad.crew_id:
                continue
            if mate.crew_id == partner.mom.crew_id or mate.crew_id == partner.dad.crew_id:
                continue
            prob = .006
            # half siblings and full siblings
            if mate.dad.crew_id == partner.dad.crew_id:
                prob *= .01
            if mate.mom.crew_id == partner.mom.crew_id:
                prob *= .01
            if random.random() < prob:
                baby = Crewmate()
                mate.breeding = True
                partner.breeding = True
                if mate.sex == Sex.Male:
                    baby.be_born(mate, partner)
                else:
                    baby.be_born(partner, mate)
                self.crew.append(baby)
                print UI.inline_print(baby)+" has been born."
                print "Their parents are "+mate.name+" and "+partner.name
                return

    def breed_all(self):
        temp = self.crew
        random.shuffle(temp)
        for mate in temp:
            self.breed(mate)

    def pass_turn(self):
        self.current_satisfaction = self.satisfaction
        self.happiness_penalty = 0
        self.research[self.priority] += self.get_research_credits() / 1000
        for mate in self.crew:
            mate.grow_one_year()
            self.kill(mate)
            self.breed(mate)
        for mate in self.crew:
            mate.breeding = False
        self.fuel -= self.total_consumption
        if self.safety < random.random():
            print "Core Overheated. Fuel vented"
            self.fuel -= self.total_consumption
            if self.safety < random.random():
                print "Core CRITICAL. Massive Fuel Ejected"
                self.fuel -= 10 * self.total_consumption
                if self.safety < random.random():
                    print "CONTAINMENT FAILURE"
                    self.fuel = -1
        self.distance -= self.speed
        self.mission_year += 1
