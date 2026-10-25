INFORMATIONS IMPORTANTES :
Mot de passe de l'admin : P@ssword123

Nom d'utilisateur de l'employé de test : Employee
Mot de passe de l'employé de test : P@ssword123

Nom d'utilisateur du participant de test : MathTen
Mot de passe du participant de test : P@ssword1234

COMMANDES EXÉCUTÉES DANS LE CADRE DU PROJET :
# Point 2 :
python -m pip install Pillow
python manage.py makemigrations
python manage.py migrate

# Point 6 :
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py create_groups

# Point 7 :
[Création de l'arborescence :
management
> commands
    > create_groups.py
    > __init__.py
> __init__.py
]

python -m pip install django-modeltranslation
python manage.py check
python manage.py makemigrations
python manage.py migrate

[Installation de GNU gettext (64 bits, Shared) pour Windows,
via "https://mlocati.github.io/articles/gettext-iconv-windows.html?utm_source=chatgpt.com",
ensuite placé dans C:\gettext]

$env:Path += ";C:\gettext\bin"
python manage.py makemessages -l en

[Traductions anglaises mentionnées dans locale/en/LC_MESSAGES/django.po]

python manage.py compilemessages
python manage.py update_translation_fields

# Point 8 :
[Création du chemin tournaments/fixtures/initial_data.json]

python manage.py dumpdata tournaments.Tournament tournaments.Team tournaments.Player auth.User --indent 4 -o tournaments/fixtures/initial_data.json
python manage.py dumpdata auth.Group --indent 4 -o tournaments/fixtures/groups.

# Test, sur une nouvelle installation :
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py create_groups
python manage.py createsuperuser