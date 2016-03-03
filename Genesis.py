import sys

from Enum import Enum
import Initial
import UI


def main():
    genesis = Initial.test_ship()
    while not (lose(genesis) or win(genesis)):
    # while True:
        decision_loop(genesis)

def inspect_crew(s):
    answer = UI.pick_list_crew(s.crew)
    if answer == -1:
        return
    UI.full_info(s.crew[answer])

Research = Enum(["Health", "Safety", "Art", "Research", "Engine"])

def choose_research(s):
    answer = UI.list_options(Research)
    s.priority = answer

Jobs = Enum([UI.color_code("Doctor"), UI.color_code("Engineer"), UI.color_code("Researcher"), UI.color_code("Artist"), UI.color_code("Laborer")])

def assign_job(s):
    mate = UI.pick_list_crew(s.crew)
    if mate == -1:
        return
    answer = UI.list_options(Jobs, UI.inline_print(s.crew[mate]))
    if answer == 0:
        s.crew[mate].job = "Doctor"
    elif answer == 1:
        s.crew[mate].job = "Engineer"
    elif answer == 2:
        s.crew[mate].job = "Researcher"
    elif answer == 3:
        s.crew[mate].job = "Artist"
    elif answer == 4:
        s.crew[mate].job = "Laborer"
def sterilize(s):
    answer = UI.pick_list_crew(s.crew)
    if answer == -1:
        return
    s.crew[answer].sterile = True
    s.happiness_penalty += 50
def euthanize(s):
    answer = UI.pick_list_crew(s.crew)
    if answer == -1:
        return
    s.crew[answer].alive = False
    s.crew.remove(s.crew[answer])
    s.happiness_penalty += 500

def end_turn(s):
    s.pass_turn()
    UI.acknowledge()

def decision_loop(s):
    main_loop = ["Inspect Crew", "Choose Research", "Assign Job", "Sterilize", "Euthanize", "End Turn"]
    answer = UI.list_options(main_loop, header=UI.get_stats(s))
    if answer == 0:
        inspect_crew(s)
    elif answer == 1:
        choose_research(s)
    elif answer == 2:
        assign_job(s)
    elif answer == 3:
        sterilize(s)
    elif answer == 4:
        euthanize(s)
    elif answer == 5:
        end_turn(s)
    UI.acknowledge()

def win(s):
    if s.distance <= 0:
        print "You Win!"
        sys.exit()
    return False

def lose(s):
    if s.fuel <= 0 or len(s.crew) == 0:
        print "You Lose!"
        sys.exit()
    return False


if __name__ == "__main__":
    main()
