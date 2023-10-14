# comment un ordinateur calcul le temps?
# il utilise l'epoch, le plus connu c'est L'epoch UNIX: 1er janvier 1970 00:00:00 UTC
# epoch est une date arbitraire qui va dependre des SE des langages qu'on utilise
# c'est une date dans le temps à laquelle on va se mettre à compter. python utilise Epoch UNIX....

from time import time

print(time())#nombre de seconde ecoulé depuis cette date

