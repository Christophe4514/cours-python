a = 5
b = 0

# print(a/b)
# except avec précision
try:
    print(a/b)
except ZeroDivisionError:
    print(f"division par {b} impossible")

c = 10
d = "blabla"

try:
    resultat = c/d
except ZeroDivisionError:
    print(f"impossible de diviser par {d}")
except NameError:
    print(f"la variable {d} n'est pas defini")
except TypeError as e:
    print("Errer:", e)
else:
    print(resultat)
finally: #sera toujours executer
    print("fin du block de code")