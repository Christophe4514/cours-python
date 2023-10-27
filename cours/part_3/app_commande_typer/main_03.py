# quand on donne une val par defaut on a une option
import typer

app = typer.Typer()


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
        typer.echo("Suppresions des fichiers.")
        # confirm = typer.confirm("Vouler vous supprimer ?")
        # if not confirm:
        #     typer.echo("Opération annulé.")
        #     raise typer.Abort()
        # typer.confirm("Vouler vous supprimer les fichier ?", abort=True)
        
    # print("Suppression des fichier!")

@app.command("search")
def search_py():
    main(delete=False, extension="py")

@app.command("delete")
def delete_py():
    main(delete=True, extension="py")


if __name__ == "__main__":
    app()
