phrases = {
    "code_propre":  "Le code propre facilite la maintenance",
    "tester":       "Tester souvent évite beaucoup d erreurs",
    "cache_1":     "Cette phrase ne doit pas s afficher",
    "code_bon":     "Un bon code doit rester simple et clair",
    "simplicite":   "La simplicité améliore la qualité du code",
    "refactoriser": "Refactoriser améliore la compréhension",
}

blocs = [
    ["code_propre"],
    ["tester"],
    ["cache_1", "simplicite", "refactoriser"],
]

WIDTH = 100

def afficher_bloc(keys):
    sep = "-" * WIDTH
    print(sep)
    for key in keys:
        print("| " + phrases[key].lower().rjust(WIDTH - 3) + "|")
    print(sep)

for bloc in blocs:
    afficher_bloc(bloc)
    print()
