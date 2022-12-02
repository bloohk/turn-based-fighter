from time import *
import random

# -----------------------------------------------------------------------------------------------------------------------------------------
# Required
# -----------------------------------------------------------------------------------------------------------------------------------------

yesorno = False

# Player variables
player_health = 100

# Enemy variables
ai_name = "Computer"
ai_health = 100

# Weapons
sword =["Sword", 24, 85, "Medium damage, fast."]
club = ["Club", 30, 70, "Medium-high damage, medium speed"]
bow = ["Bow", 20, 90, "Low-Medium damage, very fast"]
dagger = ["Dagger", 15, 100, "Low damage, extremely fast - sure to hit"]
mace = ["Mace", 38, 60, "High damage, slow"]
fish = ["Massive trout", 45, 50, "Massive damage, very slow"]

weapons = [sword, bow, club, dagger, mace, fish] # For weapon choice

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def dmg_calc(self, wpn_stats, enemy):
        print("\n"+enemy.name+" used "+str(wpn_stats[0])+"!")
        dmg_value = wpn_stats[1] =+ float(wpn_stats[1]*random.uniform(0.9, 1.3))
        dmg_value = int(round(dmg_value))
        if random.randint(0, 100) <= wpn_stats[2]:
            self.health -= dmg_value
            print(self.name +" took "+str(dmg_value)+" damage!\n"+self.name+" now has "+str(self.health)+" health left.")
        else:
            print(enemy.name+" missed! No damage.")
        print("------------------------")

    def wpn_choice(self, wp_list):
        print("Choose your weapon!")
        wp1 = random.choice(wp_list)
        while True:
            wp2 = random.choice(wp_list)
            if wp2 != wp1:
                break
            else:
                pass
        while True:
            wp3 = random.choice(wp_list)
            if wp3 == wp1:
                pass
            elif wp3 == wp2:
                pass
            else:
                break

        print("1: "+wp1[0]+" - "+wp1[3]+"\n2: "+wp2[0]+" - "+wp2[3]+"\n3: "+wp3[0]+" - "+wp3[3])
        while True :
            wp_choice = input("Choice: ")
            if wp_choice == "1":
                return wp1
            elif wp_choice == "2":
                return wp2
            elif wp_choice == "3":
                return wp3
            else:
                print("Invalid input. Choose a number between 1 and 3.")

    def ai_turn(self):
        return random.choice(weapons)

# -----------------------------------------------------------------------------------------------------------------------------------------
# Game system
# -----------------------------------------------------------------------------------------------------------------------------------------

def play_round(player, enemy):
    if player.name == ai_name: # If player is computer
        print("\n"+player.name+"'s turn!\n")
        sleep(2)
        print("You wait in anticipation for "+player.name+"'s attack.")
        sleep(1.5)
        enemy.dmg_calc(player.ai_turn(), player)

    else: # If player is player lol
        print("\n"+player.name+"'s turn!\n")
        sleep(2)
        enemy.dmg_calc(player.wpn_choice(weapons), player)

# -----------------------------------------------------------------------------------------------------------------------------------------
# Startup
# -----------------------------------------------------------------------------------------------------------------------------------------

def game():
    plc = Player(input("What is your character called?: "), player_health)
    ai = Player(ai_name, ai_health)

    # Round shuffling
    round_count = 1
    print ("---- ! GAME START ! ----")
    while True:
        play_round(plc, ai)
        if ai.health <= 0:
            print("You won!")
            input()
            break
        round_count += 1

        play_round(ai, plc)
        if plc.health <= 0:
            print("You died.")
            input("")
            break
        round_count += 1


print("Console Turn Based Fight\n")
sleep(1)
game()

