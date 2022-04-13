from django.contrib import admin
from .models import *


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'title', 'ml_product', 'stock', 'status', 'created_at', 'updated_at',)
    ordering = ('-id',)
    search_fields = ('id', 'title', 'ml_product', 'stock', 'status',)
    list_editable = ('title', 'ml_product', 'stock', 'status',)
    list_display_links = ('id',)
    list_filter = ('title', 'status', 'created_at',)
    list_per_page = 100


@admin.register(User)
class Product(admin.ModelAdmin):
    list_display = ('id',)
    list_per_page = 100
