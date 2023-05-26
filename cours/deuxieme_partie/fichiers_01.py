# Erreurs courantes avec les fichiers JSON
# https://www.udemy.com/course/formation-complete-python/learn/lecture/16181677#overview
# Beaucoup d'étudiants ont donc l'erreur json.decoder.JSONDecodeError alors que tout est expliqué dans la vidéo ci-dessus.

# 
# 01 Les chemins de dossiers sur votre système d'exploitation.
# Les chemins sur windows

chemin = r"C:\Users\Enabel62\OneDrive\Documents\python\cours-python\cours"
# print(chemin) 
#Erreure à cause des '\U' qui est interprété comme du unicode, si on remplace \U par \Z, le print va marché
chemin = "C:\Zsers\Enabel62\OneDrive\Documents\python\cours-python\cours"
# print(chemin) 
#si il y avait un \t dans le nom du fichier, cela affichera de l'espace puisque l'interpreteur va comprendre cela comme du tabilation 
# exemple
chemin = "C:\Zsers\Enabel62\tneDrive\Documents\python\cours-python\cours"
# print(chemin) 
# solution : interprété le chemin comme du text brut en ajoutant un r devant la chaine :
# exemple
chemin_correct_1 = r"C:\Users\Enabel62\OneDrive\Documents\python\cours-python\cours"
print(chemin_correct_1) 
# ou inverser le sens des slash comme sur linux ou os
chemin_correct_2 = "C:/Users/Enabel62/OneDrive/Documents/python/cours-python/cours"
print(chemin_correct_2) 