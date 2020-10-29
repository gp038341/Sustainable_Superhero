import random
import time

#text animation
def printText(sentence):
    for char in sentence:
        print(char, end ='')
        time.sleep(.03)
    print()

def battle_arsenic():
    player_health = 100
    enemy_health = 85
    print("You found the molecule arsenic in the water")
    print("Player health:", player_health)
    print("Enemy health:", enemy_health)
    print()
    battling = True
    while battling:
        print("What would you like to do?")
        player_choice = input("attack, run, special >> ")
        damage = random.randint(10, 18)
        enemy_damage = random.randint(8, 15)
        if player_choice == "attack":
            enemy_health = enemy_health - damage
            print("You dealt", damage)
            print("Enemy Health:", enemy_health)
            player_health = player_health - enemy_damage
            print("Enemy dealt:", enemy_damage)
            print("Player Health:", player_health)
            
        if enemy_health <= 0:
            print("You won!")
            battling = False
            
        if player_health <= 0:
            print("You lose!")
            battling = False
            #Work On This
            
        if player_choice == "run":
            got_away = random.randint(1, 15)
            if got_away == 1:
                print("Couldn't get away!")
            else:
                print("Got away safely")
                battling = False

        if player_choice == "special":
            print("your special move will deal from 1 to 50 damage")
            damage == random.randint(1, 50)
            #WORK ON THIS


print("Clean Water and Sanitation")
time.sleep(.700)

printText("The world is in need of your help. In a world with over 320,000 different viruses, everybody needs clean water")
printText("Your mission: Travel around the world either purify or give people clean water.")
printText("There 5 countries that are in the most need of clean water.")
printText("These countries are Somalia, Ethiopia, Uganda, Papua_New_Guinea, and Eritrea")


#MAKE SURE THEY ONLY ARE ABLE TO SELECT EACH COUNTRY ONCE
countries = ["Somalia", "Ethiopia", "Uganda", "Papua_New_Guinea", "Eritrea"]
selecting = True
while selecting:
    print(countries)
    country_choice = input("Which country would you like to go to? >> ")
    if country_choice == "Somalia":
        printText("You use your ability of flight to go to Somalia...")
        printText("You travel all the way to Africa to get to Somalia.")
        printText("60% lack basic water services here")
        printText("You use your shrinking powers to find out what is polluting the water in this area")
        battle_arsenic()
        printText("Good work. You finished your work in Somalia. Now go help the other 4 countries")
        countries.remove("Somalia")
        




        
 
    elif country_choice == "Ethiopia":
        print("Going to Ethiopia...")

    elif country_choice == "Uganda":
        print("Going to Uganda...")

    elif country_choice == "Papua_New_Guinea":
        print("Going to Papua New Guinea...")

    elif country_choice == "Eritrea":
        print("Going to Eritrea...")

    else:
        print("Try again. Make sure you enter the exact country. Example: Papua_New_Guinea")
    

