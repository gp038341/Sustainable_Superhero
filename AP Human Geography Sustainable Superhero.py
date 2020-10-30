import random
import time

#text animation
def printText(sentence):
    for char in sentence:
        print(char, end ='')
        time.sleep(.03)
    print()

def battle_lead():
    print()
    options = ["attack", "special"]
    player_health = 100
    enemy_health = 125
    print("Player health:", player_health)
    print("Enemy health:", enemy_health)
    print()
    battling = True
    while battling:
        print(options)
        player_choice = input("What would you like to do? >> ")    
        if player_choice in options: 
            damage = random.randint(10, 18)
            enemy_damage = random.randint(10, 18)
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

            if player_choice == "special":
                choice = input("You can only use your special once per battle. Are you sure? y / n >> ")
                if choice == "y":
                    damage = random.randint(1, 50)
                    enemy_damage = random.randint(8, 15)
                    enemy_health = enemy_health - damage
                    print("You dealt", damage)
                    print("Enemy Health:", enemy_health)
                    player_health = player_health - enemy_damage
                    print("Enemy dealt:", enemy_damage)
                    print("Player Health:", player_health)
                    options.remove("special")

                if enemy_health <= 0:
                    print("You won!")
                    battling = False
                
                if player_health <= 0:
                    print("You lose!")
                    battling = False



def battle_mercury():
    print()
    options = ["attack", "special"]
    player_health = 100
    enemy_health = 175
    print("Player health:", player_health)
    print("Enemy health:", enemy_health)
    print()
    battling = True
    while battling:
        print(options)
        player_choice = input("What would you like to do? >> ")    
        if player_choice in options: 
            damage = random.randint(10, 18)
            enemy_damage = random.randint(3, 8)
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

            if player_choice == "special":
                choice = input("You can only use your special once per battle. Are you sure? y / n >> ")
                if choice == "y":
                    damage = random.randint(1, 50)
                    enemy_damage = random.randint(8, 15)
                    enemy_health = enemy_health - damage
                    print("You dealt", damage)
                    print("Enemy Health:", enemy_health)
                    player_health = player_health - enemy_damage
                    print("Enemy dealt:", enemy_damage)
                    print("Player Health:", player_health)
                    options.remove("special")

                if enemy_health <= 0:
                    print("You won!")
                    battling = False
                
                if player_health <= 0:
                    print("You lose!")
                    battling = False


def battle_arsenic():
    print()
    options = ["attack", "special"]
    player_health = 100
    enemy_health = 100
    print("Player health:", player_health)
    print("Enemy health:", enemy_health)
    print()
    battling = True
    while battling:
        print(options)
        player_choice = input("What would you like to do? >> ")    
        if player_choice in options: 
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

            if player_choice == "special":
                choice = input("You can only use your special once per battle. Are you sure? y / n >> ")
                if choice == "y":
                    damage = random.randint(1, 50)
                    enemy_damage = random.randint(8, 15)
                    enemy_health = enemy_health - damage
                    print("You dealt", damage)
                    print("Enemy Health:", enemy_health)
                    player_health = player_health - enemy_damage
                    print("Enemy dealt:", enemy_damage)
                    print("Player Health:", player_health)
                    options.remove("special")
                    
                if enemy_health <= 0:
                    print("You won!")
                    battling = False
                
                if player_health <= 0:
                    print("You lose!")
                    battling = False
       
            
            #WORK ON THIS


print("Clean Water and Sanitation")
time.sleep(2)
printText("Your Name: Solvent")
time.sleep(0.5)
printText("Your powers: Shrinking, Flying, Purifying Water")
time.sleep(0.5)

printText("The world is in need of your help. In a world with over 320,000 different viruses, everybody needs clean water")
printText("Your mission: Travel around the world either purify or give people clean water.")
printText("There are 5 countries that are in the most need of clean water.")
printText("These countries are Somalia, Ethiopia, Uganda, Papua_New_Guinea, and Eritrea")
print()


#MAKE SURE THEY ONLY ARE ABLE TO SELECT EACH COUNTRY ONCE
countries = ["Somalia", "Ethiopia", "Uganda", "Papua_New_Guinea", "Eritrea"]
selecting = True
while selecting:
    print(countries)
    country_choice = input("Which country would you like to go to? >> ")
    if country_choice in countries:
        if country_choice == "Somalia":
            printText("You use your ability of flight to go to Somalia...")
            printText("You travel all the way to Africa to get to Somalia.")
            printText("60% lack basic water services here")
            time.sleep(.7)
            printText("What would you like to do?")
            printText("Answer 1, 2, or 3")
            choice = input("1: shrink to find out what is wrong with the water  2: go to a different country.  3: quit >> ")
            if choice == "1":
              printText("You use your shrinking powers to find out what is polluting the water in this area")
              time.sleep(.5)
              printText("You found the element arsenic in the water and must battle it to purify the water")
              time.sleep(.5)
              battle_arsenic()
              printText("Good work. You finished your work in Somalia. Now go help the other countries")
              countries.remove("Somalia")
            if choice == "2":
                print()

        elif country_choice == "Ethiopia":
            printText("You use your ability of flight to travel all the way to Africa to get to Ethiopia...")
            printText("60.9% lack basic water services here")
            time.sleep(.7)
            printText("What would you like to do?")
            printText("Answer 1, 2, or 3")
            choice = input("1: shrink to find out what is wrong with the water  2: go to a different country.  3: quit >> ")
            if choice == "1":
              printText("You use your shrinking powers to find out what is polluting the water in this area")
              time.sleep(.5)
              printText("You found the element arsenic in the water and must battle it to purify the water.")
              printText("There is more polluted water here so you will have to do 2 battles")
              time.sleep(.5)
              battle_arsenic()
              printText("Good work, now for the second battle")
              print()
              battle_arsenic()
              printText("Good work. You finished your work in Ethiopia. Now go help the other countries")
              countries.remove("Ethiopia")
            if choice == "2":
                print()


        elif country_choice == "Uganda":
            printText("You use your ability of flight to travel all the way to Africa to get to Uganda...")
            printText("61.1% lack basic water services here")
            time.sleep(.7)
            printText("What would you like to do?")
            printText("Answer 1, 2, or 3")
            choice = input("1: shrink to find out what is wrong with the water  2: go to a different country.  3: quit >> ")
            if choice == "1":
              printText("You use your shrinking powers to find out what is polluting the water in this area")
              time.sleep(.5)
              printText("You found the element mercury in the water and must battle it to purify the water.")
              time.sleep(.5)
              battle_mercury()
              printText("Good work. You finished your work in Uganda. Now go help the other countries")
              countries.remove("Uganda")
            if choice == "2":
                print()

        elif country_choice == "Papua_New_Guinea":
            printText("You use your ability of flight to travel all the way to Papua_New_Guinea...")
            printText("63.4% lack basic water services here")
            time.sleep(.7)
            printText("What would you like to do?")
            printText("Answer 1, 2, or 3")
            choice = input("1: shrink to find out what is wrong with the water  2: go to a different country.  3: quit >> ")
            if choice == "1":
              printText("You use your shrinking powers to find out what is polluting the water in this area")
              time.sleep(.5)
              printText("You found the element mercury in the water and must battle it to purify the water.")
              printText("There is more polluted water here so you will have to do 2 battles")
              time.sleep(.5)
              battle_mercury()
              printText("Good work, now for the second battle")
              print()
              battle_mercury()
              printText("Good work. You finished your work in Papua_New_Guinea. Now go help the other countries")
              countries.remove("Papua_New_Guinea")
            if choice == "2":
                print()


        elif country_choice == "Eritrea":
            printText("You use your ability of flight to travel all the way to Eritrea...")
            printText("80.7% lack basic water services here")
            time.sleep(.7)
            printText("What would you like to do?")
            printText("Answer 1, 2, or 3")
            choice = input("1: shrink to find out what is wrong with the water  2: go to a different country.  3: quit >> ")
            if choice == "1":
              printText("You use your shrinking powers to find out what is polluting the water in this area")
              time.sleep(.5)
              printText("You found the element lead in the water and must battle it to purify the water.")
              printText("This will be your hardest battle yet.")
              time.sleep(.5)
              battle_lead()
              printText("Good work. You finished your work in Eritrea.")
              countries.remove("Eritrea")
            if choice == "2":
                print()



        else:
            print("Try again. Make sure you enter the exact country. Example: Papua_New_Guinea")

    if countries == []:
        selecting = False
printText("Congradulations! You beat the game!")

