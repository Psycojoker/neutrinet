# Intro

Nouvelle version du site de [Neutrinet](http://neutrinet.be).

# Comment tester le site?

Pour cela vous devez avoir python et le framework web python [django](https://docs.djangoproject.com) installé.

Sous les debian based python est fournit par défaut, pour installer django:

    sudo apt-get install python-django

Une fois que c'est fait, cloner le dépot et allez dans le nouveau répertoire:

    git clone git://github.com/Psycojoker/neutrinet.git
    cd neutrinet

Ensuite, installez les dépendances:

    pip -r requirements.txt

Puis, pour créer la db (par défaut c'est du sqlite) et charger les fixtures (des données par défaut):

    ./manage.py syncdb

Il va vous proposer de créer un admin, si vous ne voulez pas le faire tout de suite vous pouvez le faire après avec la commande:

    ./manage.py createsuperuser

Pour lancer un serveur de dev:

    ./manage.py runserver

Pour lui demander d'écouter pas uniquement les requètes venant de la machine sur lequel il tourne (et changer de port):

    ./manage.py runserver 0.0.0.0:8000

Si vous voulez modifier le fichier settings.py mais uniquement pour des modifications propre à la machine courante (ie: setter une autre db) vous pouvez créer le fichier *settings_local.py* qui surchargera toutes les configs de settings.py que vous definiriez dedans.

# TODO

* Utiliser reversion sur les flatpages
* Hoster ce dépot git chez nous
