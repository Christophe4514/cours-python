# logging est une module qui permet d'afficher les messages d'erreurs
#  5 niveux de message à afficher du moins au plus important

import logging
from venv import logger

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s : %(levelname)s : %(message)s')

# ICI on aura seulement error et critical

# logging.basicConfig(level=logging.DEBUG) # SI ON CONFIGURE NOTRE LOGGIN AVEC CE NIVEAU ON AURA TOUT LES MESSAGES

# logging.basicConfig(level=logging.INFO)

# logging.basicConfig(level=logging.WARNING)

# logging.basicConfig(level=logging.CRITICAL)

logging.debug("La fonction a bien été exécutée")
logging.info("Message d'information général")
logging.warning("Attention !")
logging.error("Une erreur est arrivée")
logging.critical("Erreur critique")