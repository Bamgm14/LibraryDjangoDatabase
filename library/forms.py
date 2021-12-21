from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class NewUserForm(UserCreationForm):

    email = forms.EmailField(required = True,help_text='Enter Email')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit = False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class NewBook(forms.ModelForm):

    class Meta:
        model = bookslist
        fields = ["Title", "ISBN", "Author_Name", "Slug", "description",'stock','cupboard_number', 'shelf_number', 'location', 'image']

    def save(self, commit = True):
        book = super(NewBook, self).save(commit = False)
        if commit:
            book.save()
        return book

class NewReader(forms.ModelForm):

    class Meta:
        model = reader
        fields = ["username", "first_name", "last_name", "email"]

    def save(self, commit = True):
        user = super(NewReader, self).save(commit = False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class NewIssue(forms.ModelForm):

    class Meta:
        model = issued_list
        fields = ("ISBN" ,"account_id", "issued_time")

    def save(self, commit = True):
        user = super(NewIssue, self).save(commit = False)
        if commit:
            user.save()
        return user
