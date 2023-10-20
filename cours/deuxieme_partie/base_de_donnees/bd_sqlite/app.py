import sqlite3

conn = sqlite3.connect("database.db")
#ajouter information
#on commence par creer un tableau

c = conn.cursor()

c.execute("""
          CREATE TABLE IF NOT EXISTS employees(
          prenom text,
          nom text,
          salaire
          )
          """)

#INSERTION DES DONNEES en passant apr un dict
d = {"prenom": "Paul", "nom": "Dupond", "salaire": 1000}
c.execute("INSERT INTO employees VALUES (:prenom, :nom, :salaire)", d)

#reccuperer les données
d = {"a": "Paul"}
c.execute("SELECT * FROM employees WHERE prenom=:a ", d)
donnees = c.fetchall()
print(donnees)
premier = c.fetchone
print(premier)

#mettre à jour les données
d = {"salaire": 20000, "prenom": "Patrick", "nom": "Dupont"}

c.execute(
    """
          UPDATE employees SET salaire=:salaire
          WHERE prenom=:prenom AND nom=:nom
    """, d
          )

##supprimer données
c.execute("DELETE FROM employees")


#faire un commit pour executer la requete
conn.commit()

conn.close()