from django.contrib import admin
from .models import motorcycle, product, compatibility_acc

# Register your models here.
@admin.register(motorcycle)
class admin_motorcycle(admin.ModelAdmin):
    list_display = ("id", "manufacturer", "motorcycle_color", "year")
    ordering = ("manufacturer",)
    search_fields = ("motorcycle",)
    motorcycle.motorcycle_color.short_description = "motorcycle"


@admin.register(product)
class admin_product(admin.ModelAdmin):
    list_display = ("id", "code", "view_image", "accessory", "compatibility")
    ordering = ("id",)

@admin.register(compatibility_acc)
class admin_compatibility(admin.ModelAdmin):
    list_display = ("id", "code_product", "code_ref")
