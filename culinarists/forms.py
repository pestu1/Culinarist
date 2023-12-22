from django import forms

from .models import Meal, Experience, Recipe

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'allergens']
        labels = {'name': ''}


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['text', 'rating']
        labels = {'text': 'Entry:', 'rating': 'Rating:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['meal', 'preparation']
        
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['meal', 'preparation']
