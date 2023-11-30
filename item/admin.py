from django.contrib import admin

from item.models import Item


# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description',)
    search_fields = ('name', 'description',)
    list_filter = ('name', 'price',)
