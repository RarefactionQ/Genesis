import random


class Gene(object):

    def __init__(self):
        self.locus = None
        self.condition = None
        self.condition_prob = None
        self.congential = None # Congential = 0, Adult = 1
        self.dominant = None # Genes are either recessive or dominant. We Mendel for now
        self.emp = 0
        self.int = 0
        self.cre = 0

    @staticmethod
    def get_dominant(pair):
        gene1 = pair[0]
        gene2 = pair[1]
        if gene1.locus != gene2.locus:
            print "Comparing different Gene loci!"
        if gene1.locus == None or gene2 == None:
            print "Uninitialized locus/loci gene1:" + str(gene1.locus) + " gene2:" + str(gene2.locus)
        if gene1.dominant:
            return gene1
        elif gene2.dominant:
            return gene2
        else:
            return gene1

    def improper_gene(self):
        return self.locus is None or self.condition_prob is None or self.congential is None

    def birth_effects(self, baby):
        if self.improper_gene():
            print "Tried to use an improper gene on a baby"
            return
        if int(self.congential) != 0:
            return
        if random.random() < self.condition_prob:
            baby.traits.append(self.condition)
            baby.empathy += int(self.emp)
            baby.intelligence += int(self.int)
            baby.creativity += int(self.cre)

    def adult_effects(self, adult):
        print "tried to adult_effects "+str(self.congential)
        if self.improper_gene():
            print "Tried to use an improper gene on a new adult"
            return
        if int(self.congential) != 1:
            return
        if random.random() < self.condition_prob:
            adult.traits.append(self.condition)
            adult.empathy += int(self.emp)
            adult.intelligence += int(self.int)
            adult.creativity += int(self.cre)
