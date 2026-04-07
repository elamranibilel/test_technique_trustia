# Test technique - Trustia

## Exercice 1

Programme Python qui affiche des blocs de texte encadrés dans la console.

```bash
python exercice1.py
```

## Exercice 2

Application web Django de gestion de produits et de factures.

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

### Stack

- Python / Django
- SQLite
- Bootstrap 5
