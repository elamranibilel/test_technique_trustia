# Test technique - Trustia

## Exercice 1

Programme Python qui affiche dans la console des blocs de texte encadrés.

- Données stockées dans un seul dictionnaire structuré
- Activation/désactivation d'une phrase via un booléen `visible`
- Largeur des blocs facilement modifiable via `WIDTH`

```bash
python exercice1.py
```

## Exercice 2

Programme Python qui affiche un menu de restaurant dans la console.

- Menu organisé par catégories (Entrées, Plats, Desserts)
- Chaque plat possède un nom, un prix et une disponibilité
- Les plats indisponibles sont masqués avec un booléen `visible`

```bash
python exercice2.py
```

## Application Django (dossier `Store/`)

Application web de gestion de produits et de factures réalisée avec Django.

### Installation

```bash
cd Store
python -m venv venv
source venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```

Ouvrir `http://127.0.0.1:8000` dans le navigateur.

### Fonctionnalités

- Créer, modifier, supprimer et lister des produits
- Créer des factures avec plusieurs produits et quantités
- Consulter le détail d'une facture (total, nombre de produits)
- Pagination sur les listes

## Stack

- Python 3
- Django / SQLite
- Bootstrap 5
