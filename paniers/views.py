# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from commandes.models import Commande
from django.shortcuts import render, redirect
from produits.models import Produit
from .models import Panier

def panier_home(request):
    panier_obj, new_obj = Panier.objects.new_or_get(request)
    context = {
        "panier": panier_obj,
    }
    return render(request, 'paniers/home.html', context)

def maj_panier(request):
    #print(request.POST)
    produit_id = request.POST.get('produit_id')
    if produit_id is not None:
        try:
            produit_obj = Produit.objects.get(id=produit_id)
        except Produit.DoesNotExist:
            print('Afficher le Message Suivant, Article en rupture desole!!')
            return redirect('panier:panier')
        panier_obj, new_obj = Panier.objects.new_or_get(request)
        if produit_obj in panier_obj.produits.all():
            panier_obj.produits.remove(produit_obj)
        else:
            panier_obj.produits.add(produit_obj)
        request.session['panier_items'] = panier_obj.produits.count()
        #return redirect(produit_obj.get_absolute_url())
    return redirect('panier:panier')

def checkout_home(request):
    panier_obj, nv_panier = Panier.objects.new_or_get(request)
    cmde_obj = None
    if nv_panier or panier_obj.produits.count() == 0:
        return redirect('panier:panier')
    else:
        cmde_obj, new_cmde_obj = Commande.objects.get_or_create(panier=panier_obj)

    context = {
        'object': cmde_obj,
    }

    return render(request, 'paniers/checkout.html', context)




# Create your views here.
