from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add_wizard', views.add_wizard, name='add_wizz'),
    path('dojosyninjas', views.ndindex, name='ndindex'),
    path('add_dojo', views.add_dojo, name='add_dojo'),
    path('add_ninja', views.add_ninja, name='add_ninja')
]
