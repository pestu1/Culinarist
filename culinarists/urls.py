"""Määrittää URL-patternit culinarists:lle."""
from django.urls import path
from . import views

app_name = 'culinarists'
urlpatterns = [
    #kotisivu
    path('', views.index, name='index'),
    #Sivu joka näyttää kaikki ateriat
    path('meals/', views.meals, name='meals'),
    #yksittäisen aterian sivu
    path('meals/<int:meal_id>/', views.meal, name='meal'),
    #Uuden aterian lisäämissivu
    path('new_meal/', views.new_meal, name='new_meal'),
    #Uuden kokemuksen lisäämissivu
    path('new_experience/<int:meal_id>/', views.new_experience, name='new_experience'),
    #kokemusten muokkaussivu
    path('edit_experience/<int:experience_id>/', views.edit_experience, name='edit_experience'),
    #kaikkien reseptien sivu
    path('meals/recipes', views.recipes, name='recipes'),
    #muokkaa reseptiä
    path('recipes/edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    #lisää uusi resepti
    path('recipes/new/', views.new_recipe, name='new_recipe'),
]
