# modifier affichage couleur
# installer colorama sur windows
# ajouter bar de progression
import time
import typer 

def main():
    # prenom = typer.style("Patrick", fg=typer.colors.RED, bg=typer.colors.BLACK, bold=True, underline=False, blink=False)
    if False:
        prenom = typer.style("Patrick", fg=typer.colors.RED, bg=typer.colors.BLACK, bold=True)
    else:
        prenom = typer.style("Patrick", fg=typer.colors.BLUE, bg=typer.colors.BLACK, bold=True)
    
    typer.secho(f"Bonjour {prenom}", fg=typer.colors.GREEN, bold=True)

    # prenoms = ["Patrick", "Marie", "Julie", "Paul", "Pierre"]
    prenoms = range(20)
    
    with typer.progressbar(prenoms) as progress:
        for prenom in progress:
            time.sleep(1) 

    typer.echo("Fin du script")


if __name__ == "__main__":
    typer.run(main)