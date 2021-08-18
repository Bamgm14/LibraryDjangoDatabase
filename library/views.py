from django.shortcuts import render
from .models import bookslist
def library_details(request):
    bookslists = bookslist.objects.all()

    return render(request, 'library_base.html',{

        'Bookslist': bookslists
        
    })
def homepage(request):
    bookslists = bookslist.objects.all()

    return render(request, 'homepage.html',{

        'Bookslist': bookslists
        
    })
    
def book_details(request,book_Slug):
    try:
        selected_book = bookslist.objects.get(Slug=book_Slug)
        return render(request, 'book_details.html', {
            'book_found': True,
            'book': selected_book,
        })


    except Exception as exc:
        return render(request, 'book_details.html', {
            'book_found': False
        })
    