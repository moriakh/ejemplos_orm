from django.shortcuts import render, HttpResponse, redirect
from wizard.models import Wizard, Ninja, Dojo

def index(request):
    wizards = Wizard.objects.all()
    context = {
        'wizards': wizards
    }
    return render(request, 'index.html', context)

def add_wizard(request):
    Wizard.objects.create(name = request.POST['wizzfname'], house = request.POST['wizzhouse'], pet = request.POST['wizzpet'], year = int(request.POST['wizzyear']))
    return redirect('/')

def ndindex(request):
    dojos = Dojo.objects.all()
    # ninjas = dojos.ninjas.all()
    ninjas = Ninja.objects.all()

    context = {
        'dojos': dojos,
        'ninjas' : ninjas
    }

    return render(request, 'ninjasdojos.html', context)

def add_ninja(request):
    Ninja.objects.create(dojo = Dojo.objects.get(id = int(request.POST['dojo_id'])), 
                        first_name = request.POST['ninja_fname'], 
                        last_name = request.POST['ninja_lname'],
                        power_force = int(request.POST['ninja_power']))
    return redirect('/dojosyninjas')

def add_dojo(request):
    Dojo.objects.create(name = request.POST['dojo_name'], city = request.POST['dojo_city'], state = request.POST['dojo_state'])
    return redirect('/dojosyninjas')

