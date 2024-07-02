from django.contrib import admin

from shop.models import Category, Product, Order,Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Order)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    fields = ('title',)
    pass