Outil en ligne de commande pour intéragir avec le SAEM
------------------------------------------------------

Pour lister les commandes disponibles : ::

  ./saem-client --help

ou pour obtenir les options spécifiques à une commande : ::

  ./saem-client eac-download --help


Gestion des notices d'autorités
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour récupérer les notices d'autorités : ::

  ./saem-client eac-download https://demo.logilab.fr/saem-demo

Cette commande va rappatrier les notices d'autorités publiques du référentiels sous forme de
fichiers XML au format EAC qui seront mis dans le répertoire de travail.

Pour envoyer une nouvelle notice d'autorités au format EAC dans un fichier ``fichier-eac.xml`` : ::

  ./saem-client eac-upload https://demo.logilab.fr/saem-demo fichier-eac.xml

Cette commande s'attend à trouver dans le répertoire de travail un fichier ``cubicweb.yaml``
comportant les identifiants de connexion au format YAML, par exemple : ::

  id: token-arkheia
  secret: 11e9ae06d7754a89a13d0e7245bc6132320cb081813b4d229a4d6

Gestion des vocabulaires
~~~~~~~~~~~~~~~~~~~~~~~~

Pour récupérer les concepts d'un vocabulaire : ::

  ./saem-client skos-download https://demo.logilab.fr/saem-demo 23578/v000200007

Cette commande va récupérer les concepts du vocabulaire ayant l'identifiant ARK
``23578/v000200007``, sous forme de fic hier XML au format SKOS qui serons mis dans un
sous-répertoire ``23578-v000200007`` du répertoire de travail.
