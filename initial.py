from Gene import Gene
from Crewmate import Crewmate
import random
from Ship import Ship
import csv

SOURCE_FILE_CREW = 'initial_crew.csv'
SOURCE_FILE_GENES = 'initial_genes.csv'

def import_crew():
	genetics = import_genetics()
	crew = []
	for x in range(20):
		mate = Crewmate()
		mate.set_sex()
		mate.set_name()
		create_genome(mate, genetics)
		crew.append(mate)
	return crew

def import_genetics():
	genetics = []
	with open(SOURCE_FILE_GENES, 'rb') as csvfile:
	    reader = csv.reader(csvfile)
	    for row in reader:
	    	gene = Gene()
	    	gene.locus = row[0]
	    	gene.condition = row[1]
	    	gene.condition_prob = row[2]
	    	gene.congential = row[3]
	    	gene.dominant = row[4]
	    	gene.emp = row[5]
	    	gene.int = row[6]
	    	gene.cre = row[7]
	    	genetics.append(gene)
	return genetics

def create_genome(crew, genetics):
	for loc in range(len(genetics)):
		temp = []
		for gene in genetics:
			if gene.locus == loc:
				temp.append(gene)
		if len(temp) == 0:
			continue
		crew.genome.append([random.choice(temp),random.choice(temp)])


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
	crew1.set_name("01","crew")
	crew1.genome.append([gene00,gene01])

	crew2 = Crewmate()
	crew2.set_sex()
	crew2.set_name("02","crew")
	crew2.genome.append([gene01,gene01])

	crew1.mom = Crewmate()
	crew1.mom.name = "mom"
	crew1.dad = Crewmate()
	crew1.dad.name = "dad"

	crew2.mom = Crewmate()
	crew2.mom.name = "mom"
	crew2.dad = Crewmate()
	crew2.dad.name = "dad"

	return [crew1,crew2]

def test_crew_adult():

	gene00 = Gene()
	gene00.locus = 0
	gene00.condition = "00" 
	gene00.condition_prob = 1
	gene00.congential = 1 #Congential = 0, Adult = 1
	gene00.dominant = True #Genes are either recessive or dominant. We Mendel for now
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
	crew1.set_name("01","crew")
	crew1.genome.append([gene00,gene01])

	crew2 = Crewmate()
	crew2.set_sex()
	crew2.set_name("02","crew")
	crew2.genome.append([gene01,gene01])

	crew1.mom = Crewmate()
	crew1.mom.name = "mom"
	crew1.dad = Crewmate()
	crew1.dad.name = "dad"

	crew2.mom = Crewmate()
	crew2.mom.name = "mom"
	crew2.dad = Crewmate()
	crew2.dad.name = "dad"

	return [crew1,crew2]

def test_ship():
	test = Ship()
	test.crew = import_crew()
	return test
