from django.contrib import admin
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'description', 'author__name')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
