from django.shortcuts import render,redirect
from .models import bookslist
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import NewUserForm
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
    
def contact(request):
    return render(request, 'Contact.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(f'Register',form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            print(f'Register')
            return redirect("/account")
        else:
            print("Hello World")
    else:
        form = NewUserForm()
    return render(request,'Register.html',{'form': form})

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.debug(request, f"You are now logged in as {username}")
                return redirect("/account")
    else:
        form = AuthenticationForm()
    return render(request,'Login.html',{'form': form})
