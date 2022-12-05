from time import *
import random

# -----------------------------------------------------------------------------------------------------------------------------------------
# Required
# -----------------------------------------------------------------------------------------------------------------------------------------

cooldown = 0

# Player variables
player_health = 100

# Enemy variables
ai_name = "Computer"
ai_health = 100

# Weapons
sword =["Sword", 24, 85, "Medium damage, fast."]
club = ["Club", 30, 70, "Medium-high damage, medium speed"]
bow = ["Bow", 20, 90, "Low-medium damage, very fast"]
dagger = ["Dagger", 15, 100, "Low damage, extremely fast - sure to hit"]
mace = ["Mace", 38, 60, "High damage, slow"]
fish = ["Massive trout", 46, 50, "Massive damage, very slow"]

elixir = ["Elixir of life", -30, 100, "Heals for a moderate amount of HP. Can only be used once every 3 player turns."]

weapons = [sword, bow, club, dagger, mace, fish] # For weapon choice

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def dmg_calc(self, wpn_stats, enemy):
        global cooldown
        global ai_name
        dmg_value = wpn_stats[1] =+ float(wpn_stats[1]*random.uniform(0.95, 1.3))
        print("dmgvalue: "+str(dmg_value))
        dmg_value = int(round(dmg_value))
        if random.randint(1, 100) <= wpn_stats[2]:
            if dmg_value > 0:
                print("\n"+enemy.name+" attacks with "+str(wpn_stats[0])+"!")
                self.health -= dmg_value
                print(self.name +" took "+str(dmg_value)+" damage and now has "+str(self.health)+" health left.")
                if enemy.name != ai_name:
                    #print("cooldown -1")
                    cooldown -= 1
            else:
                enemy.health -= dmg_value
                print("\n"+enemy.name+" used "+str(wpn_stats[0])+"!")
                print(enemy.name+" healed for "+str(-dmg_value)+". They now have "+str(enemy.health)+"!")
                if enemy.name != ai_name:
                    #print("#cooldown +3")
                    cooldown += 3
        else:
            print(enemy.name+" missed! No damage.")
            if enemy.name != ai_name:
                cooldown -= 1

    def wpn_choice(self, wp_list, elixir):
        global cooldown
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
        if cooldown == 0:
            print("4: "+elixir[0]+" - "+elixir[3])
        else:
            print("4: "+elixir[0]+" - On cooldown for another "+str(cooldown)+" rounds.")

        while True :
            wp_choice = input("Choice: ")
            #print("wpn choice = "+wp_choice)
            if wp_choice == "1":
                return wp1
            elif wp_choice == "2":
                return wp2
            elif wp_choice == "3":
                return wp3
            elif wp_choice == "4":
                if cooldown == 0:
                    return elixir
                else:
                    print("Can't use elixir for another "+str(cooldown)+" rounds.")
            else:
                print("Invalid input. Choose a number between 1 and 3.")

    def ai_turn(self):
        if random.randint(0, 5) == 0:
            return elixir
        else:
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
        print("--------------------------------------------")

    else: # If player is player lol
        print("\n"+player.name +" : "+str(player.health)+" HP")
        print(enemy.name +" : "+str(enemy.health)+" HP")
        print("\n"+player.name+"'s turn!\n")
        sleep(2)
        enemy.dmg_calc(player.wpn_choice(weapons, elixir), player)

# -----------------------------------------------------------------------------------------------------------------------------------------
# Startup
# -----------------------------------------------------------------------------------------------------------------------------------------

def game():
    plc = Player(input("What is your character called?: "), player_health)
    ai = Player(ai_name, ai_health)
    global cooldown

    # Round shuffling
    #round_count = 1
    print ("---- ! GAME START ! ----")
    while True:
        play_round(plc, ai)
        if ai.health <= 0:
            print("You won!")
            input()
            break
        if cooldown < 0:
            cooldown = 0
        #print(cooldown)

        play_round(ai, plc)
        if plc.health <= 0:
            print("You died.")
            input()
            break
        if cooldown < 0:
            cooldown = 0
        #print(cooldown)


print("Console Turn Based Fight\n")
sleep(1)
game()

