from pyscript import document
output_div = document.querySelector("#textarea")

printList = []

def _print(text): # USE THIS INSTEAD OF print() IF YOU WANT IT TO SHOW
    printList.append(text)

#### ^^ HTML SETUP DO NOT TOUCH ^^ ####

import random
randomnumber = random.randint(1,8)

_print("wow")
_print("wo2w2")

#### vv HTML SETUP DO NOT TOUCH vv ####

output_div.innerText = "\n".join(printList)
print("\n".join(printList))
