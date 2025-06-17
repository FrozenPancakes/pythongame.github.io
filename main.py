from pyscript import document
output_div = document.querySelector("#textarea")

def _print(text): # USE THIS INSTEAD OF print() IF YOU WANT IT TO SHOW
    output_div.innerText = text

#### ^^ HTML SETUP DO NOT TOUCH ^^ ####

import random
randomnumber = random.randint(1,8)

_print("wow")
_print("wo2w2")