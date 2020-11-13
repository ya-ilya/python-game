import time
import os
from random import randint
import colorama
from colorama import Fore, Back, Style
colorama.init()

name = "ya-ilya game"
ver = "beta 0.5"

savefiler = open("save.txt",'r',encoding = 'utf-8')
moneyfile = int(savefiler.read(1))
energyfile = int(savefiler.read(3))
healthfile = int(savefiler.read(5))
fishs = 0
money = moneyfile
level = 1
exp = 0
fact = 0
facttwo = 0
energy = energyfile
health = healthfile
itemud = 0
itemhare = 0
itemdeer = 0
itembird = 0
ud = 80
savefiler.close()

print("██╗░░░██╗░█████╗░░░░░░░██╗██╗░░░░░██╗░░░██╗░█████╗░\n╚██╗░██╔╝██╔══██╗░░░░░░██║██║░░░░░╚██╗░██╔╝██╔══██╗\n░╚████╔╝░███████║█████╗██║██║░░░░░░╚████╔╝░███████║\n░░╚██╔╝░░██╔══██║╚════╝██║██║░░░░░░░╚██╔╝░░██╔══██║\n░░░██║░░░██║░░██║░░░░░░██║███████╗░░░██║░░░██║░░██║\n░░░╚═╝░░░╚═╝░░╚═╝░░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝")
print("Welcome to " + name + " [" + ver + "]")
time.sleep(1.5)
print("| 1 - New Game")
print("| 2 - Credits [finishes the program]")
print("------------------------------------------------------------------")
selmain = int(input("> "))

if selmain == 1:
        print("| [SOON] Choose the difficulty\n| 1 - Normal")
        print("------------------------------------------------------------------")
        seldiff = 0
        seldiff = int(input("> "))
        if seldiff == 1:
                while 1:
                        try:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(Fore.GREEN + '| Money: ' + str(money) + Fore.YELLOW + ' | Energy: ' + str(energy) + Fore.RED + ' | Health: ' + str(health) + ' |' + Fore.RESET)
                                print("| Сhoose what you want to do")
                                print("| 1 - To go fishing\n| 2 - Go to work in a factory\n| 3 - Restore power\n| 4 - Go to the store\n| 5 - Inventory\n| 6 - Save game\n| 7 - Hunt ")
                                print("------------------------------------------------------------------")
                                seldey = 0
                                seldey = int(input("> "))
                                if seldey == 1:
                                        if energy > 6:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                print("| You started fishing")
                                                time.sleep(randint(0, 9))
                                                fishone = randint(0, 5)
                                                energy = energy - 3
                                                print("| You caught " + str(fishone) +" fish")
                                                time.sleep(randint(0, 9))
                                                fishtwo = randint(0, 4)
                                                energy = energy - 3
                                                print("| You caught " + str(fishtwo) + " more fish")
                                                fishs = fishone + fishtwo
                                                time.sleep(1.3)
                                                if itemud == 0:
                                                        fishmoney = fishs * randint(1, 3)
                                                elif itemud == 1:
                                                        fishmoney = fishs * randint(1, 6)
                                                print("| You managed to catch " + str(fishs) + " fish. You sold them for $ " + str(fishmoney))
                                                time.sleep(0.8)
                                                print("| You also spent 6 energy!")
                                                print("------------------------------------------------------------------")
                                                money = money + fishmoney
                                        elif energy < 6:
                                                print("| You have no energy! Sleep")
                                                print("------------------------------------------------------------------")
                                                time.sleep(5)
                                        invsel=int(input("| Exit?\n> "))
                                        print(invsel)
                                        if invsel != 56443:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                elif seldey == 2:
                                                if energy > 8:
                                                        os.system('cls' if os.name == 'nt' else 'clear')
                                                        print("| You came to work at the factory. There is a system of levels. The more levels the more you pay")
                                                        time.sleep(0.7)
                                                        a=int(input("| 1 - get started\n| Any number - cancel\n"))
                                                        if a != 1:
                                                                print("| You don't want to work in a factory anymore")
                                                        else:
                                                                print("| You started working in a factory")
                                                                time.sleep(0.2)
                                                                print("| Work...")
                                                                time.sleep(0.2)
                                                                print("| Work...")
                                                                time.sleep(0.2)
                                                                print("| Work...")
                                                                time.sleep(0.2)
                                                                print("| Finishing the job..")
                                                                time.sleep(1.0)
                                                                energy = energy - 4
                                                                if level == 1:
                                                                        exp = exp + randint(1, 2)
                                                                        facttwo = randint(3, 7)
                                                                        if exp > 30:
                                                                                level = level + 1
                                                                                print("| You got level 2 in the factory!")
                                                                elif level == 2:
                                                                        exp = exp + randint(2, 3)
                                                                        facttwo = randint(5, 10)
                                                                        if exp > 30:
                                                                                level = level + 1
                                                                                print("| You got level 3 in the factory!")
                                                                elif level == 3:
                                                                        facttwo == randint(7, 13)
                                                                print("| You have earned " + str(facttwo) + "$ so far")
                                                                print("------------------------------------------------------------------")
                                                                money = money + fact
                                                                time.sleep(0.9)
                                                        b=int(input("| 1 - get started\n| Any number - cancel\n"))
                                                        if b != 1:
                                                                print("| You don't want to work in a factory anymore")
                                                                time.sleep(0.8)
                                                        else:
                                                                print("| You continued to work in the factory. Keep it up!")
                                                                time.sleep(0.2)
                                                                print("| Work...")
                                                                time.sleep(0.2)
                                                                print("| Work...")
                                                                time.sleep(0.2)
                                                                print("| Work...")
                                                                time.sleep(0.2)
                                                                print("| Finishing the job..")
                                                                time.sleep(1.0)
                                                                energy = energy - 4
                                                                if level == 1:
                                                                        exp = exp + randint(1, 2)
                                                                        fact = randint(3, 7)
                                                                        if exp > 15:
                                                                                level = level + 1
                                                                                print("| You got level 2 in the factory!")
                                                                                exp = 0
                                                                        time.sleep(0.7)
                                                                elif level == 2:
                                                                        exp = exp + randint(2, 3)
                                                                        fact = randint(5, 10)
                                                                        if exp > 30:
                                                                                level = level + 1
                                                                                print("| You got level 3 in the factory!")
                                                                                exp = 0
                                                                        time.sleep(0.7)
                                                                elif level == 3:
                                                                        fact == randint(7, 13)
                                                                factmoneys = fact + facttwo
                                                                print("| You got another " + str(factmoneys) + "$ working in the factory")
                                                                print("| You also spent 8 energy!")
                                                                print("------------------------------------------------------------------")
                                                                invsel=int(input("| Exit?\n> "))
                                                                print(invsel)
                                                                if invsel != 56443:
                                                                        os.system('cls' if os.name == 'nt' else 'clear')
                                                                money = money + factmoneys
                                                                time.sleep(0.9)
                                                elif energy < 8:
                                                        print("| You have no energy! Sleep")
                                                        print("------------------------------------------------------------------")
                                                        time.sleep(5)
                                                        
                                elif seldey == 3:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        vop=int(input("| Are you sure this is what you want? This will take time\n| 1 - get started\n| Any number - cancel\n------------------------------------------------------------------\n> "))
                                        print(vop)
                                        if vop == 1:
                                                tempenergy = energy
                                                if tempenergy < 36:
                                                        energyint = randint(6, 17)
                                                        energy = energy + energyint
                                                        print("| You went to bed and started sleeping")
                                                        time.sleep(1)
                                                        print("------------------------------------------------------------------")
                                                        time.sleep(3)
                                                        print("| Good morning! Your energy has been restored by " + str(energyint) + "!")
                                                        time.sleep(1)
                                                        print("| Now you have " + str(energy) + " energy")
                                                        print("------------------------------------------------------------------")
                                                        time.sleep(2)
                                                        invsel=int(input("| Exit?\n> "))
                                                        print(invsel)
                                                        if invsel != 56443:
                                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                else:
                                                        print("| You have enough energy - " + energy)
                                elif seldey == 4:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        magsel=int(input("| You came to the store and were shown a list of products\n| 1 - fishing rod (gives you 2 times more money from fishin\n| Enter the number of the item you want to buy: "))
                                        print(magsel)
                                        if magsel == 1:
                                                if itemud != 0:
                                                        print("| You already have a fishing rod!")
                                                        print("------------------------------------------------------------------")
                                                        time.sleep(1)
                                                elif itemud == 0:
                                                        if money < ud:
                                                                print("| Fool! You don't have enough money to buy this")
                                                                print("------------------------------------------------------------------")
                                                        elif money > ud:
                                                                money = money - ud
                                                                itemud = 1
                                                                print("| You have successfully purchased a fishing rod for $80! Now your balance - " + str(money))
                                                                print("------------------------------------------------------------------")
                                                                time.sleep(1)
                                        invsel=int(input("| Exit?\n> "))
                                        print(invsel)
                                        if invsel != 56443:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                elif seldey == 5:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("| Your inventory:")
                                        if itemud == 0:
                                                print("| Fishing rods: is not available")
                                                time.sleep(1)
                                        elif itemud == 1:
                                                print("| Fishing rod: available")
                                                time.sleep(1)
                                        print("| You can buy items in the store")
                                        print("------------------------------------------------------------------")
                                        invsel=int(input("| Exit?\n> "))
                                        print(invsel)
                                        if invsel != 56443:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                elif seldey == 6:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("| The game is saved...")
                                        savefilew = open("save.txt",'w')
                                        savefilew.write(str(money) + '\n' + str(energy))
                                        savefilew.close()
                                        time.sleep(2)
                                        print("| The game has been saved!")
                                        invsel=int(input("| Exit?\n> "))
                                        print(invsel)
                                        if invsel != 56443:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                elif seldey == 7:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if energy > 6:
                                                huntsel=int(input("| Are you sure you want to go hunting? You might get killed\n| 1 - Yes\n| ENTER - No\n> "))
                                                print(huntsel)
                                                if huntsel == 1:
                                                        print("| You went hunting")
                                                        huntrand = randint(3, 12)
                                                        huntrandentity = randint(1, 3)
                                                        huntrandsn = randint (1, 3)
                                                        time.sleep(huntrand)
                                                        if huntrandentity == 1:
                                                                hunttargeone = "hare"
                                                        elif huntrandentity == 2:
                                                                hunttargeone = "deer"
                                                        elif huntrandentity == 3:
                                                                hunttargeone = "bird"
                                                        huntone=int(input("| Have you seen " + str(hunttargeone) + "\n| Shoot him?\n| 1 - Yes\n> "))
                                                        print(huntone)
                                                        if huntone == 1:
                                                                if huntrandsn == 1:
                                                                        if hunttargeone == "hare":
                                                                                print("| You have successfully shot a hare")
                                                                                if itemhare >= 4:
                                                                                        print("| You don't have room for this hare! Sell the rest in the store!")
                                                                                        time.sleep(2)
                                                                                else:
                                                                                        energy = energy - 3
                                                                                        itemhare = itemhare + 1
                                                                                        time.sleep(2)
                                                                        elif hunttargeone == "deer":
                                                                                print("| Wow! You shot a deer! Good loot")
                                                                                if itemdeer >= 2:
                                                                                        print("| Unfortunately, you can not carry this deer, you have no free space! You can free up space by selling items in the store!")
                                                                                        time.sleep(2)
                                                                                else:
                                                                                        itemdeer = itemdeer + 1
                                                                                        energy = energy - 5
                                                                                        time.sleep(2)
                                                                        elif hunttargeone == "bird":
                                                                                print("| You shot a little bird! So-so production")   
                                                                                itembird = itembird + 1
                                                                                energy = energy - 2
                                                                                time.sleep(2)            
                                                                elif huntrandsn == 2:
                                                                        if hunttargeone == "hare":
                                                                                print("| You missed the hare! Here's the failure")
                                                                                time.sleep(2)
                                                                        elif hunttargeone == "bird":
                                                                                print("| You missed the bird. Don't worry, you'll catch it again!")
                                                                                time.sleep(2)
                                                                        elif hunttargeone == "deer":
                                                                                print("| You missed the deer! I could have made a lot of money")
                                                                                time.sleep(2)
                                                                elif huntrandsn == 3:
                                                                        if hunttargeone == "hare":
                                                                                print("| You wounded the hare but it managed to escape!")
                                                                                time.sleep(2)
                                                                        elif hunttargeone == "bird":
                                                                                print("| You hit a bird but it managed to fly away")
                                                                                time.sleep(2)
                                                                        elif huntrandsn == "deer":
                                                                                if health < 10:
                                                                                        print("You hit a deer in the leg and it ran at you! You're dead...")
                                                                                        money = money - money / 2
                                                                                        energy = energy - energy / 2
                                                                                        health = 15
                                                                                        time.sleep(2)
                                                                                else:
                                                                                        health = health - 10
                                                                                        print("| you hit a deer in the leg and it ran at you! Your HP has dropped to " + str(health))
                                                                                        time.sleep(2)
                                        elif energy < 6:
                                                print("| You have no energy! Sleep")
                                                time.sleep(2)
                                        invsel=int(input("| Exit?\n> "))
                                        print(invsel)

                                                                
                        except ValueError:
                                print("")