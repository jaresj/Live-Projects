from django.db import models


# model

class Nutrition(models.Model):
    type = models.CharField(max_length=100)
    calories = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    serving_size = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    protein = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    carbohydrates = models.DecimalField(max_digits=3, decimal_places=0, null=True)
    fats = models.DecimalField(max_digits=3, decimal_places=0, null=True)

    food = models.Manager() # Object manager

    def __str__(self):
        return self.type


