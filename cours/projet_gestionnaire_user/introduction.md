# Le gestionnaire d'utilisateurs

'

    Dans les prochaines parties, je vous ai préparé un projet concret typique, qui va vous permettre de mettre en pratique toutes ces notions. Ce projet va nous permettre de gérer des utilisateurs, avec leur nom, prénom, adresse et numéro de téléphone. On pourra ainsi se créer un carnet d'adresse de nos contacts, quelque chose que vous retrouvez dans beaucoup d'entreprise via ce qu'on appelle le CRM (Customer Relationship Management, c'est à dire la gestion des relations avec le client).

    Ce projet est relativement simple au niveau de la logique et du code, le but n'est pas de vous tordre le cerveau sur la partie algorithme. Vous verrez que les fonctionnalités de notre programme seront donc très basiques. Cela vous permettra également de voir à quel point une grande partie des lignes de code ne sont pas constitué par les fonctionnalités du programme mais par la documentation, les tests, le logging, etc.



    Ce projet a donc pour but de vous montrer tous les éléments qui constituent un vrai projet Python professionnel.



    Création des fichiers, de l'environnement virtuel, organisation et documentation du code, mise en place d'un logger. On va revoir tous ces sujets ensemble dans ce projet.



    Ce projet reviendra également plus tard dans la formation. On y reviendra lors de la partie sur l'orienté objet pour modifier la façon dont notre code est organisé pour rajouter des classes.



    On y reviendra pour ajouter des tests unitaires une fois que nous aurons vu la théorie sur le sujet.



    On y reviendra également quand nous aurons vu la bibliothèque Typer pour créer des programmes en ligne de commande.



    Ou encore après la partie sur Django, pour utiliser notre API réalisée lors de la partie sur l'orientée objet, avec une interface web.


'

'[source:] [https://github.com/DocstringFr/la-formation-complete-python/tree/master/prj-010_le-gestionnaire-dutilisateurs-crm]'

# Intaller un environement virtuel env

    en utilisant la commande :

    pytnon -m venv nom_de_mon_environnement

# Lancer son envirennement 

    source Script/activate

# Installer Faker 

    pip install Faker

## Utiliser pip list 

    pour voir les packages installer

# Creer un module user

    qui contient deux fonction :

    get_user : pour générer les utilisateurs

    get_users : pour générer plusieurs utilisateurs