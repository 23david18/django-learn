from django.shortcuts import render, redirect
from .models import Book, DataBook
from .forms import BookForm, DataBookForm


# Create your views here.

def index(request):
    book = Book.objects.all()
    data_book = DataBook.objects.all()

    context = {
        'book': book,
        'data_book': data_book
    }
    return render(request, 'index.html', context)

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Book:index')
    else:
        form = BookForm()


    return render(request, 'create_book.html', {'form': form})

def create_data(request):
    if request.method == 'POST':
        form = DataBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Book:index')
    else:
        form = DataBookForm()

    return render(request, 'create_data.html', {'form': form})
    
