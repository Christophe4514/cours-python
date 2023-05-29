from pathlib import Path
# trier des fichier selon extension
# on ajoute dans le dossier specifique les fichiers specifique selon extension
dirs = {
    ".png": "Images",
    ".mp4": "Videos",
    "txt": "Documents"
}
tri_dirs = Path.home() / "Tri"
filles = [f for f in tri_dirs.iterdir() if f.is_file()]
for f in filles:
    # print(f.name)
    # print(Path.home())
    # continue
    output_dir = tri_dirs / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)