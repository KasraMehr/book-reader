from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'likes', 'comments')


admin.site.register(Book, BookAdmin)
