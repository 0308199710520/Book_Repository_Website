from django.contrib import admin
from .models import Author, Book, BookInstance, Language, Genre


admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
# Register your models here.
