import math
# from goto import with_goto

nombre_un = input("inserer le premier nombre : \n")
nombre_deux = input("inserer le second nombre : \n")
if( nombre_un.isdigit() & nombre_deux.isdigit() ):
    print(f"la somme de {nombre_un} et {nombre_deux} = {int(nombre_un) + int(nombre_deux)}")
else:
    print("impossible de faire l'addition !")