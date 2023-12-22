from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Meal(models.Model):
    """malli annoksesta"""
    name = models.CharField(max_length=400)
    allergens = models.CharField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        """palauttaa string esityksen annoksesta"""
        return self.name


class Experience(models.Model):
    """Kokemus ateriasta"""
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'experiences'
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.meal} - {self.text[:50]}..."

class Recipe(models.Model):
    """Resepti aterialle"""
    meal = models.OneToOneField(Meal, on_delete=models.CASCADE)
    preparation = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recipe for {self.meal.name}"
