import time 
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
test_weapon =["Sword", 20]
test_weapon2 = ["Club", 30]
weapons = [test_weapon] # For weapon choice


class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_dmg(self, dmg):
        self.health -= dmg
        print(self.name +" took "+str(dmg)+" damage!\n"+self.name+" now has "+str(self.health)+" health left.")

    def ai_turn(self):
        return random.choice(weapons)

# -----------------------------------------------------------------------------------------------------------------------------------------
# Game system
# -----------------------------------------------------------------------------------------------------------------------------------------

def play_round(player, enemy):
    if player.name == ai_name: # If player is computer
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+player.name+"'s turn!")
        enemy.take_dmg(player.ai_turn()[1])

    else: # If player is player lol
        print("\n"+player.name+"'s turn!")
        input()

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
        play_round(ai, plc)
        if plc.health <= 0:
            print("You died.")
            round_count += 1
            break

        play_round(plc, ai)
        if ai.health <= 0:
            print("You won!")
            round_count += 1
            break


print("Console Turn Based Fight v.1.0\n")
game()

