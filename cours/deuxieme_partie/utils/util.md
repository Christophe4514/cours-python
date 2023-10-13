# Package
    
    c'est un document contenant des miodules

# Documentation du code 

## 3 méthodes :

* Le mot docstring est un raccourci pour DOCumentation STRINGs.

    On les utilise pour donner des indications sur le comportement d'une fonction, d'une méthode, d'une classe ou même d'un module entier.

    Vous pouvez accéder à cette documentation à n'importe quel moment dans votre code grâce à la méthode __doc__ :

    ['
        
        def print_modulo(): 

        """Affiche tous les chiffres pairs compris entre 0 et 10"""

        for i in range(10): 

            if i % 2 == 0: 

                print(i) 

        print(print_modulo.__doc__)

    ']

    1. Google

    2. sphinx

    3. numpy

    lien: https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring

    extension vscode : autoDocstring