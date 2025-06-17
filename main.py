from pyscript import document
output_div = document.querySelector("#textarea")

def _print(text):
    output_div.innerText = text

#############

import random

randomnumber = random.randint(1,2)

if randomnumber == 1:
    _print("sub2ades")
else: 
    _print("unsub2ades")