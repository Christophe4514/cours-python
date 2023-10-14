# Qu'est-ce qu'un environnement virtuel Python ?
    
    Un environnement virtuel est un environnement d'exécution isolé.

    C'est-à-dire qu'il permet d'isoler les paquets utilisés pour un projet, afin d'avoir 
    
    des versions différentes pour chaque projet.

    Par exemple, vous pouvez avoir sur le même ordinateur deux projets Python qui utilisent chacun une version différente d'un même paquet.

## Pour créer un environnement virtuel Python, vous pouvez utiliser le module venv qui est inclus 
    
    dans la bibliothèque standard de Python. Voici la commande à utiliser :inclus dans la bibliothèque standard de Python. Voici la commande à utiliser :

* python -m venv nom_de_lenvironnement

# Que contient un environnement virtuel Python ?
    
    Un environnement virtuel Python contient plusieurs dossiers et fichiers :

    '
    │ ──├── bin
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── easy_install
    │   ├── easy_install-3.8
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.8
    │   ├── python -> python3
    │   └── python3 -> /Library/Developer/CommandLineTools/usr/bin/python3
    ├── include
    ├── lib
    │   └── python3.8
    │      └── site-packages
    └── pyvenv.cfg

'

* Le dossier bin contient l'interpréteur Python et tous les exécutables dont vous pourriez avoir besoin (comme easy_install ou pip). C'est également dans ce dossier que vous trouverez les fichiers qui vous permettent d'activer votre environnement virtuel (activate).

* Le dossier include ne contient par défaut aucun fichier. Ce dossier sert dans le cas de la création de bibliothèques utilisant le langage C.

* Le dossier lib contient tous les paquets que vous installerez avec pip dans cet environnement virtuel (à l'intérieur du sous-dossier site-packages).

* Le fichier pyvenv.cfg contient des variables qui définissent certains paramètres de votre environnement virtuel, comme le chemin vers l'interpréteur Python système ou la version de Python de votre environnement virtuel.

# Comment activer un environnement virtuel Python ?

    Pour activer votre environnement virtuel Python, il suffit de « sourcer » le fichier activate dans votre terminal :

* source bin(script)/activate

    Si vous utilisez Windows, vous n'aurez pas un dossier bin mais un dossier Scripts. Pour activer votre environnement virtuel, il vous suffit de taper activate.bat dans l'invite de commande.

# pour desactiver :

    on utilise la commande:

    deactivate