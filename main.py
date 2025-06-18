from pyscript import document
output_div = document.querySelector(".textarea")

printList = []

def _print(text): # USE THIS INSTEAD OF print() IF YOU WANT IT TO SHOW
    printList.append(text)

#### ^^ HTML SETUP DO NOT TOUCH ^^ ####

import random

_print("DEAD WEST")
_print("Welcome to the Game")
_print("be sure to sub 2 ades!!!")
_print("if you don't i will steal ur kneecaps")
_print("How to Play" \
"The Goal of the Game: Reach 100km" \
"Raid Houses or Cities to get items to sell or keep in your Sack which contains 25kg worth of items" \
"You start off with a Crowbar that can be used to pry open House Doors and Kill Zombies" \
"Add Coal to the Furnace in the Train to add 'Ticks' of fuel" \
"Good Luck")
_print("Type [y] to see Complex Instructions otherwise type [n] to Start")

#### vv HTML SETUP DO NOT TOUCH vv ####

output_div.innerText = "\n".join(printList) 
