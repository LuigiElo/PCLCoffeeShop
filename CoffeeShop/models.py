from enum import Enum

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

# Create your models here.
from django.db.models import Sum


class Category(Enum):
    Coffee = "Coffee"
    Tea = "Tea"
    Juice = "Juice"
    Soda = "Soda"
    Milk = "Milk"


class Size(Enum):
    Small = "Small"
    Medium = "Medium"
    Large = "Large"


class Drink(models.Model):
    category = models.CharField(
        max_length=10,
        choices=[(tag.value, tag.name) for tag in Category])
    type = models.CharField(max_length=20)
    size = models.CharField(
        max_length=10,
        choices=[(tag.value, tag.name) for tag in Size])
    price = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.category}, {self.type}, {self.size}, {self.price}" + "$"


class Order(models.Model):
    drinks = models.ManyToManyField("Drink", blank=True)
    buyer = models.CharField(max_length=20)