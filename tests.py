from Crewmate import Crewmate
from Gene import Gene
import initial
from Ship import Ship
import ui

def test_crew_id_increment():
    crew1 = Crewmate()
    crew2 = Crewmate()

    # print "crew1 "+str(crew1.get_id())+". crew2 "+str(crew2.get_id())
    if crew2.get_id() - crew1.get_id() != 1:
        print "Error, crew_id_increment broken"

def test_set_parents():
    crew1 = Crewmate()
    crew2 = Crewmate()
    crew3 = Crewmate()
    crew3.set_parents(crew1, crew2)
    if crew3.dad != crew1:
        print "Error, not the right dad"
    if crew3.mom != crew2:
        print "Error, not the right mom"

def test_get_set_attributes():
    crew1 = Crewmate()
    crew1.empathy = 5
    crew1.intelligence = 5
    crew1.creativity = 5
    if crew1.empathy != 5:
        print "Error, something is wrong with getting or setting empathy"
    if crew1.intelligence != 5:
        print "Error, something is wrong with getting or setting intelligence"
    if crew1.creativity != 5:
        print  "Error, something is wrong with getting or setting creativity"

def test_growing_up():
    crew1 = Crewmate()
    crew2 = Crewmate()

    crew1.age = 1
    crew1.grow_one_year()
    if crew1.age != 2:
        print "Error, problem growing one year to 2"
    if crew1.adult is not False:
        print "Error, infant is being reported as adult"

    crew2.age = 14
    crew2.grow_one_year()
    if crew2.age != 15:
        print "Error, problem growing one year to 15"
    if crew2.adult is not True:
        print "Error, adult is not being reported as such"

def test_sex():
    crew1 = Crewmate()
    crew2 = Crewmate()

    crew1.set_sex(Sex.Female)
    if crew1.sex != Sex.Female:
        print "Sex isn't able to be assigned manually"

    crew2.set_sex()
    if crew2.sex != Sex.Male and crew2.sex != Sex.Female:
        print "Sex isn't correctly assigned randomly"
        print crew2.sex

def test_naming():
    crew1 = Crewmate()
    crew2 = Crewmate()
    crew3 = Crewmate()

    crew1.set_name("foo", "bar") #remember, first name is last, last name is first
    if crew1.name != "bar foo":
        print "Error, name isn't being correctly set manually"
        print crew1.name+" should be bar foo"

    crew2.set_sex()
    crew2.set_name("bar")
    if "bar" not in crew2.name:
        print "Error, name isn't being set correctly when given just last name"
        print crew2.name+" should have last name bar"

    crew3.set_sex()
    crew3.set_name()
    if crew3.name == "Unnamed":
        print "Error, name isn't being set correctly when given no names"
        print crew3.name

def test_dominance():
    gene1 = Gene()
    gene2 = Gene()
    gene1.locus = 0
    gene2.locus = 0
    gene2.condition = "dom"
    gene2.dominant = True
    # Gene.get_dominant(gene1)
    pair = [gene1, gene2]
    if Gene.get_dominant(pair).condition != "dom":
        print "Error, dominant gene isn't working"

def test_birth_effects():
    crew = initial.test_crew_infant()
    Gene.get_dominant(crew[0].genome[0]).birth_effects(crew[0])
    Gene.get_dominant(crew[1].genome[0]).birth_effects(crew[1])
    if crew[0].empathy != 1:
        print "Birth effects incorrectly applied to dominant child"
    if crew[1].empathy != -1:
        print "Birth effects incorrectly applied to recessive child"

def test_adulthood_effects():
    crew = initial.test_crew_adult()
    Gene.get_dominant(crew[0].genome[0]).adult_effects(crew[0])
    Gene.get_dominant(crew[1].genome[0]).adult_effects(crew[1])
    if crew[0].empathy != 1:
        print "Adult effects incorrectly applied to dominant adult"
    if crew[1].empathy != -1:
        print "Adult effects incorrectly applied to recessive adult"

def test_gamete_generation():
    crew = initial.test_crew_adult()
    gamete = crew[1].get_gamete()
    if gamete[0].condition != "01":
        print "Impossible gene in gamete"

def test_inheriting_genome():
    crew = initial.test_crew_adult()
    child = Crewmate()
    child.set_parents(crew[0], crew[1])
    var0 = False
    var1 = False
    for _ in range(10):
        child.inherit()
        for gene in child.genome[0]:
            if gene.condition == "00":
                var0 = True
            if gene.condition == "01":
                var1 = True
    if not (var0 and var1):
        print "test_inheriting_genome failed"

def test_generate_child():
    crew = initial.test_crew_infant()
    # child = Crewmate()
    baby = Crewmate()
    baby.be_born(crew[0], crew[1])
    # ui.full_info(baby)
    if any_uninitialized(baby):
        print "test_generate_child failed"

def any_uninitialized(crew):
    return crew.name == "Unnamed" or crew.dad is None or crew.mom is None or crew.sex is None

def test_assign_job():
    crew = Crewmate()
    crew.job = "Tester"
    # crew.training = True
    crew.grow_one_year()
    # if crew.training == True:
        # print "test_assign_job failed"

# def test_sterilize():
# def test_dying():
# def test_random_mating():
# def test_assign_job():
# def test_computing_work():
# def test_ui():

def test_clear():
    print "foo"
    ui.clear()
    print "bar"

def test_crew_print():
    crew = initial.test_crew_infant()
    crew[0].job = "Researcher"
    print ui.inline_print(crew[0])
    ui.full_info(crew[1])

def test_fullscreen():
    ui.enter_full()

def test_acknowledge():
    ui.acknowledge()

def test_crew_pick():
    crew = initial.test_crew_infant()
    ui.pick_list_crew(crew)

def test_option_pick():
    options = ["Back", "First", "Second", "Third"]
    answer = ui.list_options(options)
    print options[answer]

def test_ship_constructor():
    Ship()

def test_ship_compute():
    ss_test = Ship()
    crew = initial.test_crew_adult()
    for member in crew:
        member.age = 14
        member.grow_one_year()
    crew[0].job = "Doctor"
    ss_test.crew = crew
    ss_test.compute_healthiness()
    if ss_test.healthiness != 0.1:
        print "test_ship_compute failed on Doctor"

    crew[0].job = "Artist"
    ss_test.crew = crew
    ss_test.compute_satisfaction()
    if ss_test.satisfaction != 0.1:
        print "test_ship_compute failed on Artist"

    crew[0].job = "Engineer"
    ss_test.crew = crew
    ss_test.compute_safety()
    if ss_test.safety == -1:
        print "test_ship_compute failed on Engineer"




def main():
    print "beginning tests"
    test_crew_id_increment()
    test_set_parents()
    test_get_set_attributes()
    test_growing_up()
    test_sex()
    test_naming()
    test_dominance()
    test_birth_effects()
    test_adulthood_effects()
    test_gamete_generation()
    test_inheriting_genome()
    test_generate_child()
    # test_acknowledge()
    # test_clear()
    # test_crew_print()
    # test_crew_pick()
    # test_fullscreen()
    # test_option_pick()
    test_ship_constructor()
    test_ship_compute()



if __name__ == "__main__":
    main()
