from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import bookslist


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit = False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class NewBook(forms.ModelForm):
    class Meta:
        model = bookslist
        fields = ["Title", "ISBN", "Author_Name", "description",'stock','image']
    def save(self, commit = True):
        book = super(NewBook, self).save(commit = False)
        if commit:
            book.save()
        return book