menu = {
    "entrées": [
        {"nom": "Salade César", "prix": 8, "visible": True},
        {"nom": "Soupe du jour", "prix": 6, "visible": False},
    ],
    "plats": [
        {"nom": "Steak frites", "prix": 15, "visible": True},
        {"nom": "Poisson grillé", "prix": 14, "visible": True},
        {"nom": "Plat du chef", "prix": 18, "visible": False},
    ],
    "desserts": [
        {"nom": "Tiramisu", "prix": 7, "visible": True},
        {"nom": "Glace", "prix": 5, "visible": True},
        {"nom": "Dessert mystère", "prix": 9, "visible": False},
    ],
}

for categorie, plats in menu.items():
    print(f"\n--- {categorie} ---")
    for plat in plats:
        if plat["visible"]:
            print(f"{plat['nom'].lower()} - {plat['prix']}€")
