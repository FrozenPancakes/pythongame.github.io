from pyscript import document
output_div = document.querySelector("#textarea")

printList = []

def _print(text): # USE THIS INSTEAD OF print() IF YOU WANT IT TO SHOW
    printList.append(text)

def reprint():
    print("t")
    output_div.innerText = "\n".join(printList)


#### ^^ HTML SETUP DO NOT TOUCH ^^ ####

import random
import js
from time import sleep

_print("DEAD WEST")
_print("Welcome to the Game")
_print("be sure to sub 2 ades!!!")
_print("if you don't i will steal ur kneecaps")
_print(" ")

_print("The year is 1884, the World has been taken over by an Zombie Apocolypse, the only safe spot is in Mexico exactly 100km away from you in the USA. You plan to travel there to be safe but the only way is through a train. You go to find a driver only to realize that they all turned into Zombies. You are on your own and have to find everything you need such as fuel. Good Luck")
_print(" ")

_print("HOW TO PLAY")
_print("The Goal of the Game: Reach 100km.")
_print("Raid Houses or Cities to get items to sell which you store in your Sack which contains 25kg worth of items.")
_print("You start off with a Crowbar that can be used to pry open House Doors and Kill Zombies.")
_print("Add Coal to the Furnace in the Train to add 'Ticks' of fuel.")
_print("Good Luck!")

_print(" ")
_print("Type [yes] to see Complex Instructions otherwise type [no] to Start")

reprint()


sleep(10)
prompt = js.prompt("sub2ades?")

while prompt != "yes" or "no":
    print("wha")
    prompt = js.prompt("invalid answer") 

if prompt == "yes":
    printList = []
    _print("ades")
    reprint()
elif prompt == "no":
    js.alert("you suck and you should sub now")
