import Crewmate
import Ship
import random

class Quest(object):
    id_counter = 0
    def __init__(self):
        Quest.id_counter += 1
        self.quest_id = Quest.id_counter
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

    def victory(self,ship):
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
        elif self.v_type == "fuel":
            ship.fuel += self.v_int

    def failure(self,ship):
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
        elif self.f_type == "fuel":
            ship.fuel -= self.f_int
        elif self.f_type == "death":
            ship.death(random.choice(ship.crew))

    def succeed(self):
        return self.work >= self.cost

    def count_work(self,ship):
        temp = 0
        for mate in ship.crew:
            if mate.job == self.description+" "+str(self.quest_id):
                if "emp" in self.type:
                    temp += mate.creativity
                if "int" in self.type:
                    temp += mate.intelligence
                if "cre" in self.type:
                    temp += mate.creativity
        return temp

    def apply_work(self,ship):
        self.work = self.count_work(ship)
