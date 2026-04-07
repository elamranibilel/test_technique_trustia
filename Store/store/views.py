from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Produit, Facture, LigneFacture
from .forms import ProduitForm, FactureForm


# ---------- Accueil ----------

def accueil(request):
    return render(request, 'store/accueil.html')


# ---------- Produits ----------

def liste_produits(request):
    produits = Produit.objects.all()
    paginator = Paginator(produits, 10)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'store/liste_produits.html', {'page_obj': page})


def creer_produit(request):
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'store/form_produit.html', {'form': form})


def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    form = ProduitForm(request.POST or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'store/form_produit.html', {'form': form})


def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'store/confirmer_suppression.html', {'produit': produit})


# ---------- Factures ----------

def liste_factures(request):
    factures = Facture.objects.all().order_by('-date_creation')
    paginator = Paginator(factures, 10)
    page = paginator.get_page(request.GET.get('page'))
    return render(request, 'store/liste_factures.html', {'page_obj': page})


def creer_facture(request):
    produits = Produit.objects.all()
    if request.method == 'POST':
        facture = Facture.objects.create()
        for produit in produits:
            quantite = request.POST.get(f'quantite_{produit.id}', 0)
            if int(quantite) > 0:
                LigneFacture.objects.create(facture=facture, produit=produit, quantite=quantite)
        return redirect('detail_facture', pk=facture.pk)
    return render(request, 'store/creer_facture.html', {'produits': produits})


def detail_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'store/detail_facture.html', {'facture': facture})
