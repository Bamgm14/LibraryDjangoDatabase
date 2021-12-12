from django.db import models
from django.db.models.fields import CharField
from django.core.validators import RegexValidator
from django.utils.text import slugify
from urllib.parse import quote
from pathlib import Path
import os
import uuid

#print(settings.BASE_URL)

class bookslist(models.Model):

    Title = models.CharField(max_length=200)
    Slug = models.SlugField(unique=True, blank=True)
    ISBN = models.CharField(max_length=200, primary_key=True)
    Author_Name = models.CharField(max_length=200)
    description = models.TextField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/',default = 'images/not-found-image-15383864787lu.jpg',blank = True)

    def save(self, *args, **kwargs):
        self.Slug = slugify(quote(f"{self.Title}_{self.Author_Name}_{self.ISBN}"), allow_unicode=True)
        super(bookslist, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.Slug}'

class reader(models.Model):

    account_id = models.UUIDField(blank=True, default=uuid.uuid4, unique=True, editable=False)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=13,blank=True) # validators should be a list
    email = models.EmailField(blank=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

class issued_list(models.Model):

    ISBN = models.ForeignKey(bookslist, on_delete = models.RESTRICT)
    account_id = models.ForeignKey(reader, on_delete = models.CASCADE)
    issued_time = models.DateTimeField()




