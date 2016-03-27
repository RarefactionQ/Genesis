import sys

from Enum import Enum
import Initial
from Jobs import Jobs
import UI
from Quest import Quest

quest_list = []
def main():
    genesis = Initial.test_ship()
    for mate in genesis.crew:
        mate.job = "Laborer"
    while not (lose(genesis) or win(genesis)):
    # while True:
        decision_loop(genesis)

def inspect_crew(s):
    answer = UI.pick_list_crew(s.crew)
    if answer == -1:
        return
    UI.full_info(s.crew[answer])

Research = Enum(['Health', 'Safety', 'Art', 'Research', 'Engine'])

def choose_research(s):
    answer = UI.list_options(Research)
    s.priority = answer

def assign_job(s):
    mate = UI.pick_list_crew(s.crew)
    if mate == -1:
        return
    colorful_jobs = map(UI.color_code, Jobs)
    for quest in quest_list:
        colorful_jobs.append(quest.description+" "+str(quest.quest_id))
    job = UI.list_options(colorful_jobs, UI.inline_print(s.crew[mate]))
    if job < len(Jobs):
        s.crew[mate].job = Jobs[job]
    else:
        print job
        index = job - len(Jobs)
        print str(len(Jobs))
        s.crew[mate].job = quest_list[index].description+" "+str(quest_list[index].quest_id)

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
    for quest in quest_list:
        quest.apply_work(s)
        if quest.succeed():
            quest.victory(s)
            quest_list.remove(quest)
        else:
            quest.failure(s)
    new_quest = Initial.get_random_quest()
    UI.acknowledge()
    print new_quest.intro
    quest_list.append(new_quest)
    s.pass_turn()
    UI.acknowledge()

def decision_loop(s):
    main_loop = ["Inspect Crew", "Choose Research", "Assign Job", "Sterilize", "Euthanize", "End Turn"]
    quest_status = ""
    for quest in quest_list:
        quest_status+="\n"+quest.description+", projected work: "+str(quest.count_work(s))+"/"+str(quest.cost)
    answer = UI.list_options(main_loop, header=str(UI.get_stats(s)+quest_status))
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
