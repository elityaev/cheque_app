from django.contrib import admin

from .models import Product, Category, SubCategory, Receipt


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'organization', 'summa', 'processing')
    list_filter = ('date', 'organization', 'summa', 'processing')
    search_fields = ('date', 'organization')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'sum', 'sub_category')
    list_filter = ('name', 'quantity', 'price', 'sum', 'sub_category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')