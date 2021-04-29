from django.contrib import admin
from django.utils.html import format_html

from CoffeeShop.models import Drink, Order
from django.urls import reverse
from django.utils.http import urlencode


# Register your models here.
@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ("category", "type", "size", "price")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("buyer", "order_items", "total_price")

    def order_items(self, obj):
        count = ""
        for drink in obj.drinks.all():
            count += str(drink.category + " " + drink.type + ", ")

        url = (
                reverse("admin:CoffeeShop_drink_changelist")
                + "?"
                + urlencode({"orders__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">Drinks: {}</a>', url, count)

    def total_price(self, obj):
        result = sum(drink.price for drink in obj.drinks.all())
        return f'{result}$'
