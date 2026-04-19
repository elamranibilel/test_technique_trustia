WIDTH = 100

data = {
    "bloc1": [
        {"texte": "Le code propre facilite la maintenance", "visible": True},
    ],
    "bloc2": [
        {"texte": "Tester souvent évite beaucoup d erreurs", "visible": True},
        {"texte": "Cette phrase ne doit pas s afficher", "visible": False},
    ],
    "bloc3": [
        {"texte": "Cette phrase ne doit pas s afficher", "visible": True},
        {"texte": "Un bon code doit rester simple et clair", "visible": False},
        {"texte": "La simplicité améliore la qualité du code", "visible": True},
        {"texte": "Refactoriser améliore la compréhension", "visible": True},
    ],
}

sep = "-" * WIDTH

for bloc in data.values():
    print(sep)
    for phrase in bloc:
        if phrase["visible"]:
            print("| " + phrase["texte"].lower().rjust(WIDTH - 3) + "|")
    print(sep)
    print()
