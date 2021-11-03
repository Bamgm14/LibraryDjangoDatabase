from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import bookslist
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User

try:
    email = User.objects.filter(is_superuser=True).values_list('email')[0][0]
except:
    import warnings
    email = "[!]WARNING[!]"
    warnings.warn("No Email For SuperUser", Warning)

def issued_book(request):
    pass

def add_book(request):
    message=''
    if request.method == "POST":
        form = NewBook(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            message = "Book has been added."
        else:
            message = "An Error Has Occured. Possible invalid form entire."
    else:
        form = NewBook()
    return render(request,'add_book.html',{'msg':message,'form':form})

def account(request):
    #print(dir(request.user))
    return render(request,'Account.html',{"user":request.user})

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
    print(request.user)
    try:
        selected_book = bookslist.objects.get(Slug=book_Slug)
        return render(request, 'book_details.html', {
            'book_found': True,
            'book': selected_book,
            'email': email,
            'user': request.user
        })


    except Exception as exc:
        return render(request, 'book_details.html', {
            'book_found': False
        })
    
def contact(request):
    return render(request, 'Contact.html')

def _logout(request):
    logout(request)
    return redirect('/')

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
            return redirect("/register")
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
