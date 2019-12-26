import random
hits_f = 0
hits_l = 0
test = []
#Wizard

def wizard_attack_roll():
    global hits_f
    attack_roll = random.randint(1,20)
    if attack_roll == 20:
        critical = True
    if attack_roll + 5 + 6 >= 15: # +5 INT and +6 Proficiency
        print("It's a HIT!")
        hits_f = hits_f +1
    
    
    return attack_roll
    
    
if __name__ == "__main__":
    for each in range(20):
        test.append(wizard_attack_roll())
    for i in test:
        if i >= 15:
            hits_l = hits_l + 1
    print(hits_f)
    print(hits_l)            
    print(test)


"""
Wizard:
Firebolt = 5d10
INT +5
Proficiency +6
Empowered Evocation: add INT to damage rolls

Fighter:
Longsword = 1d10
STR +5
Proficiency +6
Great Weapon Fighting: Reroll 1&2 damage dice rolls once
Makes 4 attack rolls
Improved/Superior critical: Crits on 18-20 attack rolls

"""