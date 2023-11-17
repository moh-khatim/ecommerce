from django.contrib import admin

from product import models


class ProductLineInline(admin.TabularInline):
    model = models.ProductLine
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]

admin.site.register(models.Brand)
admin.site.register(models.Category)
# admin.site.register(models.Product)
admin.site.register(models.ProductLine)

