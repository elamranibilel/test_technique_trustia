from django.db import models


class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom


class Facture(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(ligne.produit.prix * ligne.quantite for ligne in self.lignes.all())

    def nb_produits(self):
        return sum(ligne.quantite for ligne in self.lignes.all())

    def __str__(self):
        return f"Facture #{self.id}"


class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name="lignes")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def sous_total(self):
        return self.produit.prix * self.quantite
