import time
import os
from random import randint

name = "ya-ilya game"
ver = "beta 0.1"

fishs = 0
money = 0
level = 1
exp = 0
fact = 0
facttwo = 0
energy = 20
itemud = 0
ud = 80

print("██╗░░░██╗░█████╗░░░░░░░██╗██╗░░░░░██╗░░░██╗░█████╗░\n╚██╗░██╔╝██╔══██╗░░░░░░██║██║░░░░░╚██╗░██╔╝██╔══██╗\n░╚████╔╝░███████║█████╗██║██║░░░░░░╚████╔╝░███████║\n░░╚██╔╝░░██╔══██║╚════╝██║██║░░░░░░░╚██╔╝░░██╔══██║\n░░░██║░░░██║░░██║░░░░░░██║███████╗░░░██║░░░██║░░██║\n░░░╚═╝░░░╚═╝░░╚═╝░░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝")
print("Welcome to " + name + " [" + ver + "]")
time.sleep(1.5)
print(" 1 - New Game")
print(" 2 - Credits [finishes the program]")
print("------------------------------------------------------------------------")
selmain = int(input("> "))

if selmain == 1:
        print("[SOON] Choose the difficulty\n 1 - Normal")
        print("------------------------------------------------------------------------")
        seldiff = 0
        seldiff = int(input("> "))
        if seldiff == 1:
                while 1:
                        try:
                                print("Сhoose what you want to do")
                                print("1 - To go fishing\n2 - Go to work in a factory\n3 - Stats\n4 - Restore power\n5 - Go to the store\n6 - Inventory ")
                                print("------------------------------------------------------------------------")
                                seldey = 0
                                seldey = int(input("> "))
                                if seldey == 1:
                                        if energy > 6:
                                                print("You started fishing")
                                                time.sleep(randint(0, 9))
                                                fishone = randint(0, 5)
                                                energy = energy - 3
                                                print("You caught " + str(fishone) +" fish")
                                                time.sleep(randint(0, 9))
                                                fishtwo = randint(0, 4)
                                                energy = energy - 3
                                                print("You caught " + str(fishtwo) + " more fish")
                                                fishs = fishone + fishtwo
                                                time.sleep(1.3)
                                                if itemud == 0:
                                                        fishmoney = fishs * randint(1, 3)
                                                elif itemud == 1:
                                                        fishmoney = fishs * randint(1, 6)
                                                print("You managed to catch " + str(fishs) + " fish. You sold them for $ " + str(fishmoney))
                                                time.sleep(0.8)
                                                print("You also spent 6 energy!")
                                                print("------------------------------------------------------------------------")
                                                money = money + fishmoney
                                                time.sleep(1.1)
                                        elif energy < 6:
                                                print("You have no energy! Sleep")
                                                print("------------------------------------------------------------------------")
                                                time.sleep(0.8)
                                elif seldey == 2:
                                                if energy > 8:
                                                        print("You came to work at the factory. There is a system of levels. The more levels the more you pay")
                                                        time.sleep(0.7)
                                                        a=int(input("1 - get started\nAny number - cancel\n"))
                                                        if a != 1:
                                                                print("You don't want to work in a factory anymore")
                                                        else:
                                                                print("You started working in a factory")
                                                                time.sleep(0.2)
                                                                print("Work...")
                                                                time.sleep(0.2)
                                                                print("Work...")
                                                                time.sleep(0.2)
                                                                print("Work...")
                                                                time.sleep(0.2)
                                                                print("Finishing the job..")
                                                                time.sleep(1.0)
                                                                energy = energy - 4
                                                                if level == 1:
                                                                        exp = exp + randint(1, 2)
                                                                        facttwo = randint(3, 7)
                                                                        if exp > 30:
                                                                                level = level + 1
                                                                                print("You got level 2 in the factory!")
                                                                elif level == 2:
                                                                        exp = exp + randint(2, 3)
                                                                        facttwo = randint(5, 10)
                                                                        if exp > 30:
                                                                                level = level + 1
                                                                                print("You got level 3 in the factory!")
                                                                elif level == 3:
                                                                        facttwo == randint(7, 13)
                                                                print("You have earned " + str(facttwo) + "$ so far")
                                                                print("------------------------------------------------------------------------")
                                                                money = money + fact
                                                                time.sleep(0.9)
                                                        b=int(input("1 - get started\nAny number - cancel\n"))
                                                        if b != 1:
                                                                print("You don't want to work in a factory anymore")
                                                                time.sleep(0.8)
                                                        else:
                                                                print("You continued to work in the factory. Keep it up!")
                                                                time.sleep(0.2)
                                                                print("Work...")
                                                                time.sleep(0.2)
                                                                print("Work...")
                                                                time.sleep(0.2)
                                                                print("Work...")
                                                                time.sleep(0.2)
                                                                print("Finishing the job..")
                                                                time.sleep(1.0)
                                                                energy = energy - 4
                                                                if level == 1:
                                                                        exp = exp + randint(1, 2)
                                                                        fact = randint(3, 7)
                                                                        if exp > 15:
                                                                                level = level + 1
                                                                                print("You got level 2 in the factory!")
                                                                                exp = 0
                                                                        time.sleep(0.7)
                                                                elif level == 2:
                                                                        exp = exp + randint(2, 3)
                                                                        fact = randint(5, 10)
                                                                        if exp > 30:
                                                                                level = level + 1
                                                                                print("You got level 3 in the factory!")
                                                                                exp = 0
                                                                        time.sleep(0.7)
                                                                elif level == 3:
                                                                        fact == randint(7, 13)
                                                                factmoneys = fact + facttwo
                                                                print("You got another " + str(factmoneys) + "$ working in the factory")
                                                                print("You also spent 8 energy!")
                                                                print("------------------------------------------------------------------------")
                                                                money = money + factmoneys
                                                                time.sleep(0.9)
                                                elif energy < 8:
                                                        print("You have no energy! Sleep")
                                                        print("------------------------------------------------------------------------")
                                                        time.sleep(0.8)
                                                        
                                                        
                                elif seldey == 3:
                                        print("You have " + str(money) + "$")
                                        print("Energy you have - " + str(energy))
                                        print("--------------------------------")
                                        time.sleep(1.0)
                                elif seldey == 4:
                                        vop=int(input("Are you sure this is what you want? This will take time\n1 - get started\nAny number - cancel\n"))
                                        print(vop)
                                        if vop == 1:
                                                tempenergy = energy
                                                if tempenergy < 36:
                                                        energyint = randint(6, 17)
                                                        energy = energy + energyint
                                                        print("You went to bed and started sleeping")
                                                        time.sleep(1)
                                                        print("💤💤💤")
                                                        print("------------------------------------------------------------------------")
                                                        time.sleep(3)
                                                        print("Good morning! Your energy has been restored by " + str(energyint) + "!")
                                                        time.sleep(1)
                                                        print("Now you have " + str(energy) + " energy")
                                                        print("------------------------------------------------------------------------")
                                                        time.sleep(2)
                                                else:
                                                        print("You have enough energy - " + energy)
                                elif seldey == 5:
                                        magsel=int(input("You came to the store and were shown a list of products\n1 - fishing rod (gives you 2 times more money from fishing)\n2 - exit"))
                                        print(magsel)
                                        if magsel == 1:
                                                if itemud != 0:
                                                        print("You already have a fishing rod!")
                                                        time.sleep(1)
                                                elif itemud == 0:
                                                        if money < ud:
                                                                print("Fool! You don't have enough money to buy this")
                                                                time.sleep(1)
                                                        elif money > ud:
                                                                money = money - ud
                                                                itemud = 1
                                                                print("You have successfully purchased a fishing rod for $80! Now your balance - " + str(money))
                                                                time.sleep(1)
                                elif seldey == 6:
                                        print("Your inventory:")
                                        if itemud == 0:
                                                print("Fishing rods: is not available")
                                                time.sleep(1)
                                        elif itemud == 1:
                                                print("Fishing rod: available")
                                                time.sleep(1)
                                        print("You can buy items in the store")
                                        print("------------------------------------------------------------------------")
                                        time.sleep(1)
                        except ValueError:
                                print("")
elif selmain == 2:
        print("2020. Author ya-ilya. https://github.com/ya-ilya")
