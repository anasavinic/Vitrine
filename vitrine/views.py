from django.shortcuts import render, redirect

from vitrine.forms import CityForm, VitrineForm
from vitrine.models import Vitrine, Hotel


def lista_vitrine(request):
    qs = Vitrine.objects.all()
    hotel = Hotel.objects.all()

    context = {
        'vitrine': qs,
        'hotel': hotel,
    }

    return render(request, 'vitrine/lista_vitrine.html', context)


def destinos_vitrine(request):
    hotel = Hotel.objects.all()

    context = {
        'hotel': hotel,
    }

    return render(request, 'vitrine/destinos_vitrine.html', context)


def sobre_vitrine(request):
    sobre = Hotel.objects.all()

    context = {
        'sobre': sobre,
    }

    return render(request, 'vitrine/sobre_vitrine.html', context)


def cadastro_cidades(request):

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vitrine-lista')
    else:
        form = CityForm()
    context = {
        'form': form,
    }

    return render(request, 'vitrine/cadastro_cidades.html', context)


def cadastro_vitrine(request):

    if request.method == "POST":
        form = VitrineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vitrine-lista')
    else:
        form = VitrineForm()
    context = {
        'form': form,
    }

    return render(request, 'vitrine/cadastro_vitrine.html', context)