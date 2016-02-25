from Ship import Ship
from Crewmate import Crewmate
import ui
import initial
import sys
from blessings import Terminal

def main():
	genesis = initial.test_ship()
	# while not (lose(genesis) or win(genesis))
	while True:
		decision_loop(genesis)

def get_stats(s):
	term = Terminal()
	stats = ""
	s.compute_all()
	stats += term.bold("Mission Year: "+str(s.mission_year)+"\n")
	stats += "Healthiness: "+term.magenta(str(s.healthiness))+", "
	stats += "Satisfaction: "+term.cyan(str(s.satisfaction))+", "
	stats += "Safety: "+term.blue(str(s.safety))+", "
	stats += "Projected Research: "+term.green(str(s.get_research_credits()))+", "
	stats += "\nEnergy Use: "+str(s.total_consumption)+" Remaining Fuel: "+str(s.fuel)
	stats += "Speed: "+str(s.speed)+" Distance: "+str(s.distance)
	return stats

def inspect_crew(s):
	print "inspect_crew"
def choose_research(s):
	print "choose_research"
def assign_job(s):
	print "assign_job"
def sterilize(s):
	print "sterilize"
def euthanize(s):
	print "euthanize"
def end_turn(s):
	print "end_turn"

def decision_loop(s):
	main_loop = ["Inspect Crew","Choose Research","Assign Job","Sterilize","Euthanize","End Turn"]
	answer = ui.list_options(main_loop,get_stats(s))
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

def lose(s):
	if s.fuel <= 0 or len(s.crew) == 0:
		print "You Lose!"
		sys.exit()


if __name__ == "__main__":
    main()