import os

from blessings import Terminal
from Jobs import Jobs

term = Terminal()

def enter_full():
    print term.enter_fullscreen

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def acknowledge():
    raw_input("Hit Return to Continue.")


def get_stats(s):
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

def inline_print(crew):
    return "ID: "+str(crew.crew_id)+" \""+crew.name+"\", Age: "+str(crew.age)+", Job: "+color_code(crew.job)+"("+term.red(str(crew.empathy))+", "+term.blue(str(crew.intelligence))+", "+term.yellow(str(crew.creativity))+")"

def full_info(crew):
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
    #     print str(gene[0].locus)+": "+str(gene[0].condition)+", "+str(gene[1].condition)

def job_color(job):
    if job == Jobs.Doctor:
        return term.magenta
    elif job == Jobs.Engineer:
        return term.blue
    elif job == Jobs.Researcher:
        return term.green
    elif job == Jobs.Artist:
        return term.cyan
    elif job == Jobs.Laborer:
        return term.red_on_green
    else:
        return lambda x: x

def color_code(job):
    return job_color(job)(job)

def pick_list_crew(crew):
    # clear()
    fields = [0, 0, 0, 0]
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
        for i, member in enumerate(crew):
            s = ""
            s += str(i+1)+": "
            s += "ID: "+str(member.crew_id)
            for _ in range(fields[0] - len(str(member.crew_id))):
                s += " "
            s += " \""+member.name+"\","
            for _ in range(fields[1] - len(member.name)):
                s += " "
            s += " Age: "+str(member.age)+","
            for _ in range(fields[2] - len(str(member.age))):
                s += " "
            s += " Job: "+(member.job)
            for _ in range(fields[3] - len(str(member.job))):
                s += " "
            s += " ("+term.red(str(member.empathy))+", "+term.blue(str(member.intelligence))+", "+term.yellow(str(member.creativity))+")"
            print s
        print "Please enter the number of the Crewmate to select them. Or 0 for back."
        answer = raw_input()

    return int(answer)-1

def list_options(options, header=None):
    answer = -1
    while not (str(answer).isdigit() and ((int(answer) > -1) and (int(answer) < len(options)))):
        clear()
        if header is not None:
            print header
        i = 0
        for option in options:
            print str(i)+": "+option
            i += 1

        answer = raw_input("Please enter the number of the option you wish to select.")
    return int(answer)

# def inspect_crew():
# def choose_research():
# def assign_job()
# def sterilize():
# def euthanize():
