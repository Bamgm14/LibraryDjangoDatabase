from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.library_details, name = 'library_details'),
    path('books/<slug:book_Slug>', views.book_details, name = "book-details"),
    path('', views.homepage, name = "home-page"),
    path('contact/', views.contact, name = 'contact'),
    path('login/',views.Login, name = "login"),
    path('register/',views.register, name = "register"),
    path('account/',views.account, name = "account"),
    path('logout/',views._logout,name = 'logout'),
    path('add-book/',views.add_book,name = 'add book')
]