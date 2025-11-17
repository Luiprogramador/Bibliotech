from django.contrib import admin
from catalog.models import Author, Book, Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'published_date', 'isbn_number', 'genre')
# Register your models here.
