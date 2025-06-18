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


#### vv HTML SETUP DO NOT TOUCH vv ####

output_div.innerText = "\n".join(printList) 
