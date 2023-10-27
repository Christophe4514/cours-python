# ajouter un argument à typer
from click import confirm
import typer

# def main(extension: str = "txt")
# def main(extension: str = typer.Argument(None, help="Extension à chercher")):
# def main(extension: str = typer.Argument(..., help="Extension à chercher")):

# quand on donne une val par defaut on a une option
def main(delete: bool = typer.Option(True, help="Option require"), extension: str = typer.Argument("txt", help="Extension à chercher")):
    """
    Affiche les fichier trouvés avec l'extension données.
    """
    print(delete)

    if not extension:
        pass

    typer.echo(f"Recherche des fichiers avec extensions {extension}")
    # demander information ou confirmation
    # extension = typer.prompt("entrer extension à chercher? ")
    # print(extension)

    # demande confirmation
    if delete:
        # confirm = typer.confirm("Vouler vous supprimer ?")
        # if not confirm:
        #     typer.echo("Opération annulé.")
        #     raise typer.Abort()
        typer.confirm("Vouler vous supprimer les fichier ?", abort=True)
        
    print("Suppression des fichier!")

if __name__ == "__main__":
    typer.run(main)
