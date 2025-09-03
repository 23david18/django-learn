from django.contrib import admin
from .models import Book, DataBook

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(Book, BookAdmin)
admin.site.register(DataBook)
