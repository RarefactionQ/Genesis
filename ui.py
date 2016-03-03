import os
from blessings import Terminal

def enter_full():
	term = Terminal()
	print term.enter_fullscreen

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def acknowledge():
	raw_input("Hit Return to Continue.")


def inline_print(crew):
	term = Terminal()
	return "ID: "+str(crew.crew_id)+" \""+crew.name+"\", Age: "+str(crew.age)+", Job: "+color_code(crew.job)+"("+term.red(str(crew.empathy))+", "+term.blue(str(crew.intelligence))+", "+term.yellow(str(crew.creativity))+")"

def full_info(crew):
	term = Terminal()
	print "Name: \""+crew.name+"\" id #:"+str(crew.crew_id)
	print term.red("Empathy: "+str(crew.empathy))+","+term.blue(" Intelligence: "+str(crew.intelligence))+","+term.yellow(" Creativity: "+str(crew.creativity))
	print "Age: "+str(crew.age)
	print "Adult: "+str(crew.adult)
	print "Sex: "+str(crew.sex)
	print "Job: "+color_code(crew.job)
	print "Dad: \""+str(crew.dad.name)+"\", Mom: \""+str(crew.mom.name)+"\""
	traits_str = ""
	for trait in crew.traits:
		if trait:
			traits_str += trait+", "
	print "Traits: "+traits_str
	# print "Full Genome: "
	# for gene in crew.genome:
	# 	print str(gene[0].locus)+": "+str(gene[0].condition)+", "+str(gene[1].condition)

def color_code(job):
	term = Terminal()
	if job == "Doctor":
		return term.magenta("Doctor")
	elif job == "Engineer":
		return term.blue("Engineer")
	elif job == "Researcher":
		return term.green("Researcher")
	elif job == "Artist":
		return term.cyan("Artist")
	elif job == "Laborer":
		return term.red_on_green("Laborer")
	else:
		return job

def pick_list_crew(crew):
	term = Terminal()
	# clear()
	fields = [0,0,0,0]
	for member in crew:
		if len(str(member.crew_id)) > fields[0]:
			fields[0] = len(str(member.crew_id))
		if len(member.name) > fields[1]:
			fields[1] = len(member.name)
		if len(str(member.age)) > fields[2]:
			fields[2] = len(str(member.age))
		if len(member.job) > fields[3]:
			fields[3] = len(member.job)
	answer = -1
	while not (str(answer).isdigit() and ((int(answer) > -1) and (int(answer) <= len(crew)))):
		clear()
		print "0: Back"
		i = 0
		for member in crew:
			i+=1
			s = ""
			s+=str(i)+": "
			s+= "ID: "+str(member.crew_id)
			for _ in range(fields[0] - len(str(member.crew_id))):
				s+=" "
			s+=" \""+member.name+"\","
			for _ in range(fields[1] - len(member.name)):
				s+=" "
			s+=" Age: "+str(member.age)+","
			for _ in range(fields[2] - len(str(member.age))):
				s+=" "
			s+= " Job: "+color_code(member.job)
			for _ in range(fields[3] - len(str(member.job))):
				s+=" "
			s+=" ("+term.red(str(member.empathy))+", "+term.blue(str(member.intelligence))+", "+term.yellow(str(member.creativity))+")"
			print s
		print "Please enter the number of the Crewmate to select them. Or 0 for back."
		answer = raw_input()

	return int(answer)-1

def list_options(options,header=None):
	answer = -1
	while not (str(answer).isdigit() and ((int(answer) > -1) and (int(answer) < len(options)))):
		clear()
		if header != None:
			print header
		i = 0
		for option in options:
			print str(i)+": "+option
			i+=1

		answer = raw_input("Please enter the number of the option you wish to select.")
	return int(answer)

# def inspect_crew():
# def choose_research():
# def assign_job()
# def sterilize():
# def euthanize():

