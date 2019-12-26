import random, time

times_run = ""      #Use String if you want user to choose
wizard_damage = []
fighter_damage = []
wizard_dict = {"Name":"Wizard", "Damage":[5,10], "Number of attacks":1, "Skill Mod":5, "Proficiency":6, "Empowered Evocation":5}
fighter_dict = {"Name":"Fighter", "Damage":[1,10], "Number of attacks":4, "Skill Mod":5, "Proficiency":6, "GW Fighting":True, "I/S Crit":True}

def user_setup():
    print("How u get here?")
    #User picks if attack rolls are share and number of attack rolls to calculate

def roll_attack():
    roll = random.randint(1, 20)
    return roll

def attack_crunch(details):
    
    attack = 0
    critical = False
    damage = 0
    
    for r in range(details["Number of attacks"]):
        attack = random.randint(1, 20)
        if attack + details["Skill Mod"] + details["Proficiency"] >= 15:
            if attack == 20 or "I/S Crit" in details and attack >= 18:
                print("Rolled a:", attack, "Thats a:", attack + details["Skill Mod"] + details["Proficiency"], "CRITICAL HIT from: ",details["Name"])
                critical = True
                damage = damage + damage_crunch(details, critical)
                critical = False
            else:
                print("Rolled a:",attack, "Thats a:", attack + details["Skill Mod"] + details["Proficiency"], "To hit! Not a crit with: ", details["Name"])
                damage = damage + damage_crunch(details, critical)

        
        else:
            print("Rolled a:", attack, "Thats a:", attack + details["Skill Mod"] + details["Proficiency"], "To hit! Miss from: ", details["Name"])
            damage =  damage + 0
    store_damage(details, damage)

        
def damage_crunch(details, critical):
    damage = 0
    number_of_dmg_dice = details["Damage"][0]
    if critical:
        number_of_dmg_dice = number_of_dmg_dice * 2
    for i in range(number_of_dmg_dice):
        damage_roll = random.randint(1,details["Damage"][1])
        if damage_roll <= 2 and "GW Fighting" in details:
            damage_reroll = random.randint(1, details["Damage"][1])
            if damage_reroll > damage_roll:
                damage_roll = damage_reroll              
        print (damage_roll, "damage rolled")
        damage = damage + damage_roll
        
    if details["Name"] != "Wizard":
        damage = damage + details["Skill Mod"]    
    if "Empowered Evocation" in details:
        damage = damage + details["Empowered Evocation"]
    print("total damage:", damage)
    return damage

def store_damage(details, damage):
    global wizard_damage, fighter_damage
    
    if details["Name"] == "Wizard":
        wizard_damage.append(damage)
    if details["Name"] == "Fighter":
        fighter_damage.append(damage)
    
    else:
        print("Class name unknown")
    
def average_damage(damage_list):
    total = 0
    for i in damage_list:
        total = total + i
    average = total / len(damage_list)
    return average
    
def setup():
    global times_run
    
    while times_run != int:
        times_run = input("Please entre the number of turns to test: ")
        try:
            times_run = int(times_run)
            print(times_run, "attacks will be calculated")
            time.sleep(2)
            break
        except:
            print("Sorry, please enter a whole number")    


if __name__ == "__main__":
    #attack_global = roll_attack()
    setup()
    for i in range(times_run):
        attack_crunch(wizard_dict)
        attack_crunch(fighter_dict)
    print(wizard_damage)
    print(fighter_damage)
    wizard_average = average_damage(wizard_damage)
    print("The average damage done by the Wizard with", times_run, "rounds is:", wizard_average)
    fighter_average = average_damage(fighter_damage)
    print("The average damage done by the Fighter with", times_run, "rounds is:", fighter_average)
    

"""
Wizard:
Firebolt = 5d10
INT +5
Proficiency +6
Empowered Evocation: add INT to damage rolls

Fighter:
Longsword = 1d10
Makes 4 attack rolls
STR +5
Proficiency +6
Great Weapon Fighting: Reroll 1&2 damage dice rolls once
Improved/Superior critical: Crits on 18-20 attack rolls

"""