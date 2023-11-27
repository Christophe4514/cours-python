# Creer un projet django

    1. creer un environnement virtuel
    
    2. installer django: "pip install django"

    3. verifier la version de django: "python -m django --version"

## Pour concerver ses pacquages :

    on gèle son environement viertuel dans un fichier requirements.txt :

    pip freeze > requirements.txt

    N.B: s'assurer qu'on a sourcer son environement virtuel pour faire
*
    * Pour afficher le contenu de ce fichier on utilise la cmd:
*

    * cat requirements.txt
  
## Créer un projet django

* django-admin startproject DocBlog

## Lancer le serveur de production:

  On ne va pas passer par django-admin mais par le fichier management :
  
  On va aller dans src avec cd src

  Ensuite : * python manage.py runserver
  
  Appliquer la migration : python manage.py migrate
  
## La variable d'environnement append_views 

  lorsqu'on cree une vue sans mettre le slash (/) à la fin si la variable append est à true, la vue est directement rediriger vers la page avec le / que django g_re automatiquement, sinon la vue renvoie une erreur 404