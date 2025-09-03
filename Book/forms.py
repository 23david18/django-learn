from django import forms
from .models import Book, DataBook

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title']

class DataBookForm(forms.ModelForm):
    class Meta:
        model = DataBook
        fields = ['description', 'book']

        

