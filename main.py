from pyscript import document
output_div = document.querySelector("#textarea")

printList = []

def _print(text): # USE THIS INSTEAD OF print() IF YOU WANT IT TO SHOW
    printList.append(text)

#### ^^ HTML SETUP DO NOT TOUCH ^^ ####

import random

_print("DEAD WEST")
_print("Welcome to the Game")
_print("be sure to sub 2 ades!!!")
_print("if you don't i will steal ur kneecaps")
_print("The year is 1884, the World has been taken over by an Zombie Apocolypse, the only safe spot is in Mexico exactly 100km away from you in the USA. You plan to travel there to be safe but the only way is through a train. You go to find a driver only to realize that they all turned into Zombies. You are on your own and have to find everything you need such as fuel. Good Luck")

_print("Type 'y' to see Complex Instructions otherwise type n to Start")

#### vv HTML SETUP DO NOT TOUCH vv ####

output_div.innerText = "\n".join(printList) 
