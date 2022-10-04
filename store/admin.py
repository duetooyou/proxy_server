from django.contrib import admin
from .models import PetrolStore, Image, Price, Service


class PriceInline(admin.TabularInline):
    model = Price
    extra = 1


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(PetrolStore)
class PetrolAdmin(admin.ModelAdmin):
    inlines = [ImageInline, PriceInline]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('petrols',)
