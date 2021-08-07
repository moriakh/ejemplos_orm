from django.db import models
from django.db.models.deletion import CASCADE

class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField(default="desc")
    

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    power_force = models.IntegerField(default=12)

'''
python manage.py makemigrations
python manage.py migrate

from wizard.models import Dojo, Ninja

dojo1 = Dojo.objects.create(name = "Miyagi Things", city = "Osaka", state = "Edo")
dojo2 = Dojo.objects.create(name = "Teriyaki", city = "Sushi", state = "Fuji")
dojo3 = Dojo.objects.create(name = "Ozuna", city = "Suki", state = "Nagaya")

dojo1.delete()
dojo2.delete()
dojo3.delete()

dojo4 = Dojo.objects.create(name = "Suzumu", city = "Yokota", state = "Fuji")
dojo5 = Dojo.objects.create(name = "Emerald", city = "Rush", state = "Jade")
dojo6 = Dojo.objects.create(name = "Tom", city = "Cruise", state = "Wurtz")

dojo4.ninjas.create(first_name = "Hiperion", last_name = "Sol")
dojo4.ninjas.create(first_name = "Daniel", last_name = "Sun")
dojo4.ninjas.create(first_name = "Hipogrifo", last_name = "Condor")

dojo5.ninjas.create(first_name = "Agente", last_name = "Lince")
dojo5.ninjas.create(first_name = "Emerald", last_name = "Stone")
dojo5.ninjas.create(first_name = "Rush", last_name = "Emerald")

dojo6.ninjas.create(first_name = "Thunder", last_name = "Bird")
dojo6.ninjas.create(first_name = "Piola", last_name = "Jaiva")
dojo6.ninjas.create(first_name = "Laja", last_name = "Salto")

Dojo.objects.first().ninjas.all()
Dojo.objects.last().ninjas.all()
Dojo.objects.last().ninjas.last()

python manage.py makemigrations
python manage.py migrate

from wizard.models import Dojo
dojo7 = Dojo.objects.create(name = "Shoy", city = "Lee", state = "Fut", desc = "Cibercrimen")
'''
