import csv
import random
import sys

from Gene import Gene
from Crewmate import Crewmate
from Ship import Ship
from Quest import Quest

SOURCE_FILE_CREW = 'initial_crew.csv'
SOURCE_FILE_GENES = 'initial_genes.csv'
SOURCE_FILE_QUESTS = 'initial_quest.csv'

def import_crew():
    temp = Ship()
    genetics = import_genetics()
    seed = []
    for _ in range(100):
        mate = Crewmate()
        mate.set_sex()
        mate.set_name()
        mate.adult = True
        create_genome(mate, genetics)
        seed.append(mate)
    temp.crew = seed
    # while len(temp.crew) < 101:
    #     temp.breed_all()
    #     print "breeding"
    temp.breed_all()
    del temp.crew[0:100]
    for mate in temp.crew:
        mate.age = int(20*random.random()) + 15
        mate.become_adult()

    return temp.crew

def import_genetics():
    genetics = []
    with open(SOURCE_FILE_GENES, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            gene = Gene()
            gene.locus = row[0]
            gene.condition = row[1]
            gene.condition_prob = row[2]
            # print str(gene.condition_prob)+" prob"
            gene.congential = row[3].strip()
            # print str(gene.congential)+" congential"
            gene.dominant = row[4]
            gene.emp = row[5]
            gene.int = row[6]
            gene.cre = row[7]
            genetics.append(gene)
    if genetics is None or len(genetics) == 0:
        sys.exit(0)
    return genetics

def create_genome(crew, genetics):
    for loc in range(len(genetics)):
        temp = []
        for gene in genetics:
            if int(gene.locus) == int(loc):
                temp.append(gene)
        if len(temp) == 0:
            continue
        crew.genome.append([random.choice(temp), random.choice(temp)])

def get_random_quest():
    return import_a_quest()

def import_a_quest():
    with open(SOURCE_FILE_QUESTS, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        length = int(reader.next()[0])
        choice = random.randint(0,length-1)
        for _ in range(0,choice):
            reader.next()
        row = reader.next()
        quest = Quest()
        quest.intro = str(row[0])
        quest.description = str(row[1])
        quest.v_type = str(row[2])
        quest.v_int = int(row[3])
        quest.f_type = str(row[4])
        quest.f_int = int(row[5])
        quest.fail = str(row[6])
        quest.outro = str(row[7])
        quest.type = str(row[8])
        quest.constant = int(row[9])
        quest.variable = int(row[10])
        return quest

def test_quest():
    quest = Quest()
    quest.intro = "This is a testing Quest"
    quest.description = "test"
    quest.v_type = "emp"
    quest.v_int = 1
    quest.f_type = "emp"
    quest.f_int = -1
    quest.fail = "Fail"
    quest.outro = "Finished Testing Quest"
    quest.type = "emp"
    quest.cost = 10
    quest.work = 0
    return quest

def test_crew_infant():
    gene00 = Gene()
    gene00.locus = 0
    gene00.condition = "00"
    gene00.condition_prob = 1
    gene00.congential = 0 #Congential = 0, Adult = 1
    gene00.dominant = True #Genes are either recessive or dominant. We Mendel for now
    gene00.emp = 1
    gene00.int = 1
    gene00.cre = 1

    gene01 = Gene()
    gene01.locus = 0
    gene01.condition = "01"
    gene01.condition_prob = 1
    gene01.congential = 0 #Congential = 0, Adult = 1
    gene01.dominant = False #Genes are either recessive or dominant. We Mendel for now
    gene01.emp = -1
    gene01.int = -1
    gene01.cre = -1

    crew1 = Crewmate()
    crew1.set_sex()
    crew1.set_name("01", "crew")
    crew1.genome.append([gene00, gene01])

    crew2 = Crewmate()
    crew2.set_sex()
    crew2.set_name("02", "crew")
    crew2.genome.append([gene01, gene01])

    crew1.mom = Crewmate()
    crew1.mom.name = "mom"
    crew1.dad = Crewmate()
    crew1.dad.name = "dad"

    crew2.mom = Crewmate()
    crew2.mom.name = "mom"
    crew2.dad = Crewmate()
    crew2.dad.name = "dad"

    return [crew1, crew2]

def test_crew_adult():

    gene00 = Gene()
    gene00.locus = 0
    gene00.condition = "00"
    gene00.condition_prob = 1
    gene00.congential = 1 # Congential = 0, Adult = 1
    gene00.dominant = True # Genes are either recessive or dominant. We Mendel for now
    gene00.emp = 1
    gene00.int = 1
    gene00.cre = 1

    gene01 = Gene()
    gene01.locus = 0
    gene01.condition = "01"
    gene01.condition_prob = 1
    gene01.congential = 1 #Congential = 0, Adult = 1
    gene01.dominant = False #Genes are either recessive or dominant. We Mendel for now
    gene01.emp = -1
    gene01.int = -1
    gene01.cre = -1

    crew1 = Crewmate()
    crew1.set_sex()
    crew1.set_name("01", "crew")
    crew1.genome.append([gene00, gene01])

    crew2 = Crewmate()
    crew2.set_sex()
    crew2.set_name("02", "crew")
    crew2.genome.append([gene01, gene01])

    crew1.mom = Crewmate()
    crew1.mom.name = "mom"
    crew1.dad = Crewmate()
    crew1.dad.name = "dad"

    crew2.mom = Crewmate()
    crew2.mom.name = "mom"
    crew2.dad = Crewmate()
    crew2.dad.name = "dad"

    return [crew1, crew2]

def test_ship():
    test = Ship()
    test.crew = import_crew()
    test.current_satisfaction = .5
    test.priority = 0
    test.research = [1.0, 1.0, 1.0, 1.0, 1.0] #health, safety, art, research, engine
    test.speed = .01
    test.distance = 50.0
    test.mission_year = 1000
    test.fuel = 2500000
    return test
