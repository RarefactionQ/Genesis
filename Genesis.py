import sys

from blessings import Terminal
import initial
import ui


def main():
    genesis = initial.test_ship()
    while not (lose(genesis) or win(genesis)):
    # while True:
        decision_loop(genesis)

def get_stats(s):
    term = Terminal()
    stats = ""
    s.compute_all()
    stats += term.bold("Mission Year: "+str(s.mission_year)+"\n")
    stats += "Healthiness: "+term.magenta(str(s.healthiness))+", "
    stats += "Satisfaction: "+term.cyan(str(s.current_satisfaction))+", "
    stats += "Safety: "+term.blue(str(s.safety))+", "
    stats += "Projected Research: "+term.green(str(s.get_research_credits()))+", "
    stats += "Projected Satisfaction: "+term.cyan(str(s.satisfaction))+", "
    stats += "\nEnergy Use: "+str(s.total_consumption)+" Remaining Fuel: "+str(s.fuel)+", "
    stats += "Speed: "+str(s.speed)+" Distance: "+str(s.distance)
    return stats

def inspect_crew(s):
    answer = ui.pick_list_crew(s.crew)
    if answer == -1:
        return
    ui.full_info(s.crew[answer])

def choose_research(s):
    answer = ui.list_options(["Health", "Safety", "Art", "Research", "Engine"])
    s.priority = answer

def assign_job(s):
    mate = ui.pick_list_crew(s.crew)
    if mate == -1:
        return
    answer = ui.list_options([ui.color_code("Doctor"), ui.color_code("Engineer"), ui.color_code("Researcher"), ui.color_code("Artist"), ui.color_code("Laborer")], ui.inline_print(s.crew[mate]))
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
    answer = ui.pick_list_crew(s.crew)
    if answer == -1:
        return
    s.crew[answer].sterile = True
    s.happiness_penalty += 50
def euthanize(s):
    answer = ui.pick_list_crew(s.crew)
    if answer == -1:
        return
    s.crew[answer].alive = False
    s.crew.remove(s.crew[answer])
    s.happiness_penalty += 500

def end_turn(s):
    s.pass_turn()
    ui.acknowledge()

def decision_loop(s):
    main_loop = ["Inspect Crew", "Choose Research", "Assign Job", "Sterilize", "Euthanize", "End Turn"]
    answer = ui.list_options(main_loop, get_stats(s))
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
    ui.acknowledge()

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
