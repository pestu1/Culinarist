from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Meal, Experience, Recipe
from .forms import MealForm, ExperienceForm, RecipeForm

def index(request):
    """Culinarist kotisivu."""
    return render(request, 'culinarists/index.html')

@login_required
def meals(request):
    """Näytä kaikki ateriat."""
    meals = Meal.objects.filter(owner =request.user).order_by('date_added')
    context = {'meals': meals}
    return render(request, 'culinarists/meals.html', context)

@login_required
def meal(request, meal_id):
    """näyttää yhden tietyn aterian"""
    meal = Meal.objects.get(id=meal_id)
    #estää muiden aterioiden näkemisen
    if meal.owner != request.user:
        raise Http404
    experiences = meal.experience_set.order_by('-date_added')
    allergens = meal.allergens
    context = {'meal': meal, 'experiences': experiences, 'allergens': allergens}
    return render(request, 'culinarists/meal.html', context)

@login_required
def new_meal(request):
    """lisää uusi ateria-annos."""
    if request.method != 'POST':
        # Ei dataa --> anna tyhjä lomake
        form = MealForm()
    else:
        # POST data annettu. Käsittele data
        form = MealForm(data=request.POST)
        if form.is_valid():
            new_meal = form.save(commit=False)
            new_meal.owner = request.user
            new_meal.save()
            return redirect('culinarists:meals')
    
    #Näytä tyhjä tai invalidi lomake
    context = {'form': form}
    return render(request, 'culinarists/new_meal.html', context)

@login_required
def new_experience(request, meal_id):
    meal = Meal.objects.get(id=meal_id)

    if request.method != 'POST':
        form = ExperienceForm()
    else:
        form = ExperienceForm(data=request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.meal = meal
            experience.save()
            return redirect('culinarists:meal', meal_id=meal.id)

    context = {'form': form, 'meal': meal}
    return render(request, 'culinarists/new_experience.html', context)

@login_required
def edit_experience(request, experience_id):
    """muokkaa olemassa olevaa kokemusta."""
    experience = Experience.objects.get(id=experience_id)
    meal = experience.meal
    #estää muiden kokemusten muokkaamisen
    if meal.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = ExperienceForm(instance=experience)
    else:
        form = ExperienceForm(instance=experience, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('culinarists:meal', meal_id=meal.id)
    context = {'experience': experience, 'meal': meal, 'form': form}
    return render(request, 'culinarists/edit_experience.html', context)
    
@login_required  
def recipes(request):
    """Näytä kaikki reseptit."""
    recipes = Recipe.objects.order_by('date_added')
    context = {'recipes': recipes}
    return render(request, 'culinarists/recipes.html', context)

@login_required
def edit_recipe(request, recipe_id):
    """Muokkaa olemassa olevaa reseptiä."""
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method != 'POST':
        # Alkuperäinen pyyntö; täytä lomake nykyisellä reseptillä.
        form = RecipeForm(instance=recipe)
    else:
        # POST-data lähetetty; käsittele data.
        form = RecipeForm(instance=recipe, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('culinarists:recipes')

    context = {'recipe': recipe, 'form': form}
    return render(request, 'culinarists/edit_recipe.html', context)

@login_required
def new_recipe(request):
    """Lisää uusi resepti."""
    if request.method != 'POST':
        # Ei dataa --> anna tyhjä lomake
        form = RecipeForm()
    else:
        # POST data annettu. Käsittele data
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('culinarists:recipes')

    # Näytä tyhjä tai invalidi lomake
    context = {'form': form}
    return render(request, 'culinarists/new_recipe.html', context)
    
    

