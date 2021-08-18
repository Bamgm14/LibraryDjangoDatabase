from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.library_details, name = 'library_details'),
    path('books/<slug:book_Slug>', views.book_details, name = "book-details"),
    path('', views.homepage)

]