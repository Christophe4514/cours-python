# createur des dossier
from pathlib import Path

chemin = r"C:\Users\Enabel62\OneDrive\Documents\python\cours-python\cours\deuxieme_partie"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}


for dossier_principal, sous_dossiers in d.items():
    for dossier in sous_dossiers:
        chemin_dossier = Path(chemin) / dossier_principal / dossier
        chemin_dossier.mkdir(exist_ok=True, parents=True)