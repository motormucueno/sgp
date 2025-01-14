from django.contrib import admin
from .models import Brand, Category, product
import csv
from django.http import HttpResponse



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "is_activ", "description", "created_at", "update_at") # campos do model Band que vão aparecer no painel de administração
    search_fields = ("name",) #o campo a ser pesquisado
    list_filter = ("is_activ",) #o campo a ser filtrado

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_activ", "description", "created_at", "update_at") # campos do model Band que vão aparecer no painel de administração
    search_fields = ("name",) #o campo a ser pesquisado
    list_filter = ("is_activ",) #o campo a ser filtrado

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ("title", "band", "category", "price", "description", "created_at", "update_at") # campos do model Band que vão aparecer no painel de administração
    search_fields = ("title", "band__name", "category__name") # o campo a ser pesquisado
    list_filter = ("band", "category") # o campo a ser filtrado

