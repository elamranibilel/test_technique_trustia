from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/creer/', views.creer_produit, name='creer_produit'),
    path('produits/<int:pk>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('produits/<int:pk>/supprimer/', views.supprimer_produit, name='supprimer_produit'),

    path('factures/', views.liste_factures, name='liste_factures'),
    path('factures/creer/', views.creer_facture, name='creer_facture'),
    path('factures/<int:pk>/', views.detail_facture, name='detail_facture'),
]
