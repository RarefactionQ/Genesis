import csv
import random

from Gene import Gene
from Enum import Enum

Sex = Enum(['Male', 'Female'])

class Crewmate(object):
    id_counter = 0
    def __init__(self):
        self.crew_id = Crewmate.id_counter
        Crewmate.id_counter += 1

        # Setting default values
        self.alive = True
        self.adult = False
        self.name = "Unnamed"
        self.set_parents()
        self.sex = None
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

    def __cmp__(self, other):
        return cmp(self.get_id(), other.get_id())

    def __hash__(self):
        return hash(self.get_id())

    def get_id(self):
        return self.crew_id

    def set_parents(self, dad=None, mom=None):
        # Hack to let them breed
        if dad is None:
            dad = type('X', (object,), dict(name="Lost to the ages", crew_id=-1000*random.random()))
        if mom is None:
            mom = type('X', (object,), dict(name="Lost to the ages", crew_id=-1000*random.random()))
        self.dad = dad
        self.mom = mom

    def set_sex(self, sex=None):
        if sex is None:
            sex = random.choice(Sex)
        self.sex = sex

    def set_name(self, last=None, first=None):
        name_file = "names.txt"
        if last is None or first is None:
            with open(name_file, 'r') as f:
                reader = csv.reader(f)
                last_names = reader.next()
                boys_names = reader.next()
                girls_names = reader.next()
                if last is None:
                    last = random.choice(last_names)
                if first is None:
                    if self.sex is None:
                        print "Tried to name while sex isn't set!"
                        return
                    elif self.sex == Sex.Male:
                        first = random.choice(boys_names)
                    elif self.sex == Sex.Female:
                        first = random.choice(girls_names)

        self.name = first+" "+last

    def grow_one_year(self):
        self.age += 1
        if self.age == 15:
            self.become_adult()
        if self.sex == Sex.Female and self.age == 45:
            self.sterile = True
        if self.sex == Sex.Male and self.age == 65:
            self.sterile = True
        # self.training = False

    def become_adult(self):
        print self.name + " crew id:" + str(self.crew_id) + " has become an adult"
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
        self.genome = zip(gamete1, gamete2)

    def be_born(self, dad=None, mom=None):
        self.set_parents(dad, mom)
        last_name = mom.name.split(' ')[1]
        self.set_sex()
        self.set_name(last_name)
        self.inherit()
        for gene in self.genome:
            Gene.get_dominant(gene).birth_effects(self)

    def breedable(self):
        return self.adult and not self.sterile and not self.breeding
