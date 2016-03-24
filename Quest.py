import Crewmate
import Ship
import random

class Quest(object):
    id_counter = 0
    def __init__(self):
        id_counter += 1
        self.quest_id = id_counter
        self.intro = ""
        self.description = ""
        self.v_type = ""
        self.v_int = 0
        self.f_type = ""
        self.f_int = 0
        self.outro = ""
        self.type = ""
        self.cost = 0
        self.work = 0

    def victory(ship,self):
        if self.v_type == None:
            return
        elif self.v_type == "emp":
            for mate in ship.crew:
                mate.empathy += self.v_int
        elif self.v_type == "int":
            for mate in ship.crew:
                mate.intelligence += self.v_int
        elif self.v_type == "cre":
            for mate in ship.crew:
                mate.creativity += self.v_int
        elif self.v_type == "fuel"
            ship.fuel += self.v_int

    def failure(ship,self):
        if self.f_type == None:
            return
        elif self.f_type == "emp":
            for mate in ship.crew:
                mate.empathy -= self.f_int
        elif self.f_type == "int":
            for mate in ship.crew:
                mate.intelligence -= self.f_int
        elif self.f_type == "cre":
            for mate in ship.crew:
                mate.creativity -= self.f_int
        elif self.f_type == "fuel"
            ship.fuel -= self.f_int
        elif self.f_type == "death"
            ship.death(random.choice(ship.crew))

    def succeed(self):
        return self.work >= self.cost

    def apply_work(self,ship):
        for mate in ship.crew:
            if mate.job == self.description+" "+str(self.quest_id):
                if "emp" in self.type:
                    self.work += mate.creativity
                if "int" in self.type:
                    self.work += mate.intelligence
                if "cre" in self.type:
                    self.work += mate.creativity
