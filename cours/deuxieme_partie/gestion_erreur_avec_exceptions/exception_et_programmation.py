#ici il est question de continuer d'executer un script meme en cas d'erreur
#grace aux exceptions avec les deux facon de coder :
#LBYL (look before you leap) regarder avant de sauter
#EAPF (it's easier to ask for forgiveness than permission) il est plus facile de demander pardon que de demander la permission

#LBYL
# if "cle" in dict:
#     print(dict["cle"])

# EAFP
# try:
#     print(dict["cle"])
# except:
#     pass

# exemple
liste = [2,3,"texte",4]
# total = sum(liste) #ne va pas marché

# LBYL
for i in liste:
    if not str(i).isdigit():
        liste.remove(i)
total = sum(liste)
print(f"total est : {total}")

# EAFP
listes = [2, 5, "var", 10]
try:
    totale = sum(listes)
except:
    totale = 0
    print(f"total EAFP est: {totale}")