import time
import os
from random import randint
import colorama
from colorama import Fore, Back, Style
colorama.init()
from inputimeout import inputimeout, TimeoutOccurred

name = "ya-ilya game"
ver = "second pre-release 1.0"

savefiler = open("save.txt",'r',encoding = 'utf-8')
money = int(savefiler.readline())
energy = int(savefiler.readline())
health = int(savefiler.readline())
itemfirstaidkit = int(savefiler.readline())
itemud = int(savefiler.readline())
itemhare = int(savefiler.readline())
itemdeer = int(savefiler.readline())
itembird = int(savefiler.readline())
level = int(savefiler.readline())
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
        seldiff = int(input("> "))
        if seldiff == 1:
                while 1:
                        try:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(Fore.GREEN + '| Money: ' + str(money) + Fore.YELLOW + ' | Energy: ' + str(energy) + Fore.RED + ' | Health: ' + str(health) + ' |' + Fore.RESET)
                                print("| Сhoose what you want to do")
                                print("| 1 - To go fishing\n| 2 - Go to work in a factory\n| 3 - Restore power\n| 4 - Go to the store\n| 5 - Inventory\n| 6 - Save game\n| 7 - Hunt\n| 8 - Exit")
                                print("------------------------------------------------------------------")
                                seldey = 0
                                seldey = int(input("> "))
                                if seldey == 1:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        fishrandsn = randint(1, 3)
                                        fishrandsntwo = randint(1, 3)
                                        fishs = 0
                                        if energy > 6:
                                                print("| You started fishing")
                                                time.sleep(randint(0, 9))
                                                try:
                                                        something = inputimeout(prompt="| You will see that there are fish in the net!\n| 1 - Pull out the grid\n> ", timeout=3)
                                                        if fishrandsn == 1:
                                                                fishs = randint(0, 5)
                                                                print("| You have successfully taken all the fish from the net")
                                                                time.sleep(1)
                                                        elif fishrandsn == 2:
                                                                print("| You slipped and fell into the sea, and the fish were released from the net")
                                                                health -= 2
                                                                time.sleep(1)
                                                        elif fishrandsn == 3:
                                                                print("| hmm.. You have come to the net and was there was nothing there! What's wrong with you")
                                                                time.sleep(1)
                                                        print("------------------------------------------------------------------")
                                                        time.sleep(randint(2, 9))
                                                except TimeoutOccurred:
                                                        something = "| You didn't have time to pull the fish out! ("
                                                        print(something)
                                                try:
                                                        something = inputimeout(prompt="| You will see that another fish is biting!\n| 1 - Try to catch\n> ", timeout=3)
                                                        if fishrandsntwo == 1:
                                                                fishs = fishs + randint(0, 4)
                                                                print("| You have successfully taken all the fish from the net")
                                                                time.sleep(1)
                                                        elif fishrandsntwo == 2:
                                                                print("| You slipped and fell into the sea, and the fish were released from the net")
                                                                health = health - 2
                                                                time.sleep(1)
                                                        elif fishrandsntwo == 3:
                                                                print("| hmm.. You have come to the net and was there was nothing there! What's wrong with you")
                                                                time.sleep(1)
                                                        energy = energy - 6
                                                        time.sleep(1.3)
                                                        if itemud == 0:
                                                                fishmoney = fishs * randint(1, 3)
                                                        elif itemud == 1:
                                                                fishmoney = fishs * randint(1, 6)
                                                        if fishs == 0:
                                                                print("| Unfortunately, you didn't catch anything")
                                                        else:
                                                                print("| You managed to catch " + str(fishs) + " fish. You sold them for $ " + str(fishmoney))
                                                        time.sleep(0.8)
                                                        print("| You also spent 6 energy!")
                                                        print("------------------------------------------------------------------")
                                                        money += fishmoney
                                                except TimeoutOccurred:
                                                        something = "| You didn't have time to pull out the second fish! ("
                                                        print(something)
                                        elif energy < 6:
                                                print("| You have no energy! Sleep")
                                                print("------------------------------------------------------------------")
                                        invsel=int(input("| Exit?\n> "))
                                        print(invsel)
                                        if invsel != None:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                elif seldey == 2:
                                                if energy > 8:
                                                        exp = 0
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
                                                                if level == 1:
                                                                        exp += randint(1, 2)
                                                                        facttwo = randint(3, 7)
                                                                        if exp > 30:
                                                                                level += 1
                                                                                print("| You got level 2 in the factory!")
                                                                elif level == 2:
                                                                        exp += randint(2, 3)
                                                                        facttwo = randint(5, 10)
                                                                        if exp > 30:
                                                                                level += 1
                                                                                print("| You got level 3 in the factory!")
                                                                elif level == 3:
                                                                        facttwo == randint(7, 13)
                                                                print("| You have earned " + str(facttwo) + "$ so far")
                                                                print("------------------------------------------------------------------")
                                                                energy -= 4
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
                                                                if level == 1:
                                                                        exp += randint(1, 2)
                                                                        fact = randint(3, 7)
                                                                        if exp > 15:
                                                                                level += 1
                                                                                print("| You got level 2 in the factory!")
                                                                                exp = 0
                                                                        time.sleep(0.7)
                                                                elif level == 2:
                                                                        exp += randint(2, 3)
                                                                        fact = randint(5, 10)
                                                                        if exp > 30:
                                                                                level += 1
                                                                                print("| You got level 3 in the factory!")
                                                                                exp = 0
                                                                        time.sleep(0.7)
                                                                elif level == 3:
                                                                        fact == randint(7, 13)
                                                                energy -= 4
                                                                factmoneys = fact + facttwo
                                                                money += factmoneys
                                                                print("| You got another " + str(factmoneys) + "$ working in the factory\n| You have " + str(level) + " level")
                                                                print("| You also spent 8 energy!")
                                                                print("------------------------------------------------------------------")
                                                                invsel=int(input("| Exit?\n> "))
                                                                print(invsel)
                                                                if invsel != None:
                                                                        os.system('cls' if os.name == 'nt' else 'clear')
                                                                money += factmoneys
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
                                                        energy += energyint
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
                                                        if invsel != None:
                                                                os.system('cls' if os.name == 'nt' else 'clear')
                                                else:
                                                        print("| You have enough energy - " + energy)
                                elif seldey == 4:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        magsel=int(input("| You came to the store and were shown a list of products\n| 1 - fishing rod (gives you 2 times more money from fishin - 80$\n| 2 - to sell rabbits\n| 3 - sell deer\n| 4 - to sell birds\n| 5 - buy first aid kit - 20$\n Enter the number of the product you want to sell or buy: "))
                                        print(magsel)
                                        if magsel == 1:
                                                if itemud != 0:
                                                        print("| You already have a fishing rod!")
                                                        print("------------------------------------------------------------------")
                                                        time.sleep(1)
                                                elif itemud == 0:
                                                        if money < 80:
                                                                print("| Fool! You don't have enough money to buy this")
                                                                print("------------------------------------------------------------------")
                                                        elif money > 80:
                                                                money -= 80
                                                                itemud = 1
                                                                print("| You have successfully purchased a fishing rod for $80! Now your balance - " + str(money))
                                                                print("------------------------------------------------------------------")
                                                                time.sleep(1)
                                        elif magsel == 2:
                                                if itemhare != 0:
                                                        haremoney = itemhare * 7
                                                        itemhare = 0
                                                        print("| You have successfully sold all the hares and received " + str(haremoney))
                                                        money += haremoney
                                                        time.sleep(1)
                                                elif itemhare == 0:
                                                        print("| You don't have any hares in your inventory")
                                                        time.sleep(1)
                                        elif magsel == 3:
                                                if itemdeer != 0:
                                                        deermoney = itemdeer * 12
                                                        itemdeer = 0
                                                        print("| You sold all the deer and got " + str(deermoney))
                                                        money += deermoney
                                                        time.sleep(1)
                                                elif itemhare == 0:
                                                        print("| You don't have any deer in your inventory")
                                                        time.sleep(1)
                                        elif magsel == 4:
                                                if itembird != 0:
                                                        birdmoney = itemdeer * 4
                                                        itembird = 0
                                                        print("| You sold all the birds for " + str(birdmoney))
                                                        money += birdmoney
                                                        time.sleep(1)
                                                elif itembird == 0:
                                                        print("| You don't have any birds in your inventory")
                                                        time.sleep(1)
                                        elif magsel == 5:
                                                if money >= 20:
                                                        if itemfirstaidkit < 5:
                                                                print("| you have successfully purchased a first aid kit")
                                                                money -= 20
                                                                itemfirstaidkit = itemfirstaidkit + 1
                                                                time.sleep(1)
                                                        elif itemfirstaidkit >= 5:
                                                                print("you have more than 5 first aid kits! where do you want so much?")
                                                                time.sleep(1)
                                                if money < 20:
                                                        print("| You don't have enough money! you need to have 20$ to buy this")
                                        invsel=int(input("| Exit?\n> "))
                                        print(invsel)
                                        if invsel != None:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                elif seldey == 5:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("| Your inventory:")
                                        if itemud == 0:
                                                time.sleep(1)
                                        elif itemud == 1:
                                                print("| Fishing rod: available")
                                        if itemhare == 0:
                                                time.sleep(1)
                                        elif itemhare != 0:
                                                print("| Hare: " + str(itemhare))
                                        if itembird == 0:
                                                time.sleep(1)
                                        elif itembird != 0:
                                                print("| Birds: " + str(itembird))
                                        if itemdeer == 0:
                                                time.sleep(1)
                                        elif itemdeer != 0:
                                                print("| Deers: " + str(itemdeer))
                                        if itemfirstaidkit == 0:
                                                faktext = "| ENTER - Exit\n> "
                                                time.sleep(1)
                                        elif itemfirstaidkit != 0:
                                                faktext = "| 1 - Apply first aid kit | ENTER - Exit\n> "
                                                print("| First aid kits: " + str(itemfirstaidkit))
                                        print("| You can buy items in the store")
                                        print("------------------------------------------------------------------")
                                        invsel=int(input(faktext))
                                        print(invsel)
                                        if invsel == 1:
                                                if itemfirstaidkit >= 1:
                                                        if health >= 20:
                                                                print("| You have enough HP already!")
                                                                time.sleep(1)
                                                        elif health < 20:
                                                                fakrand = randint(5, 20)
                                                                print("| First aid kit successfully applied! You added " + str(fakrand))
                                                                health += fakrand
                                                                itemfirstaidkit -= 1
                                                                time.sleep(1)
                                                elif itemfirstaidkit < 1:
                                                        print("| You don't have any first aid kits! You can buy them in the store")
                                                        time.sleep(1)
                                        elif invsel != None:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                elif seldey == 6:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("| The game is saved...")
                                        savefilew = open("save.txt",'w')
                                        savefilew.write(str(money) + '\n' + str(energy) + '\n' + str(health) + '\n' + str(itemfirstaidkit) + "\n" + str(itemud) + "\n" + str(itemhare) + "\n" + str(itemdeer) + "\n" + str(itembird) + "\n" + str(level))
                                        savefilew.close()
                                        time.sleep(2)
                                        print("| The game has been saved!")
                                        invsel=int(input("| Exit?\n> "))
                                        print(invsel)
                                        if invsel != None:
                                                os.system('cls' if os.name == 'nt' else 'clear')
                                elif seldey == 7:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        if energy > 6:
                                                huntsel=int(input("| Are you sure you want to go hunting? You might get killed\n| 1 - Yes\n| ENTER - No\n> "))
                                                print(huntsel)
                                                if huntsel == 1:
                                                        print("| You went hunting")
                                                        huntrand = randint(3, 8)
                                                        huntrandentity = randint(1, 3)
                                                        huntrandsn = randint (1, 3)
                                                        time.sleep(huntrand)
                                                        if huntrandentity == 1:
                                                                hunttargeone = "hare"
                                                        elif huntrandentity == 2:
                                                                hunttargeone = "deer"
                                                        elif huntrandentity == 3:
                                                                hunttargeone = "bird"
                                                        try:
                                                                something = inputimeout(prompt="| Have you seen " + str(hunttargeone) + "\n| Shoot him?\n| 1 - Yes\n> ", timeout=3)
                                                                if huntrandsn == 1:
                                                                        if hunttargeone == "hare":
                                                                                print("| You have successfully shot a hare")
                                                                                if itemhare >= 4:
                                                                                        print("| You don't have room for this hare! Sell the rest in the store!")
                                                                                        time.sleep(2)
                                                                                else:
                                                                                        energy -= 3
                                                                                        itemhare += 1
                                                                                        time.sleep(2)
                                                                        elif hunttargeone == "deer":
                                                                                print("| Wow! You shot a deer! Good loot")
                                                                                if itemdeer >= 2:
                                                                                        print("| Unfortunately, you can not carry this deer, you have no free space! You can free up space by selling items in the store!")
                                                                                        time.sleep(2)
                                                                                else:
                                                                                        itemdeer += 1
                                                                                        energy -= 5
                                                                                        time.sleep(2)
                                                                        elif hunttargeone == "bird":
                                                                                print("| You shot a little bird! So-so production")   
                                                                                itembird += 1
                                                                                energy -= 2
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
                                                                                        money -= money / 2
                                                                                        energy -= energy / 2
                                                                                        health = 15
                                                                                        time.sleep(2)
                                                                                else:
                                                                                        health -= 10
                                                                                        print("| you hit a deer in the leg and it ran at you! Your HP has dropped to " + str(health))
                                                                                        time.sleep(2)
                                                        except TimeoutOccurred:
                                                                something = "| You didn't have time to shoot ("
                                                        print(something)
                                        elif energy < 6:
                                                print("| You have no energy! Sleep")
                                                time.sleep(2)
                                        invsel=int(input("| Exit?\n> "))
                                        print(invsel)
                                elif seldey == 8:
                                        print("| bb")
                                        os.abort()                                           
                        except ValueError:
                                print("")
