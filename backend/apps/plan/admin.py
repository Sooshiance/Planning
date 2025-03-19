from django.contrib import admin

# Register your models here.
from .models import Book, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


class BookAdmin(admin.ModelAdmin):
    list_display = ["title"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
