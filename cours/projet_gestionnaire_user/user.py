"""Module to generate random users"""
import faker
import logging
from pathlib import Path

# from deuxieme_partie.projet import BASE_DIR


# définir le fichier de log

n = input("entrer le nombre d'utilisateur à generer : \n")
n = int(n)

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'user.log', level=logging.WARNING)
 
    # logging.basicConfig(level=logging.WARNING,
    #                     filename="user.log",
    #                     filemode="w",
    #                     format='%(asctime)s - %(levelname)s - %(message)s')

fake = faker.Faker(locale="fr_FR")


def get_user():
    """Generate a ingle user

    Returns:
        str: user
    """

    logging.info("Generate a single user.")
    return f"{fake.first_name()} {fake.last_name()}"



def get_users(n):
    """Generate a list of user

    Args:


    Args:
        n (int): Number of user to generate

    Returns:
        list[str]: user
    """
    logging.info(f"Generate a list of {n} user.")
    return [get_user() for _ in range(n)]

if __name__ == "__main__":
    user = get_users(n)
    print(user)
