from time import *
import random

# -----------------------------------------------------------------------------------------------------------------------------------------
# Required
# -----------------------------------------------------------------------------------------------------------------------------------------

# Player variables
player_health = 100

# Enemy variables
ai_name = "Computer"
ai_health = 100

# Weapons
sword =["Sword", 20, 85, "Medium damage, high speed."]
club = ["Club", 30, 70, "Medium-high damage, medium speed"]
bow = ["Bow", 18, 90, "Medium damage, very high speed"]

weapons = [sword, bow, club] # For weapon choice

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def dmg_calc(self, wp_stats, enemy):
        print(enemy.name+" used "+str(wp_stats[0])+"!")
        dmg_value = wp_stats[1] =+ float(wp_stats[1]*random.uniform(0.95, 1.3))
        dmg_value = int(round(dmg_value))
        if random.randint(0, 100) <= wp_stats[2]:
            self.health -= dmg_value
            print(self.name +" took "+str(dmg_value)+" damage!\n"+self.name+" now has "+str(self.health)+" health left.")
        else:
            print(enemy.name+" missed! No damage.")

    def ai_turn(self):
        return random.choice(weapons)

# -----------------------------------------------------------------------------------------------------------------------------------------
# Game system
# -----------------------------------------------------------------------------------------------------------------------------------------

def play_round(player, enemy):
    if player.name == ai_name: # If player is computer
        print("\n"+player.name+"'s turn!\n")
        print("You wait in anticipation for "+player.name+"'s attack.")
        enemy.dmg_calc(player.ai_turn(), player)

    else: # If player is player lol
        print("\n"+player.name+"'s turn!\n")
        print("Choose your weapon!")
        wp1 = random.choice(weapons)
        wp2 = random.choice(weapons)
        wp3 = random.choice(weapons)
        print("1: "+wp1[0]+" - "+wp1[3]+"\n2: "+wp2[0]+" - "+wp2[3]+"\n3: "+wp3[0]+" - "+wp3[3])

        wp_choice = input("Choice: ")
        if wp_choice == "1":
            enemy.dmg_calc(wp1, player)
        elif wp_choice == "2":
            #print(player.name+" used "+str(wp2[0])+"!")
            enemy.dmg_calc(wp2, player)
        elif wp_choice == "3":
            #print(player.name+" used "+str(wp3[0])+"!")
            enemy.dmg_calc(wp3, player)

# -----------------------------------------------------------------------------------------------------------------------------------------
# Startup
# -----------------------------------------------------------------------------------------------------------------------------------------

def game():
    plc = Player(input("What is your character called?: "), player_health)
    ai = Player(ai_name, ai_health)

    # Round shuffling
    round_count = 1
    print ("---- ROUND "+str(round_count)+" START! ----")
    while True:
        play_round(plc, ai)
        if ai.health <= 0:
            print("You won!")
            round_count += 1
            input()
            break
        
        play_round(ai, plc)
        if plc.health <= 0:
            print("You died.")
            round_count += 1
            input()
            break

print("Console Turn Based Fight v2.0\n")
sleep(1)
game()

