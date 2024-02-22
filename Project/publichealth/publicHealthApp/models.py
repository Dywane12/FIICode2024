from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    dietary_preferences = models.CharField(max_length=200)
    allergens = models.CharField(max_length=200)
    def __str__(self):
        return self.name + ' ' + self.surname + '\n' + self.dietary_preferences + '\n' + self.allergens

class Food(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    weight = models.IntegerField()
    nutritional_facts = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.brand + ' ' + self.name + '\n' + self.nutritional_facts + '\n' + self.price
