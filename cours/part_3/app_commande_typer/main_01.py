# creation de la base d'une application avec typer

import typer

def main():
    """
    Affiche les fichier trouvés avec l'extension données.
    """
    typer.echo("Recherche des fichiers")

if __name__ == "__main__":
    typer.run(main)
